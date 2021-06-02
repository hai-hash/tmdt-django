from django.shortcuts import render,redirect
from shop.models import *

def index(request):
    products = Product.objects.all()
    return render(request,"busi/busi.html",{'products':products})

def edit(request,product_id):
    if request.method == 'POST':
        id = request.POST['id']
        product = Product.objects.get(id=id)
        
        saleoff = request.POST['saleoff']
        image = request.POST['image']
       
        product.saleOff=saleoff
        product.image=image
       
        product.save()
        return redirect('busi')


    product = Product.objects.get(id=product_id)
    return render(request,"busi/edit.html",{'product':product})
