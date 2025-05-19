from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import crud_dishes
from app.core.database import SessionLocal
from app.schemas.dish import Dish

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{restaurant_id}", response_model=list[Dish])
def get_dishes_by_restaurant(restaurant_id: int, db: Session = Depends(get_db)):
    return crud_dishes.get_dishes_by_restaurant(db, restaurant_id)




