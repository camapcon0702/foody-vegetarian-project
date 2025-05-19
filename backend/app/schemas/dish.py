from pydantic import BaseModel
from typing import Optional

class DishBase(BaseModel):
    name: str
    image: str
    price: float
    description: Optional[str]

class DishCreate(DishBase):
    IdDish: int
    IdRestaurant: int

class Dish(DishBase):
    IdDish: int
    IdRestaurant: int

    class Config:
        orm_mode = True
