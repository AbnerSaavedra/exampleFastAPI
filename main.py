from typing import List, Union
 
from fastapi import FastAPI
from pydantic import BaseModel
 
app = FastAPI()

class Tag(BaseModel):
    name: str
    description: str

class Item(BaseModel):
    id: int
    name: str
    description: str
    tags: List[Tag]

listTags = []
 
@app.get("/")
def read_root():
    return {"message": "Hello from Koyeb"}

@app.post("/item")
async def createItem(item: Item):
    listTags.append(item)
    return item