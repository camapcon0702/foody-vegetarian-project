from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.dish import Dish, DishCreate, DishUpdate
from app.crud import crud_dishes
from app.core.database import SessionLocal

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

@router.get("/", response_model=list[Dish])
def get_all_dishes(db: Session = Depends(get_db)):
    return crud_dishes.get_all_dishes(db)

@router.post("/add", response_model=Dish)
def add_dish(dish: DishCreate, db: Session = Depends(get_db)):
    return crud_dishes.create_dish(db, dish)

@router.put("/edit/{dish_id}", response_model=Dish)
def update_dish(dish_id: int, dish_update: DishUpdate, db: Session = Depends(get_db)):
    updated_dish = crud_dishes.update_dish(db, dish_id, dish_update)
    if not updated_dish:
        raise HTTPException(status_code=404, detail="Không tìm thấy ID món")
    return updated_dish

@router.delete("/delete/{dish_id}", response_model=Dish)
def delete_dish(dish_id: int, db: Session = Depends(get_db)):
    deleted_dish = crud_dishes.delete_dish(db, dish_id)
    if not deleted_dish:
        raise HTTPException(status_code=404, detail="Không tìm thấy ID món")
    return deleted_dish



