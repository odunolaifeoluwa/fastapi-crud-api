from fastapi import APIRouter, HTTPException, status
from typing import List
from app.models.item import Item

router = APIRouter(
    prefix="/items",
    tags=["Items"]
)

# Fake database
items = []

# GET All Items

@router.get("/", response_model=List[Item])
def get_items():
    return items

# GET Single Item

@router.get("/{item_id}", response_model=Item)
def get_single_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

# CREATE an Item

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_item(item: Item):
    items.append(item)
    return {
        "message": "Item created successfully",
        "item": item
    }

# UPDATE Item

@router.put("/{item_id}")
def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(items):
        if item.id == item_id:
            items[index] = updated_item
            return {
                "message": "Item updated successfully",
                "item": updated_item
            }
    raise HTTPException(status_code=404, detail="Item not found")

# DELETE Item

@router.delete("/{item_id}")
def delete_item(item_id: int):
    for index, item in enumerate(items):
        if item.id == item_id:
            deleted_item = items.pop(index)
            return {
                "message": "Item deleted successfully",
                "deleted_item": deleted_item
            }
    raise HTTPException(status_code=404, detail="Item not found")