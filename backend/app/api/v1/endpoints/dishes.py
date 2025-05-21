from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud import crud_dishes
from app.core.database import AsyncSessionLocal
from app.schemas.dish import Dish

router = APIRouter()

async def get_async_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session

@router.get("/{restaurant_id}", response_model=list[Dish])
async def get_dishes_by_restaurant(restaurant_id: int, db: AsyncSession = Depends(get_async_db)):
    return await crud_dishes.get_dishes_by_restaurant(db, restaurant_id)




