# fastAPI的中间件相当于是一个对路径函数执行之前或者之后进行功能性增强的东西
import time
from fastapi import FastAPI,Request
app = FastAPI()

# 声明这是一个中间件
@app.middleware("http")
# 这里的http是，将下面的函数封装为http请求的一个中间件，之后每一个http请求都需要走这个中间件
async def add_process_time_header(
        request: Request, # 当前请求对象
        call_next):
    # 请求前的处理，记录开始时间
    start_time = time.time()

    # 将请求传递给下一个中间件或者路由函数
    response = await call_next(request) # 调用下一个中间件或者路由函数的回调

    # 响应后的处理，计算处理时间并添加响应头
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.get("/")
async def root():
    return {"Hello": "World"}

# fastAPI中有内置的中间件
# HTTPSRedirectMiddleware	强制将 HTTP 请求重定向为 HTTPS
# TrustedHostMiddleware	限制允许访问的主机名
# GZipMiddleware	自动压缩响应内容
# CORSMiddleware	处理跨域请求（下一章详细介绍）

from fastapi.middleware.gzip import GZipMiddleware
app.add_middleware(GZipMiddleware,minimum_size=1000)

@app.get("/ping")
async def ping():
    return {"message":"这个响应可能会被GZip压缩"}