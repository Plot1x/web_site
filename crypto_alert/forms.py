from django import forms
from .models import CryptoSelection


# Форма для створення цінових сповіщень
class CryptoSelectionForm(forms.ModelForm):
    # Поле для вводу торгового символу криптовалюти (наприклад, BTCUSDT)
    crypto = forms.CharField(

        # Назва поля у формі
        label="Crypto Symbol", 

        widget=forms.TextInput(
            attrs={"list": "crypto_symbols",  # Атрибут для HTML datalist
                    "placeholder": "Enter symbol"}  # Текст в полі з підсказками
                    )
    )

    class Meta:
        # Модель з якою працює форма
        model = CryptoSelection
        # Поля які будуть доступні на сайті і в які,
        # можна буде вписувати данні
        fields = ['crypto', 'alert_price']