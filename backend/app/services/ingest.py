import requests
from decimal import Decimal, ROUND_HALF_UP
from tqdm import tqdm
import mysql.connector
from mysql.connector import Error

BASE_API_URL = "http://127.0.0.1:8001/api/v1"

def get_restaurants():
    try:
        response = requests.get(f"{BASE_API_URL}/restaurants/")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Lỗi lấy danh sách nhà hàng: {e}")
        return []

def get_dishes_by_restaurant(restaurant_id):
    try:
        response = requests.get(f"{BASE_API_URL}/dishes/{restaurant_id}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Lỗi lấy món ăn cho nhà hàng {restaurant_id}: {e}")
        return []

def insert_dishes(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("TRUNCATE TABLE Dishes")
        conn.commit()
        
        restaurants = get_restaurants()
        if not restaurants:
            print("Không có dữ liệu nhà hàng")
            return
        
        for restaurant in tqdm(restaurants, desc="Processing Restaurants"):
            restaurant_id = restaurant.get("IdRestaurant")
            if not restaurant_id:
                continue

            dishes = get_dishes_by_restaurant(restaurant_id)
            if not dishes:
                continue
                
            for dish in dishes:
                try:
                    dish_id = dish.get("IdDish")
                    name = dish.get("name", "Unknown Dish")
                    description = dish.get("description")
                    price = Decimal(str(dish.get("price", 0.0))).quantize(
                        Decimal("0.1"), rounding=ROUND_HALF_UP
                    )
                    image = dish.get("image", "")
                    
                    cursor.execute(
                        """
                        INSERT IGNORE INTO Dishes (IdDish, IdRestaurant, name, image, price, description)
                        VALUES (%s, %s, %s, %s, %s, %s)
                        """,
                        (dish_id, restaurant_id, name, image, price, description),
                    )
                except Exception as e:
                    print(f"Lỗi khi xử lý món {name} của nhà hàng {restaurant_id}: {e}")
                    continue
        
        conn.commit()
        print("Insert món ăn thành công!")
        
    except Error as e:
        conn.rollback()
        print(f"Lỗi database: {e}")
    except Exception as e:
        conn.rollback()
        print(f"Lỗi: {e}")