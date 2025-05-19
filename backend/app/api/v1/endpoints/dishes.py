from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.dish import Dish #, DishCreate
from app.crud import crud_dishes
from app.core.database import AsyncSessionLocal

router = APIRouter()

async def get_async_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session

@router.get("/restaurant/{restaurant_id}", response_model=list[Dish])
def get_dishes_by_restaurant(restaurant_id: int, db: AsyncSession = Depends(get_async_db)):
    return crud_dishes.get_dishes_by_restaurant(db, restaurant_id)

# @router.post("/", response_model=Dish)
# def add_dish(dish: DishCreate, db: AsyncSession = Depends(get_async_db)):
#     return crud_dishes.create_dish(db, dish)
