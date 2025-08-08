from django import forms

CRYPTO_CHOICES = [
        ('BTCUSDT', 'Bitcoin (BTC)'),
        ('ETHUSDT', 'Ethereum (ETH)'),
        ('SOLUSDT', 'Solana (SOL)'),
    ]

class CryptoForm(forms.Form):
    alert_price = forms.CharField(label="Ціна", max_length=10000000)
    crypto = forms.ChoiceField(choices=CRYPTO_CHOICES, label="Виберіть криптовалюту")