from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()

items = []

class Item(BaseModel):
    id: int
    name: str
    price: float

# create

it = Item(
    id=22, 
    name="Darshan",
    price=20.2)

items.append(it)

@app.post("/items")
def create_items(item: Item):
    items.append(item)
    return {"message": "Item create", "item": item}    


@app.get("/items")
def get_items():
    return items
