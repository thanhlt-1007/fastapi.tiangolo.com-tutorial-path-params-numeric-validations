from fastapi import FastAPI, Path, Query
from typing import Annotated

app = FastAPI()

@app.get("/hello")
async def get_hello():
    return {
        "message": "Hello, World!"
    }

@app.get("/items/{item_id}")
async def get_items(
    item_id: Annotated[int, Path()],
    q: Annotated[str | None, Query(alias="item-query")] = None,
):
    result = {
        "item_id": item_id
    }
    if q:
        result.update({
            "q": q
        })

    return result
