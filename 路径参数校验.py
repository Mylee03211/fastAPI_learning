# 与查询参数使用Query添加校验一样，路径参数使用path进行校验
from fastapi import FastAPI,Path
from typing import Annotated

app = FastAPI()

@app.get("/root/{id}")
async def read_root(
        # 为路径参数添加元数据和校验
        id:Annotated[int,Path(title="用户ID",description="用户ID",ge=1)]):
    return {"id":id}