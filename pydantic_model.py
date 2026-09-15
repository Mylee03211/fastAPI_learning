from pydantic import BaseModel,ConfigDict,Field
from fastapi import FastAPI

app = FastAPI()

# 如果没有设置默认值，那么就表示这字段是必须要填写的
class Item(BaseModel):
    name: str
    description: str|None=None
    price: float
    tax: float|None = None


@app.post('/items/')
def create_item(item:Item):
    # fastapi 自动校验请求体，校验通过后赋值给item参数
    return item

# 仅仅能自动转化参数是不够的，我们有时候还会对参数进行处理，因此pydantic也能对数据进行访问
@app.get("/get_items/")
def get_item(item:Item):
    # 访问模型属性
    print(item)

    # 序列化为字典
    item_dict = item.model_dump()
    print(item_dict)

    # 序列化为JSON字符串
    item_json = item.model_dump_json()
    print(item_json)
    return item_dict

# 接下来讲解一下pydantic的模型配置（ConfigDict）
# 我们用item做例子，这里的price虽然我们要求是float类型，但是pydantic会自动进行类型转换
# 换句话说，如果请求体中的price输入的是字符串的price，也能通过。但是我们可以通过模型配置来要求更严格
class new_item(BaseModel):
    model_config = ConfigDict(
        strict=True,
        populate_by_name=True,
    )
    user_name: str = Field(alias="userName")
    description: str|None=None
    price: float

@app.post('/new_items/')
def create_new_item(new_item:new_item):
    return new_item