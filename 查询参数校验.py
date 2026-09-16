# 有些时候我们传入的参数我们需要校验，这个时候就需要通过Query和Annotated，在不改变函数逻辑的情况下增强参数校验。
from typing import Annotated
from fastapi import FastAPI,Query

app = FastAPI()

@app.get("/items/")
async def read_items(
        # 使用Annotated+Query添加校验
        q : Annotated[str|None,Query(max_length=50)]=None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# Annotated[str|None,]类型注解，表示q可以是字符串或者None
# Query(max_length=59) 校验规则，q的最大长度为50
# 使用Annotated最大好处是，可以给变量添加元数据，而元数据就是描述数据的一个东西
async def test(
        user_name: Annotated[str,Query(max_length=10),"这是用户名"]="admin"
):
    return {"user_name": user_name}
# 就比如上面这个例子，user_name是str类型，然后最大长度是10，元数据是：这是用户名，最后的默认值是admin

# 然后有些时候我们会传入多个同一个参数，比如我们要传入的city参数有多个，如果直接使用查询参数的话，FastAPI会将其解释为请求体
@app.get("/citys")
async def citys(
    # q 可以在 URL 中出现多次，值会被收集为列表
    city: Annotated[list[str] | None, Query()] = None,
):
    query_items = {"city": city}
    return query_items

# 我们看看不适用Query的情况
@app.get("/citys2")
async def citys2(
    # q 可以在 URL 中出现多次，值会被收集为列表
    city2: Annotated[list[str] | None]
):
    query_items = {"city2": city2}
    return query_items
# 调用的时候就会说body missing