# http://lccalhost:8080, 这个URL分别由协议+域名+端口组成，只要任意一个不同就是不同源，也就是跨域

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 配置CORS中，允许访问的前端
# noinspection bad-argument-type
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000"
    ],
    allow_credentials=True,# 允许携带Cookie
    allow_methods=["*"], # 允许的HTTP方法
    allow_headers=["*"], # 允许的请求头
    max_age=600, # 预检请求的缓存时间，单位秒
)
@app.get("/")
async def root():
    return {"message":"Hello World"}