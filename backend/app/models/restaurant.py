from sqlalchemy import Column, Integer, String, DECIMAL
from app.core.database import Base

class Restaurant(Base):
    __tablename__ = "Restaurants"

    IdRestaurant = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    address = Column(String(255))
    district = Column(String(255))
    average_rating = Column(DECIMAL(4, 1), default=0.0)
    delivery_url = Column(String(255), nullable=True)
