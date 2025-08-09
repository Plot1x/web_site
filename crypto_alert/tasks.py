from celery import shared_task
import datetime

@shared_task
def send_data():
    print(f"Sending data at {datetime.datetime.now()}")
