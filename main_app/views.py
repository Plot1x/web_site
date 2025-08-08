# from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .services.pair_price_check import get_crypto_price


def homepage(request):
    return render(request, 'home.html')


def about(request):
    # return HttpResponse("My About page.")
    return render(request, 'about.html')
