from controller.user import UserOrm
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get():
    return UserOrm.get_all()

@app.get("/{id}")
def get_user(id:str):
    return UserOrm.get(id=id)

@app.post("/")
def create(name: str, password:str):
    return UserOrm.create(name=name, password=password)

@app.delete("/{id}")
def delete(id: int):
    return UserOrm.delete(id=id)