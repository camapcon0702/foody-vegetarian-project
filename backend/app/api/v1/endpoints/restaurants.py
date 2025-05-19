from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.restaurant import Restaurant, RestaurantCreate
from app.crud import crud_restaurants
from app.core.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[Restaurant])
def read_restaurants(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_restaurants.get_restaurants(db, skip, limit)

@router.post("/", response_model=Restaurant)
def add_restaurant(restaurant: RestaurantCreate, db: Session = Depends(get_db)):
    return crud_restaurants.create_restaurant(db, restaurant)
