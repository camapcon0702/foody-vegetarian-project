from sqlalchemy.orm import Session
from app.models.dish import Dish
from app.schemas.dish import DishCreate

def get_dishes_by_restaurant(db: Session, restaurant_id: int):
    return db.query(Dish).filter(Dish.IdRestaurant == restaurant_id).all()

def get_all_dishes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Dish).offset(skip).limit(limit).all()

def create_dish(db: Session, dish: DishCreate):
    db_dish = Dish(**dish.dict())
    db.add(db_dish)
    db.commit()
    db.refresh(db_dish)
    return db_dish

def update_dish(db: Session, dish_id: int, dish_update: DishCreate):
    db_dish = db.query(Dish).filter(Dish.id_dish == dish_id).first()
    if not db_dish:
        return None
    for key, value in dish_update.dict(exclude_unset=True).items():
        setattr(db_dish, key, value)
    db.commit()
    db.refresh(db_dish)
    return db_dish

def delete_dish(db: Session, dish_id: int):
    db_dish = db.query(Dish).filter(Dish.id_dish == dish_id).first()
    if not db_dish:
        return None
    db.delete(db_dish)
    db.commit()
    return db_dish