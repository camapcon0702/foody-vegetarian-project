import json
import os

from app.core.database import AsyncSessionLocal
from app.models.restaurant import Restaurant
from app.models.dish import Dish
from sqlalchemy import select
from decimal import Decimal, ROUND_HALF_UP

async def insert_restaurants_from_json():
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    path = os.path.join(BASE_DIR, 'data', 'restaurants.json')
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Restaurant.IdRestaurant))
        existing_ids = {row[0] for row in result.fetchall()}

        new_restaurants = []
        for item in data:
            if item['Id'] in existing_ids:
                continue

            try:
                avg_rating = float(item['AvgRating'])
            except (ValueError, TypeError, KeyError):
                avg_rating = 0.0

            new_restaurants.append(Restaurant(
                IdRestaurant=item['Id'],
                name=item['Name'],
                address=item['Address'],
                district=item['District'],
                average_rating=avg_rating,
                delivery_url=item['DeliveryUrl']
            ))

        session.add_all(new_restaurants)
        await session.commit()


async def insert_dishes_from_json():
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    path = os.path.join(BASE_DIR, 'data', 'menus.json')

    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Restaurant.IdRestaurant))
        valid_restaurant_ids = {row[0] for row in result.fetchall()}

        result = await session.execute(select(Dish.IdDish))
        existing_dish_ids = {row[0] for row in result.fetchall()}

        new_dishes = []
        for restaurant_data in data:
            restaurant_id = restaurant_data["restaurant_id"]
            if restaurant_id not in valid_restaurant_ids:
                continue

            for dish in restaurant_data["menu"]:
                if dish["IdDish"] in existing_dish_ids:
                    continue

                new_dishes.append(Dish(
                    IdDish=dish["IdDish"],
                    IdRestaurant=restaurant_id,
                    name=dish["name"],
                    image=dish["image"],
                    price=Decimal(str(dish["price"])).quantize(
                        Decimal("0.1"), rounding=ROUND_HALF_UP
                    ),
                    description=dish["description"]
                ))

        session.add_all(new_dishes)
        await session.commit()