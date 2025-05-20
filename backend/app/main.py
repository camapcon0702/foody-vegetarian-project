from app.services.scheduler import start_scheduler
from fastapi import FastAPI
from app.api.v1.api import api_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Foody Vegetarian API")

# Cấu hình CORS (cho phép frontend gọi API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Gắn router chính
app.include_router(api_router, prefix="/api/v1")
start_scheduler()

