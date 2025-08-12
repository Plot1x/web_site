from celery import shared_task
from .models import CryptoSelection
from datetime import datetime
from .modules import pair_price_check as ppc

@shared_task
def send_data():
    selections = CryptoSelection.objects.all()
    print(f"--- {datetime.now()} ---")
    for sel in selections:

        get_crypto_price = ppc.get_crypto_price(sel.crypto)

        if sel.last_checked_price is not None:
            if sel.last_checked_price < sel.alert_price <= get_crypto_price:
                print(f"User: {sel.user.username}, Crypto: {sel.crypto}, "
                    f"Alert Price: {sel.alert_price}, Now Price: {sel.now_price}",
                    "Ціна пересікла знизу вгору")
                
            elif sel.last_checked_price > sel.alert_price >= get_crypto_price:
                print(f"User: {sel.user.username}, Crypto: {sel.crypto}, "
                    f"Alert Price: {sel.alert_price}, Now Price: {sel.now_price}",
                    "Ціна пересікла зверху в низ")
        else:
            pass

        sel.last_checked_price = get_crypto_price
        sel.save()