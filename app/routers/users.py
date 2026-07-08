from fastapi import APIRouter
from model.items import Item
from logger import logger

router = APIRouter(prefix="/users", tags=["users"])

items = []
it = Item(
    id=22,
    name="Darshan",
    price=20.2)

items.append(it)

@router.post("/items")
def create_items(item: Item):
    logger.info(f"creating items............")
    items.append(item)
    logger.info(f"stored item {item.id}")
    return {"message": "Item create", "item": item}


@router.get("/items")
def get_items():
    logger.info(f"Fetching items {len(items)}")
    return items