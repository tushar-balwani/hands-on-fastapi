from fastapi import FastAPI
from enum import Enum

app = FastAPI()


@app.get("/users/{id}/info")
async def user_info(id: int):
    return {"id": id}


@app.get("/users/{id}")
async def user_info(id):
    return {"id": id}


# if we don't specify datatype, by default it will take as string

## Note:- FastAPI search from top to bottom to find a route.
## it is important to specify static routes before dynamic routes

# ANOTHER EXAMPLE WITH ENUM INPUT


class EnumExample(str, Enum):
    one = "one"
    two = "two"
    three = "three"


@app.get("/enum_example/{num}")
async def enum_example_route(num: EnumExample):
    return {"selected": num.value}
