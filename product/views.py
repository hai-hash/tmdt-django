from django.shortcuts import render
from .models import *

# Create your views here.

def display(request):
    products = Product.objects.all()
    if len(products) == 0:
        products = ""

    return render(request,"products.html",{'products': products})

def detail(request):
    products = Product.objects.all()[:6]
    return render(request,"product_details.html",{'products': products})