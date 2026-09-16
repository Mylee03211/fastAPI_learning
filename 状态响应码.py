from fastapi import FastAPI, status

app = FastAPI()

# 使用status即可，fastAPI内部有枚举类可以使用
# 创建资源时，使用 201 状态码
@app.get("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(name: str):
    return {"name": name}