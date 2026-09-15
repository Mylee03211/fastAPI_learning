from fastapi import FastAPI

# 创建FastAPI应用实例
app = FastAPI()

# 定义根路径的GET路由
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/get_itemId/{item_id}")
def get_itemId(item_id:int, q:str=None):
    return {"item_id": item_id, "q": q}