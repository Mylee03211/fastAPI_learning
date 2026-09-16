# 当函数参数既不是路径参数，也不是请求体的时候，FASTAPI会将其自动解释为查询参数
from fastapi import FastAPI

app = FastAPI()

# skip 和 limit 是查询参数，有默认值
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    # 模拟分页查询
    return fake_items_db[skip : skip + limit]

@app.get("/items/message")
async def read_message(message : str|None = None):# 默认值为None的话，表示这个参数不是必填的
    return {"message": message}