from django.apps import AppConfig
import threading

class CryptoAlertConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crypto_alert'

    def ready(self):
        def update_symbols():
            from .models import CryptoSymbol
            from .modules import pair_price_check as ppc
            symbols = ppc.get_all_crypto_symbol()
            for symbol in symbols:
                if not CryptoSymbol.objects.filter(symbol=symbol).exists():
                    CryptoSymbol.objects.create(symbol=symbol, name=symbol)
                    
        threading.Thread(target=update_symbols).start()
