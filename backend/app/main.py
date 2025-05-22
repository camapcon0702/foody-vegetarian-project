from app.services.scheduler import start_scheduler
from fastapi import FastAPI
from app.api.v1.api import api_router
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import Base, engine
from app.models import restaurant, dish
from app.services.crawler import crawling_all_restaurants, crawling_all_dishes
from app.services.ingestion import insert_restaurants_from_json, insert_dishes_from_json
import time

app = FastAPI(title="Foody Vegetarian API", root_path="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/v1")

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        
    start_scheduler()

    crawling_all_restaurants()

    time.sleep(1)

    crawling_all_dishes()

    await insert_restaurants_from_json()

    await insert_dishes_from_json()