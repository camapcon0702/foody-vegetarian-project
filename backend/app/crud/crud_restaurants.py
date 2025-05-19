from sqlalchemy.orm import Session
from app.models.restaurant import Restaurant
from app.schemas.restaurant import RestaurantCreate

def get_restaurants(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Restaurant).offset(skip).limit(limit).all()

def create_restaurant(db: Session, restaurant: RestaurantCreate):
    db_restaurant = Restaurant(**restaurant.dict())
    db.add(db_restaurant)
    db.commit()
    db.refresh(db_restaurant)
    return db_restaurant
