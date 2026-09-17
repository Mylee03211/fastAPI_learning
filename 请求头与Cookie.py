from typing import Annotated
from fastapi import FastAPI,Header,Cookie

app = FastAPI()

@app.get("/items/")
async def read_items(
        # 接收User-Agent请求头
        x_token: Annotated[str|None,Header()] = None
):
    return {"x_token": x_token}

# python不允许连接词也就是x-token，只允许下划线x_token。但是fastAPI会自动处理这些。
# x_token	X-Token	下划线自动转为连字符
# user_agent	User-Agent	同上
# content_type	Content-Type	同上

# 而有些请求头可能会出现多次，因此可以选用list[str]来进行接收

# cookie 参数
@app.get('/items/cookie')
async def get_cookie(
        session_token: Annotated[str|None,Cookie()] = None
):
    return {"session_token": session_token}