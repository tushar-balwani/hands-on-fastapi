from fastapi import FastAPI

app = FastAPI()

### parameters which are not specified in path are considered as query parameters

items = ["item 1", "item 2", "item 3", "item 4", "item 5", "item 6", "item 7"]


@app.get("/")
async def path_params(limit: int = 10, offset: int = 0):
    return {"data": items[offset : offset + limit]}


### another example
# query: str | None = None syntax works on 3.10+. other options is
# from typing import Optional
# query: Optional[str] = None
@app.get("/{item}")
async def path_params_other(item: int, query: str | None = None):
    data = {"data": items[item]}
    if query:
        data.update({"query": query})

    return data


## NOTE - pydantic automatically tries to convert given input to required type
## Example: for limit: int -> it will convert string '10' to int 10
