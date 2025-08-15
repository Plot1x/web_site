from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import CryptoSelectionForm
from .models import CryptoSelection, CryptoSymbol

def post_alert(request):
    if request.method == 'POST':
        form = CryptoSelectionForm(request.POST)
        if request.user.is_authenticated:
            if form.is_valid():
                CryptoSelection.objects.create(
                    user=request.user,
                    crypto=form.cleaned_data['crypto'],
                    alert_price=form.cleaned_data['alert_price']
                )

                return redirect("home")
        else:
            return redirect("login")
    else:
        form = CryptoSelectionForm()
    alerts = CryptoSelection.objects.filter(user=request.user.id) 
    symbols = CryptoSymbol.objects.all()
    return render(request, 'home.html', {'form': form, 'alerts': alerts, 'symbols' : symbols})

def delete_alert(request, alert_id):
    if request.method == 'POST':
        alert = CryptoSelection.objects.get(pk=alert_id)
        alert.delete()
    return redirect('home')



