from typing import Union
from fastapi import FastAPI
from app.models import models
from app.database import engine, Base

app = FastAPI()

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"fido": "transactions"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}