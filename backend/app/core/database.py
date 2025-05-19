from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# DATABASE_URL = "mysql+pymysql://root:matkhau1@db:3306/foody_vegetarian"

# URL của toy
DATABASE_URL= "mysql+pymysql://root:12345678@localhost:3306/foody_vegetarian"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
