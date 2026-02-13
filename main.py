from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="FastAPI routes without a database")

@app.get("/")
def home():
    return {"message": "Welcome to my API"}

# Fake database (just Python list)
items = []

# Pydantic model
class Item(BaseModel):
    id: int
    name: str
    price: float

# Get All items

@app.get("/items", response_model=List[Item])
def get_items():
    return items

# Get single item by ID

@app.get("/items/{item_id}")
def get_single_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

# Create a new item

@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return {"message": "Item created successfully", "item": item}

# Update an existing item by ID

@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(items):
        if item.id == item_id:
            items[index] = updated_item
            return {"message": "Item updated successfully", "item": updated_item}
    raise HTTPException(status_code=404, detail="Item not found")

# Delete an item by ID

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for index, item in enumerate(items):
        if item.id == item_id:
            deleted_item = items.pop(index)
            return {
                "message": "Item deleted successfully",
                "deleted_item": deleted_item
            }
    raise HTTPException(status_code=404, detail="Item not found")