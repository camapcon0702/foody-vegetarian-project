from fastapi import APIRouter
from app.api.v1.endpoints import restaurants, dishes, crawl, ingestion

api_router = APIRouter()
api_router.include_router(restaurants.router, prefix="/restaurants", tags=["restaurants"])
api_router.include_router(dishes.router, prefix="/dishes", tags=["dishes"])
api_router.include_router(crawl.router, prefix="/crawl", tags=["Crawl"])
api_router.include_router(ingestion.router, prefix="/ingestion", tags=["Ingestion"])
