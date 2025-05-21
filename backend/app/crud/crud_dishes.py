from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.dish import Dish

async def get_dishes_by_restaurant(db: AsyncSession, restaurant_id: int):
    result = await db.execute(select(Dish).filter(Dish.IdRestaurant == restaurant_id))
    print(f"Received dish data: {result}")
    return result.scalars().all()
