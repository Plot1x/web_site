from django.apps import AppConfig
import threading

class CryptoAlertConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crypto_alert'

    def ready(self):
        """
        Метод ready виконується при старті Django.
        Тут ми запускаємо окремий потік, який оновлює базу даних символів криптовалют.
        """
        def update_symbols():
            """
            Функція для отримання всіх символів криптовалют з Binance
            і додавання тих, яких ще немає в базі.
            """
            from .models import CryptoSymbol
            from .modules import fetch_binance_data as fbd

            # Отримуємо список всіх символів криптовалют з Binance
            symbols = fbd.get_all_symbols()

            # Перевіряємо кожен символ і додаємо його у базу, якщо його ще немає
            for symbol in symbols:
                if not CryptoSymbol.objects.filter(symbol=symbol).exists():
                    CryptoSymbol.objects.create(symbol=symbol)

        # Запускаємо оновлення символів у окремому потоці,
        # щоб процес не блокував старт додатку
        threading.Thread(target=update_symbols, daemon=True).start()
