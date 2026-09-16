from fastapi import FastAPI

app = FastAPI(
    description="This is a sample FastAPI application.",
    version="0.0.1",
)


@app.get("/")
async def read_root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
