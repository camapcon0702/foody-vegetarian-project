from pydantic import BaseModel
from typing import Optional
from sqlalchemy.orm import relationship

class DishBase(BaseModel):
    name: str
    image: str
    price: float
    description: Optional[str] = None
    
class DishCreate(DishBase):
    IdDish: int
    IdRestaurant: int

class DishUpdate(DishBase):
    name: Optional[str] = None
    image: Optional[str] = None
    price: Optional[float] = None
    description: Optional[str] = None

class Dish(DishBase):
    IdDish: int
    IdRestaurant: int

    class Config:
        from_attributes = True