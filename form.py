from fastapi import FastAPI, Form

app = FastAPI()

# 当用户使用html的表单数据提交数据时
# 表单与json的不同的是表单的content-type是application/x-www-form-urlencoded，并且它支持的是key-value这种
@app.post("/login/")
async def login(
    username: str = Form(...),      # 必填表单字段
    password: str = Form(None),      # 非填表单字段
    description: str = Form(None) # 非必填表单，默认为None
):
    return {"username": username, "password": password, "description": description}