from apscheduler.schedulers.background import BackgroundScheduler
from pytz import timezone
from app.services.crawler import crawling_all_restaurants, crawling_all_dishes
from app.services.ingestion import insert_restaurants_from_json, insert_dishes_from_json

def start_scheduler():
    scheduler = BackgroundScheduler(timezone=timezone("Asia/Ho_Chi_Minh"))

    scheduler.add_job(crawling_all_restaurants, 'cron', hour=0, minute=0)
    scheduler.add_job(crawling_all_dishes, 'cron', hour=0, minute=5)
    scheduler.add_job(insert_restaurants_from_json, 'cron', hour=0, minute=10)
    scheduler.add_job(insert_dishes_from_json, 'cron', hour=0, minute=15)
    scheduler.start()