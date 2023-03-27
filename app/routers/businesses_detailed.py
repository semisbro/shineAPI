from typing import List

from db_management.models import Businesses_pydantic, Business

from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/businesses/detailed",
    tags=["businesses-detailed"],
)


@router.get("/", response_model=List[Businesses_pydantic])
async def get_businesses():
    users = await Business.all()
    return users


@router.get("/{biz_id}", response_model=Businesses_pydantic)
async def get_business(biz_id: int):
    user = await Business.filter(pk=biz_id).get()
    return user


# Specific
@router.put("/businesses/{business_id}", response_model=Businesses_pydantic)
async def update_business(business_id: int, business: Businesses_pydantic):
    await Business.filter(id=business_id).update(**business.dict(exclude_unset=True))
    updated_business = await Business.get(id=business_id)
    return await Businesses_pydantic.from_tortoise_orm(updated_business)
