from pydantic import BaseModel
from typing import Optional

class RestaurantBase(BaseModel):
    name: str
    address: Optional[str]
    district: Optional[str]
    average_rating: Optional[float] = 0.0
    delivery_url: Optional[str]

class RestaurantCreate(RestaurantBase):
    IdRestaurant: int

class Restaurant(RestaurantBase):
    IdRestaurant: int

    class Config:
        orm_mode = True
