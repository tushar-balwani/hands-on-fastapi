from fastapi import FastAPI, Query

app = FastAPI()


## we have to use `Query` function to add validations as shown in following example
# if we don't want to give any default value, we can use Query(...) instead


@app.get("/")
async def example(q: str | None = Query(None, min_length=3, max_length=3)):
    result = {"items": [{"itemid": "foo"}, {"itemid": "bar"}]}
    if q:
        result.update({"q": q})
    return result


# Working with non-primitive types
@app.get("/other")
async def other_example(q: list[str] = Query(...)):
    result = {"items": [{"itemid": "foo"}, {"itemid": "bar"}]}
    if q:
        result.update({"q": q})
    return result


# Swagger docs update example
@app.get("/docs-update")
async def docs_update_example(
    q: int = Query(
        ...,
        min_length=3,
        max_length=3,
        title="Doc update",
        description="Swagger docs details update",
        deprecated=True,
        alias="query",
        ge=10,
        le=100,
    )
):
    result = {"items": [{"itemid": "foo"}, {"itemid": "bar"}]}
    result.update({"q": q})
    return result


# Note:- gt and lt params have a bug. use ge and le instead


# hide schema example
@app.get("/hidden")
def hidden_query(q: str | None = Query(None, include_in_schema=False)):
    if q:
        return {"message": "found"}
    return {"message": "invalid input"}
