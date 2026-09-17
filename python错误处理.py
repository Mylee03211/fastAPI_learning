# 通过HTTPException 或者 自定义异常处理器来处理更复杂的错误场景。
from fastapi import FastAPI,HTTPException

app = FastAPI()

items = {"foo": "The Foo Wrestlers", "bar": "The Bar Fighters"}

@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        # 资源不在的时候，抛出404错误
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")
    return {"item_id": item_id}

# status_code	int	HTTP 状态码（必填）
# detail	Any	错误详情，可以是字符串、字典、列表等
# headers	dict | None	额外的响应头（可选）


# 自定义错误详情，detail参数可以是任意类型，不局限于字符串。
@app.get("/items/more/{id}")
async def read_more_item(
        id: str
):
    if id == "invalid":
        raise HTTPException(
            status_code=400,
            detail={
                "error_code":"INVALID_ID",
                "message":"商品ID格式不正确",
                "hint":"请使用字母数字组合的ID"
            }
        )
    return {"id": id}