from fastapi import APIRouter
from app.api.v1.endpoints import restaurants, dishes

api_router = APIRouter()
api_router.include_router(restaurants.router, prefix="/restaurants", tags=["restaurants"])
api_router.include_router(dishes.router, prefix="/dishes", tags=["dishes"])
