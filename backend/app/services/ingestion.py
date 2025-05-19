import json
import os

from app.core.database import AsyncSessionLocal
from app.models.restaurant import Restaurant
from app.models.dish import Dish
from decimal import Decimal, ROUND_HALF_UP
from tqdm import tqdm
from sqlalchemy import text

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
        
async def insert_dishes():
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
    path = os.path.join(BASE_DIR, 'data', 'menus.json')
    
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    async with AsyncSessionLocal() as session:
        async with session.begin():
            await session.execute(text("TRUNCATE TABLE Dishes"))
            
            for restaurant_data in tqdm(data, desc="Inserting Dishes"):
                restaurant_id = restaurant_data["restaurant_id"]
                for dish in restaurant_data["menu"]:
                    try:
                        dish_obj = Dish(
                            IdDish=dish["IdDish"],
                            IdRestaurant=restaurant_id,
                            name=dish["name"],
                            image=dish["image"],
                            price=Decimal(str(dish["price"])).quantize(
                                Decimal("0.1"), rounding=ROUND_HALF_UP
                            ),
                            description=dish["description"] if dish["description"] else None
                        )
                        session.add(dish_obj)
                        
                    except KeyError as e:
                        print(f"Missing key {e} in dish data: {dish}")
                    except Exception as e:
                        print(f"Error processing dish {dish.get('name')}: {str(e)}")
            
            await session.commit()