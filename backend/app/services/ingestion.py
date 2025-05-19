import json
import os

from app.core.database import AsyncSessionLocal
from app.models.restaurant import Restaurant

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