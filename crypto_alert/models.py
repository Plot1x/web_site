from django.db import models
from django.contrib.auth.models import User

class CryptoSelection(models.Model):
    """
    Модель для зберігання сповіщень про досягнення цін криптовалют для конкретного користувача.
    Кожен запис прив’язаний до користувача та певного символу криптовалюти.
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="Користувач, який отримує сповіщення."
    )
    crypto = models.CharField(
        max_length=15,
        help_text="Символ криптовалюти (наприклад, BTCUSDT)."
    )
    alert_price = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        help_text="Ціна, при досягненні якої сповіщення спрацює."
    )
    last_checked_price = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        default=0.0,
        help_text="Остання перевірена ціна для порівняння з alert_price."
    )
    is_expired = models.BooleanField(
        default=False,
        help_text="Вказує, чи сповіщення вже спрацювало."
    )

    def __str__(self):
        return f"{self.crypto} alert for {self.user.username} at {self.alert_price}"


class CryptoSymbol(models.Model):
    """
    Модель для зберігання всіх доступних символів криптовалют.
    Може використовуватися для автопідказок у формах.
    """
    symbol = models.CharField(max_length=10)
    
    def __str__(self): 
        return f"{self.symbol}"