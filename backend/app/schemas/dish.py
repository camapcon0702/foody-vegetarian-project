from pydantic import BaseModel
from typing import Optional

class DishBase(BaseModel):
    name: str
    image: str
    price: float
    description: Optional[str] = None
    
    
class Dish(DishBase):
    IdDish: int
    IdRestaurant: int

    class Config:
        from_attributes = True