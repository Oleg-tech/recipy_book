from apscheduler.schedulers.background import BackgroundScheduler

from .bot_controller import main_polling


def start():
    scheduler = BackgroundScheduler(timezone='Europe/Kiev')
    scheduler.add_job(main_polling)
    scheduler.start()
