from apscheduler.schedulers.background import BackgroundScheduler
from pytz import timezone
from app.services.crawler import crawling_all_restaurants, crawling_all_dishes

def start_scheduler():
    scheduler = BackgroundScheduler(timezone=timezone("Asia/Ho_Chi_Minh"))

    scheduler.add_job(crawling_all_restaurants, 'cron', hour=0, minute=0)
    scheduler.add_job(crawling_all_dishes, 'cron', hour=0, minute=5)

    scheduler.start()