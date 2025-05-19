# Foody Vegetarian

## Cấu trúc dự án
```python
foody-vegetarian-project/
│
├── backend/                          # FastAPI backend
│   ├── app/
│   │   ├── api/                      # Các route/API endpoint
│   │   │   └── v1/
│   │   │       ├── endpoints/
│   │   │       │   ├── restaurants.py
│   │   │       │   └── dishes.py
│   │   │       └── api.py
│   │   ├── core/                     # Cấu hình app, CORS, DB
│   │   │   ├── config.py
│   │   │   └── database.py
│   │   ├── crud/                     # Các thao tác với DB
│   │   │   ├── crud_restaurants.py
│   │   │   └── crud_dishes.py
│   │   ├── models/                   # Khai báo các model SQLAlchemy
│   │   │   ├── restaurant.py
│   │   │   └── dish.py
│   │   ├── schemas/                  # Pydantic models (input/output)
│   │   │   ├── restaurant.py
│   │   │   └── dish.py
│   │   ├── services/                 # Xử lý logic crawl dữ liệu
│   │   │   └── crawler.py
│   │   └── main.py                   # Entry point của app FastAPI
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend/                         # ReactJS (Vite)
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   │   ├── Home.jsx
│   │   │   └── RestaurantDetail.jsx
│   │   ├── services/                # API call
│   │   │   └── api.js
│   │   └── App.jsx
│   ├── Dockerfile
│   ├── vite.config.js
│   └── package.json
│
├── data/                             # Landing zone chứa file JSON tạm crawl
│   └── restaurants.json
│
├── nginx/
│   └── default.conf                  # Config NGINX reverse proxy
│
├── docker-compose.yml
└── README.md

```