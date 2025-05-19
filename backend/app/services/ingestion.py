import json
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.restaurant import Restaurant

def load_json_data(file_path: str):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)
    
def insert_restaurants(data: list, db: Session):
    for item in data:
        restaurant = Restaurant(**item)
        db.add(restaurant)
    db.commit()
    print(f"Đã thêm {len(data)} nhà hàng vào cơ sở dữ liệu.")