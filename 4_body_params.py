from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float


@app.post("/")
async def body_param_example(item: Item):
    # for converting item object to dictionary
    item_dict = item.model_dump()
    return item
