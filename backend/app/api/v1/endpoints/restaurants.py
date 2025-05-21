from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.restaurant import Restaurant, RestaurantCreate, RestaurantOut
from app.crud import crud_restaurants
from app.core.database import AsyncSessionLocal

router = APIRouter()

async def get_async_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session

@router.get("/", response_model=list[Restaurant])
async def read_restaurants(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_async_db)):
    return await crud_restaurants.get_restaurants(db, skip, limit)

@router.get("/all/")
async def read_all_restaurants(db: AsyncSession = Depends(get_async_db)):
    return await crud_restaurants.get_all_restaurants(db)

@router.post("/", response_model=Restaurant)
async def add_restaurant(restaurant: RestaurantCreate, db: AsyncSession = Depends(get_async_db)):
    return await crud_restaurants.create_restaurant(db, restaurant)

@router.get("/search-by-dish", response_model=list[RestaurantOut])
async def search_restaurants_by_dish(name: str = Query(..., min_length=1), db: AsyncSession = Depends(get_async_db)):
    return await crud_restaurants.find_restaurants_by_dish(db, name)

from fastapi import HTTPException


@router.get("/{restaurant_id}", response_model=RestaurantOut)
async def get_restaurant_by_id(
    restaurant_id: int,
    db: AsyncSession = Depends(get_async_db)
):
    restaurant = await crud_restaurants.get_restaurant_by_id(db, restaurant_id)
    if restaurant is None:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return restaurant
