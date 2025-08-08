from django.db import models
from django.contrib.auth.models import User

class CryptoSelection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    crypto = models.CharField(max_length=50)
    alert_price = models.DecimalField(max_digits=10, decimal_places=2)
    now_price = models.DecimalField(max_digits=10, decimal_places=2)
