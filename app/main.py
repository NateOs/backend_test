from typing import Union
from fastapi import FastAPI
from app.models import models
from app.database import engine, Base
from app.routers import transaction_routes

app = FastAPI()

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)


# Add the transaction routes to the FastAPI app
app.include_router(transaction_routes.router)

@app.get("/")
def read_root():
    return {"fido": "transactions"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}