from sqlalchemy.orm import Session
from app.models.restaurant import Restaurant
from app.models.dish import Dish
from app.schemas.restaurant import RestaurantCreate

def get_restaurants(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Restaurant).offset(skip).limit(limit).all()

def get_all_restaurants(db: Session):
    return db.query(Restaurant).all()

def create_restaurant(db: Session, restaurant: RestaurantCreate):
    db_restaurant = Restaurant(**restaurant.dict())
    db.add(db_restaurant)
    db.commit()
    db.refresh(db_restaurant)
    return db_restaurant

def find_restaurants_by_dish(db: Session, dish_name: str):
    dishes = db.query(Dish).filter(Dish.name.ilike(f"%{dish_name}%")).all()
    restaurant_ids = {dish.IdRestaurant for dish in dishes}

    restaurants = db.query(Restaurant).filter(Restaurant.IdRestaurant.in_(restaurant_ids)).all()
    return restaurants