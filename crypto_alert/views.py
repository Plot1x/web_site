from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import CryptoForm
from .models import CryptoSelection
from .modules.pair_price_check import get_crypto_price
from decimal import Decimal

def post_alert(request):
    if request.method == 'POST':
        form = CryptoForm(request.POST)
        if request.user.is_authenticated:
            if form.is_valid():
                CryptoSelection.objects.create(
                    user=request.user,
                    alert_price = form.cleaned_data['alert_price'],
                    crypto = form.cleaned_data['crypto'],
                )

                return redirect("home")
        else:
            return redirect("login")
    else:
        form = CryptoForm()
    alerts = CryptoSelection.objects.filter(user=request.user.id) 
    return render(request, 'home.html', {'form': form, 'alerts': alerts})

def delete_alert(request, alert_id):
    if request.method == 'POST':
        alert = CryptoSelection.objects.get(pk=alert_id)
        alert.delete()
    return redirect('home')



