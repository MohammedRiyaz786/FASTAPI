from fastapi import FastAPI
from typing import Optional
app=FastAPI()

@app.get("/")

async def first():
    return{"message":"hello Riyaz"}

# path parameter

@app.get("/items/{item_id}")
async def index(item_id):
    return {"product_id":item_id}

# query parameter
@app.get("/query/")
async def query_param(q:int=0,m:Optional[int]=91):
    return {"query is":q,"m is":m}

#file path
@app.get("/filepath{file_path:path}")
async def path(file_path:str):
    return {"file_path":file_path}

