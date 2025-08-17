from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    """
        Форма для заповнення людині, яка хоче зареєструватись на сайті.
    """
    class Meta:
        model = User
        fields = ("username", "password1", "password2")