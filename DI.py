from fastapi import FastAPI,Depends

app = FastAPI()

def get_user():
    return {"username":"admin","password":"123456"}

@app.get("/get_user/")
def get_user_info(user = Depends(get_user)):
    return user
