from src.post.router import router

import uvicorn

from fastapi import FastAPI


app = FastAPI()
app.include_router(router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)