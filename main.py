from fastapi import FastAPI, Query, Path
from enum import Enum
from pydantic import BaseModel
from typing import Optional

class Employee(BaseModel):
    name:str
    email:str
    empid:int

app = FastAPI()

@app.post("/emp")
async def createEmployee(emp: Employee):
    em=emp.dict()
    if emp.name == "Rohit":
        return "Hello"
    return em

@app.get("/")
async def firstFunction():
    return "Hello world"

@app.get("/emp/me")
async def getTestEmployee():
    return {"message": "Hello Rohit"}

@app.get("/emp/{id}")
async def getEmployeeId(id:int):
    return {"id":id}

class Model(str, Enum):
    alto= "Alto"
    swift= "Swift"
    wagonR= "WagonR"
    eco= "Eco"

@app.get("/model/{model_name}")
async def getModel(model_name: Model):
    if model_name == Model.alto:
        return {"message": "You have selected Alto Car"}
    elif model_name == 'Eco':
        return {"message": "You have selected ECo Taxi Car"}
    elif model_name:
        if None:
            return "Hello"
        return {"message": "You have selected Swift Car"}
    else:
        return {"message": "You have selected  WagonR Car"}

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items")
async def getItems(skip:int =0 , limit:int =10):
    return fake_items_db[skip: skip + limit]

@app.get("/ecm")
async def read_item(id: int, q: Optional[str]= None):
    if q:
        return {"item_id": id, "q": q}
    return {"item_id":id}

@app.get("/testQuery/{item_id}")
async def query_example(item_id:int=Path(..., title="Enter Item id")):
    return {"id": item_id}   


def fun_arg(*):
    