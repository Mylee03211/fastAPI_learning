from fastapi import FastAPI,Depends
from typing import Annotated
app = FastAPI()

# 定义依赖函数
def common_parameters(q: str|None = None):
    return q

# 在路由中使用依赖
@app.get("/items/")
def read_items(commons: dict = Depends(common_parameters)):
    return {"commons": commons}


# 多个路由函数可以公用一个依赖函数
@app.get("/users/")
def read_users(commons: dict = Depends(common_parameters)):
    return {"commons": commons}


# 依赖也可以存在子依赖
def child_common_parameters(q: str = Depends(common_parameters)):
    # 在子依赖对q进行校验
    if q=="admin":
        return q + "hello"
    return q


def add_function():
    print("完成了新增的操作")

# 有些时候我们只需要依赖函数的功能性增强，并不需要依赖函数的返回值，这个时候可以在注解上添加dependencies 参数
@app.get("/users/dependencies",dependencies=[Depends(add_function)])
def read_users():
    return {"code":"200"}


# 同时我们也可以设置全局依赖，这样所有的路由函数都会执行这个依赖函数，用法如下
app2 = FastAPI(dependencies=[Depends(add_function)])


# 介绍一下依赖注入的yield。我们举一个连接数据库，然后查库，最后关闭连接
def db_func():
    db = "假装这个是建立连接的函数"
    yield db
    db = "假装这个是关闭连接的函数"

def add_sql(db = Depends(db_func)):
    db = "假装这里是处理数据库的"
    return "success"

# 这里的yield就是将连接好的db交给add_sql使用，等它使用好了之后再回到依赖函数db_func中执行db的关闭。