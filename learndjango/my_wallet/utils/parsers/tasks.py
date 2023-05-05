from celery import Celery
from celery.schedules import crontab
from newsdata import get_news

celery_app = Celery('tasks', broker='redis://localhost:6379/0')


@celery_app.task
def get_fresh_news():
    get_news()


@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(crontab(minute='*/60'), get_fresh_news.s())
