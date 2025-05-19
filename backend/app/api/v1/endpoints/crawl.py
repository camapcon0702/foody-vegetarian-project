from fastapi import APIRouter, HTTPException
from app.services.crawler import crawling_all_restaurants, crawling_all_dishes

router = APIRouter()

@router.post("/restaurants", tags=["Crawl"])
def crawl_restaurants():
    try:
        crawling_all_restaurants()
        return {"message": "Crawl nhà hàng thành công"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/dishes", tags=["Crawl"])
def crawl_dishes():
    try:
        crawling_all_dishes()
        return {"message": "Crawl món ăn thành công"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))