from fastapi import FastAPI
from app.routes.items import router as items_router

app = FastAPI(title="Clean Structured API", description="A simple API following clean architecture principles", version="1.0.0")

# Include routes
app.include_router(items_router)

# Root endpoint
@app.get("/")
def home():
    return {"message": "Welcome to my Clean Structured API"}