from sqlalchemy.orm import Session
from app.models.dish import Dish

def get_dishes_by_restaurant(db: Session, restaurant_id: int):
    return db.query(Dish).filter(Dish.IdRestaurant == restaurant_id).all()

