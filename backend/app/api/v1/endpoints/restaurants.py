from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.schemas.restaurant import Restaurant, RestaurantCreate, RestaurantOut
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

@router.get("/all/")
def read_all_restaurants(db: Session = Depends(get_db)):
    return crud_restaurants.get_all_restaurants(db)

@router.post("/", response_model=Restaurant)
def add_restaurant(restaurant: RestaurantCreate, db: Session = Depends(get_db)):
    return crud_restaurants.create_restaurant(db, restaurant)

@router.get("/search-by-dish", response_model=list[RestaurantOut])
def search_restaurants_by_dish(name: str = Query(..., min_length=1), db: Session = Depends(get_db)):
    return crud_restaurants.find_restaurants_by_dish(db, name)
