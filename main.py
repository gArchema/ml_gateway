import uvicorn
from fastapi import FastAPI

from src.routers import semantic_search_router

app = FastAPI()

app.include_router(semantic_search_router)


@app.get('/')
def read_root():
    return {"Hello": "World"}


@app.get('/ping')
def ping():
    return 'pong'


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
