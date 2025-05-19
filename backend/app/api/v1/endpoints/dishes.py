from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud import crud_dishes
from app.core.database import AsyncSessionLocal
from app.schemas.dish import Dish, DishCreate, DishUpdate

router = APIRouter()

async def get_async_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session

@router.get("/{restaurant_id}", response_model=list[Dish])
async def get_dishes_by_restaurant(restaurant_id: int, db: AsyncSession = Depends(get_async_db)):
    return await crud_dishes.get_dishes_by_restaurant(db, restaurant_id)


@router.get("/", response_model=list[Dish])
async def get_all_dishes(db: AsyncSession = Depends(get_async_db)):
    return await crud_dishes.get_all_dishes(db)

@router.post("/add", response_model=Dish)
async def add_dish(dish: DishCreate, db: AsyncSession = Depends(get_async_db)):
    return await crud_dishes.create_dish(db, dish)

@router.put("/edit/{dish_id}", response_model=Dish)
async def update_dish(dish_id: int, dish_update: DishUpdate, db: AsyncSession = Depends(get_async_db)):
    updated_dish = crud_dishes.update_dish(db, dish_id, dish_update)
    if not updated_dish:
        raise HTTPException(status_code=404, detail="Không tìm thấy ID món")
    return await updated_dish

@router.delete("/delete/{dish_id}", response_model=Dish)
async def delete_dish(dish_id: int, db: AsyncSession = Depends(get_async_db)):
    deleted_dish = crud_dishes.delete_dish(db, dish_id)
    if not deleted_dish:
        raise HTTPException(status_code=404, detail="Không tìm thấy ID món")
    return await deleted_dish



