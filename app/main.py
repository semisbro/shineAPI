import uvicorn
from fastapi import FastAPI

from app.routers.business_entries import router as basic_biz_router
from app.routers.businesses_detailed import router as business_router

from db_management.models import Businesses_pydantic, Business
from database import init_db
from app.routers import business_entries

app = FastAPI()
app.include_router(router=basic_biz_router)
app.include_router(router=business_router)


@app.on_event("startup")
async def startup_event():
    await init_db()


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
