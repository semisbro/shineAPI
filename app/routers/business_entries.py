from typing import List

from db_management.models import Businesses_pydantic, Business

from fastapi import APIRouter

router = APIRouter(
    prefix="/businesses",
    tags=["businesses"],
)


@router.get("/", response_model=List[Businesses_pydantic])
async def get_businesses():
    users = await Business.all()
    return users


@router.get("/{biz_id}", response_model=Businesses_pydantic)
async def get_business(biz_id: int):
    user = await Business.filter(pk=biz_id).get()
    return user