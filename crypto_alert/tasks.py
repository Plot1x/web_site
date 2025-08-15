from celery import shared_task
from .models import CryptoSelection
from datetime import datetime
from .modules import fetch_binance_data as fbd
from decimal import Decimal

@shared_task
def send_data():
    selections = CryptoSelection.objects.all()
    print(f"--- {datetime.now()} ---")

    get_all_crypto = fbd.get_all_tickers()

    for sel in selections:

        get_all_tickers = next((item["price"] for item in get_all_crypto if item["symbol"] == sel.crypto), None)

        if sel.last_checked_price is not None:
            if sel.last_checked_price < sel.alert_price <= Decimal(get_all_tickers):
                print(f"User: {sel.user.username}, Crypto: {sel.crypto}, "
                    f"Alert Price: {sel.alert_price}, Now Price: {sel.last_checked_price}",
                    "Ціна пересікла знизу вгору")
                sel.is_expired = True
                
            elif sel.last_checked_price > sel.alert_price >= Decimal(get_all_tickers):
                print(f"User: {sel.user.username}, Crypto: {sel.crypto}, "
                    f"Alert Price: {sel.alert_price}, Now Price: {sel.last_checked_price}",
                    "Ціна пересікла зверху в низ")
                sel.is_expired = True
        else:
            pass

        sel.last_checked_price = get_all_tickers
        sel.save()