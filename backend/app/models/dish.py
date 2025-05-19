from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey
from app.core.database import Base

class Dish(Base):
    __tablename__ = "Dishes"

    IdDish = Column(Integer, primary_key=True, index=True)
    IdRestaurant = Column(Integer, ForeignKey("Restaurants.IdRestaurant", ondelete="CASCADE"))
    name = Column(String(255), nullable=False)
    image = Column(String(255), nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)
    description = Column(String(255))
