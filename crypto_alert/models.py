from django.db import models
from django.contrib.auth.models import User
from .modules import pair_price_check as ppc

class CryptoSelection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    crypto = models.CharField(max_length=50)
    alert_price = models.DecimalField(max_digits=10, decimal_places=2)
    last_checked_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    is_expired = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.crypto} alert for {self.user.username} at {self.alert_price}"
    

class CryptoSymbol(models.Model):
    symbol = models.CharField(max_length=10)  
  
    
    def __str__(self):
        return f"{self.symbol}"