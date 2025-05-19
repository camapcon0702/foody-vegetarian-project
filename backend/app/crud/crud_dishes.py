from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.dish import Dish
from app.schemas.dish import DishCreate, DishUpdate

async def get_dishes_by_restaurant(db: AsyncSession, restaurant_id: int):
    result = await db.execute(select(Dish).filter(Dish.IdRestaurant == restaurant_id))
    print(f"Received dish data: {result}")
    return result.scalars().all()

async def get_all_dishes(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(Dish).offset(skip).limit(limit))
    return result.scalars().all()

async def create_dish(db: AsyncSession, dish: DishCreate):
    db_dish = Dish(**dish.dict())
    db.add(db_dish)
    await db.commit()
    await db.refresh(db_dish)
    return db_dish

async def update_dish(db: AsyncSession, dish_id: int, dish_update: DishUpdate):
    db_dish = (await db.execute(select(Dish).filter(Dish.IdDish == dish_id))).scalars().first()
    if not db_dish:
        return None
    for key, value in dish_update.dict(exclude_unset=True).items():
        setattr(db_dish, key, value)
    await db.commit()
    await db.refresh(db_dish)
    return db_dish

async def delete_dish(db: AsyncSession, dish_id: int):
    db_dish = (await db.execute(select(Dish).filter(Dish.IdDish == dish_id))).scalars().first()
    if not db_dish:
        return None
    await db.delete(db_dish)
    await db.commit()
    return db_dish