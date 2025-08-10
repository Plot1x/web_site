from celery import shared_task
from .models import CryptoSelection
from datetime import datetime

@shared_task
def send_data():
    selections = CryptoSelection.objects.all()
    print(f"--- {datetime.now()} ---")
    for sel in selections:
        print(f"User: {sel.user.username}, Crypto: {sel.crypto}, "
              f"Alert Price: {sel.alert_price}, Now Price: {sel.now_price}")
