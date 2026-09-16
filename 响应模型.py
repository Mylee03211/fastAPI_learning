from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float


@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int):
    # 返回的数据会自动按照 Item 模型过滤和校验
    # 直接使用类型注解是最简单的方式
    return {
        "name": "Foo",
        "description": "A very nice Item",
        "price": 22.2,
        "secret": "this should not be visible",  # 不在 Item 中的字段会被过滤，因此可以用来顾虑掉敏感字段如密码
    }

# 还有几个参数比较实用，可以顾虑掉默认值、空值和未设置值的字段
# response_model_exclude_unset	排除未设置值的字段
# response_model_exclude_defaults	排除值为默认值的字段
# response_model_exclude_none	排除值为 None 的字段
# 包含/排除特定字段
# 使用 response_model_include 和 response_model_exclude 精确控制输出字段：