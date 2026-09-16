# 路径参数是在URL路径中的动态参数
from fastapi import FastAPI

app = FastAPI()


# 基本用法，fastAPI会自动进行类型转换
@app.get("/users/{id}")
async def get_user(id:int):
    return {"id":id}


# 路径顺序很重要，如果多个路由匹配到同一个URL时候，会优先选择第一个路径，比如有一个/users/me的路径，其实上下两个路径都能
# 匹配上，但是会优先选择第一个路径，因此我们会规定固定路径的一定要写在动态路径前面。
# 必须在 /users/{user_id} 之前定义
@app.get("/users/me")
async def read_user_me():
    """获取当前用户信息"""
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    """根据 ID 获取用户信息"""
    return {"user_id": user_id}


# 包含路径的路径参数
# :path 表示该参数可以匹配包含斜杠的路径
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}