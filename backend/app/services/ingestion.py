import json
import os

from app.core.database import AsyncSessionLocal
from app.models.restaurant import Restaurant
from app.models.dish import Dish
from sqlalchemy import select
from decimal import Decimal, ROUND_HALF_UP

async def insert_restaurants_from_json():
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
    path = os.path.join(BASE_DIR, 'data', 'restaurants.json')
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    async with AsyncSessionLocal() as session:
        async with session.begin():
            for item in data:
                try:
                    avg_rating = float(item['AvgRating'])
                except (ValueError, TypeError, KeyError):
                    avg_rating = 0.0
                stmt = select(Restaurant.IdRestaurant).where(Restaurant.IdRestaurant == item['Id'])
                result = await session.execute(stmt)
                exists_id = result.scalar()

                if exists_id:
                    continue
                restaurant = Restaurant(
                    IdRestaurant=item['Id'],
                    name=item['Name'],
                    address=item['Address'],
                    district=item['District'],
                    average_rating=avg_rating,
                    delivery_url=item['DeliveryUrl']
                )
                session.add(restaurant)
        await session.commit()        
        
async def insert_dishes_from_json():
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
    path = os.path.join(BASE_DIR, 'data', 'menus.json')
    
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    async with AsyncSessionLocal() as session:
        async with session.begin():
            for restaurant_data in data:
                restaurant_id = restaurant_data["restaurant_id"]
                stmt = select(Restaurant.IdRestaurant).where(Restaurant.IdRestaurant == restaurant_id)
                result = await session.execute(stmt)
                exists_id = result.scalar()
                
                if not exists_id:
                    continue  
                
                for dish in restaurant_data["menu"]:
                    stmt = select(Dish.IdDish).where(Dish.IdDish == dish["IdDish"])
                    result = await session.execute(stmt)
                    exists_dish = result.scalar()
                        
                    if exists_dish:
                        continue
                            
                    dish_obj = Dish(
                            IdDish=dish["IdDish"],
                            IdRestaurant=restaurant_id,
                            name=dish["name"],
                            image=dish["image"],
                            price=Decimal(str(dish["price"])).quantize(
                                Decimal("0.1"), rounding=ROUND_HALF_UP
                            ),
                            description=dish["description"]
                        )
                    session.add(dish_obj)    
        await session.commit()