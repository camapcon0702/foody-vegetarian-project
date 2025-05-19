from pydantic import BaseModel
from typing import Optional
from sqlalchemy.orm import relationship

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

class RestaurantOut(BaseModel):
    IdRestaurant: int
    name: str
    address: str | None
    district: str | None
    average_rating: float
    delivery_url: str | None

    class Config:
        orm_mode = True
