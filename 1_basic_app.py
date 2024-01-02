from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def get_example():
    return {"message": "Get Example"}


@app.post("/")
async def post_example():
    return {"message": "Post Example"}


@app.put("/{id}")
async def put_example(id: str):
    return {"message": "Put Example"}


@app.patch("/{id}")
async def patch_example(id: str):
    return {"mesage": "Patch Example"}


@app.delete("/{id}")
async def delete_example(id: str):
    return {"message": "Delete Example"}
