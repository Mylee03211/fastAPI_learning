# fastAPI提供了方便的访问静态资源的方法，也就是StaticFiles，
# 需要安装：pip install aiofiles

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()
# 挂载静态文件目录