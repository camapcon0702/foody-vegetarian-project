from app.services.ingestion import insert_restaurants_from_json, insert_dishes_from_json
from fastapi import APIRouter, HTTPException


router = APIRouter()

@router.post("/restaurants", tags=["Ingestion"])
async def ingestion_restaurants():
    try:
        await insert_restaurants_from_json()
        return {"message": "Ingestion nhà hàng thành công"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/dishes")
async def insert_dishes():
    try:
        await insert_dishes_from_json()
        return {"message": "Success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))