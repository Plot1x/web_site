from django import forms
from .models import CryptoSelection

class CryptoSelectionForm(forms.ModelForm):
    crypto = forms.CharField(
        label="Crypto Symbol",
        widget=forms.TextInput(attrs={"list": "crypto_symbols", "placeholder": "Enter symbol"})
    )

    class Meta:
        model = CryptoSelection
        fields = ['crypto', 'alert_price']