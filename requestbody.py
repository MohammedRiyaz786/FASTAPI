from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app= FastAPI()

class User(BaseModel):
    name:str
    company:str
    employe_code:int
    adress: Optional[str]=None

@app.post("/item/")
async def create_item(user:User):
    return user

