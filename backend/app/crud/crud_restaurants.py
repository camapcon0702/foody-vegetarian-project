from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.restaurant import Restaurant
from app.models.dish import Dish
from app.schemas.restaurant import RestaurantCreate

async def get_restaurants(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(
        select(Restaurant).offset(skip).limit(limit)
    )
    return result.scalars().all()

async def get_all_restaurants(db: AsyncSession):
    result = await db.execute(select(Restaurant))
    return result.scalars().all()

async def create_restaurant(db: AsyncSession, restaurant: RestaurantCreate):
    db_restaurant = Restaurant(**restaurant.dict())
    db.add(db_restaurant)
    await db.commit()
    await db.refresh(db_restaurant)
    return db_restaurant

async def find_restaurants_by_dish(db: AsyncSession, dish_name: str):
    result_dishes = await db.execute(
        select(Dish).filter(Dish.name.ilike(f"%{dish_name}%"))
    )
    dishes = result_dishes.scalars().all()
    restaurant_ids = {dish.IdRestaurant for dish in dishes}

    if not restaurant_ids:
        return []

    result_restaurants = await db.execute(
        select(Restaurant).filter(Restaurant.IdRestaurant.in_(restaurant_ids))
    )
    return result_restaurants.scalars().all()
