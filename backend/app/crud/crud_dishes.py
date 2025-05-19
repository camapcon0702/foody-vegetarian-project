from sqlalchemy.orm import Session
from app.models.dish import Dish
from app.schemas.dish import DishCreate

def get_dishes_by_restaurant(db: Session, restaurant_id: int):
    return db.query(Dish).filter(Dish.IdRestaurant == restaurant_id).all()

def create_dish(db: Session, dish: DishCreate):
    db_dish = Dish(**dish.dict())
    db.add(db_dish)
    db.commit()
    db.refresh(db_dish)
    return db_dish
