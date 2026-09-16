# 与路径操作函数中使用 Query、Path 声明校验的方式一样，Pydantic 模型内部使用 Field 声明字段校验：
from typing import Annotated
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str = Field(min_length=1, max_length=100, description="商品名称")  # 必填，1-100字符
    description: str | None = Field(default=None, max_length=300, description="商品描述")  # 可选
    price: float = Field(gt=0, description="商品价格")  # 必填，必须大于 0
    tax: float | None = Field(default=None, ge=0, description="税费")  # 可选，>= 0


@app.post("/items/")
async def create_item(item: Item):
    return item


# pydantic模型的字段可以是另一个pydantic
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


# 子模型：图片
class Image(BaseModel):
    url: HttpUrl      # 自动校验是否为有效的 URL
    name: str


# 主模型：商品，包含图片子模型
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    image: Image | None = None  # 可选的图片信息


@app.post("/items/")
async def create_item(item: Item):
    return item
