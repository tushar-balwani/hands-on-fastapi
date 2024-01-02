from fastapi import FastAPI, Path, Query

app = FastAPI()


## we have to use `Path` function to add validations as shown in following example
# if we don't want to give any default value, we can use Query(...) instead


@app.get("/{id}")
async def example(
    id: int
    | None = Path(
        None, ge=0, le=6, title="example", description="path patam validation example"
    ),
    q: str | None = Query(None, min_length=3, max_length=3),
):
    items = ["item 1", "item 2", "item 3", "item 4", "item 5", "item 6", "item 7"]
    data = {"data": items[id]}
    if q:
        data.update({"q": q})
    return data


# one most common python error is we can't provide non-default arguments after default

"""
@app.get("/{id}")
async def example(
    id: int
    | None = Path(
        None, ge=0, le=6, title="example", description="path patam validation example"
    ),
    q: str
):
    pass
"""


# to fix this issue, we can simply convert it to kwargs type as follows
@app.get("/other/{id}")
async def other_example(
    *,
    id: int
    | None = Path(
        None, ge=0, le=6, title="example", description="path patam validation example"
    ),
    q: str
):
    items = ["item 1", "item 2", "item 3", "item 4", "item 5", "item 6", "item 7"]
    data = {"data": items[id]}
    if q:
        data.update({"q": q})
    return data


## all parameters after * are treated as kwargs
