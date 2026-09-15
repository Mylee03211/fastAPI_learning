from fastapi import FastAPI, Form

app = FastAPI()

# 表单数据

@app.post("/login/")
async def login(
    username: str = Form(),      # 必填表单字段
    password: str = Form(),      # 必填表单字段
    description: str = Form(None) # 非必填表单，默认为None
):
    return {"username": username, "password": password, "description": description}