from fastapi import FastAPI, Body
from pydantic import BaseModel, Field

app = FastAPI()

# There are 2 ways to get body params


# first - create model and use
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.post("/first")
async def first_example(item: Item):
    return {"item": item}


# second - use Body method from FastAPI
@app.post("/second")
async def second_example(
    item: dict[str, str] = Body(..., title="Body Param example", desc="")
):
    return {"item": item}


# =========================================================================

# There are 3 ways to define example in swagger doc


# way-1: as Field
class ItemWithFieldExample(BaseModel):
    name: str = Field(..., examples=["John"])
    description: str | None = Field(None, examples=["Some Description"])
    price: float = Field(..., examples=[100])
    tax: float | None = Field(None, examples=[15.5])


@app.post("/way1")
async def way1_example(
    item: ItemWithFieldExample = Body(..., title="Body Param example", desc="")
):
    return {"item": item}


# ---------------------------------------------------
# way-2: as Meta
class ItemWithMetaExample(BaseModel):
    name: str
    description: str | None
    price: float
    tax: float | None = None

    class Config:
        schema_extra = {
            "example": {
                "name": "John",
                "description": "Something",
                "price": 100,
                "tax": 15,
            }
        }


@app.post("/way2")
async def way2_example(
    item: ItemWithMetaExample = Body(..., title="Body Param example", desc="")
):
    return {"item": item}


# ---------------------------------------------------


# way-3: Inline
@app.post("/way3")
async def way3_example(
    item: dict[str, str] = Body(
        ...,
        title="Body Param example",
        desc="",
        example={"name": "John", "description": "Something"},
    )
):
    return {"item": item}


# =========================================================================
# Body wih multiple params


class ItemNew(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    password: str
    email: str
    fullname: str


@app.post("/multi-body-params")
async def multi_body_params(
    *, item: Item = Body(..., embed=True), user: User = Body(..., embed=True)
):
    return {"item": item, "user": user}


# =========================================================================
# Body wih Nested params


class ItemNested(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    password: str
    email: str
    fullname: str
    items: list[ItemNested]


@app.post("/nested-body-params")
async def nested_body_params(user: User):
    return {"user": user}


# =========================================================================
# Body wih distributed params


class UserBase(BaseModel):
    username: str
    password: str
    email: str
    fullname: str


class UserInput(UserBase):
    pass


class UserOutput(UserBase):
    hashed_password: str


# response_model=UserOutput is used to format response
@app.post("/distributed-body-params", response_model=UserOutput)
async def distributed_body_params(user: UserInput):
    hashed_password = "$$$" + user.password + "$$$"
    dump = UserOutput(**user.model_dump(), hashed_password=hashed_password)
    return {"user": dump}
