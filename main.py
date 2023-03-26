import uvicorn
from fastapi import FastAPI

from db_management.models import User_Pydantic, BusinessUser
from database import init_db

app = FastAPI()

from typing import List


@app.on_event("startup")
async def startup_event():
    await init_db()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/users", response_model=List[User_Pydantic])
async def get_users():
    users = await BusinessUser.all()
    return users


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
