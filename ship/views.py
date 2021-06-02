from shop.models import ItemInCart, Orders
from django.shortcuts import render,redirect

# Create your views here.

def index(request):
    orders1 = Orders.objects.all()
    orders = Orders.objects.filter(status=2)
    orders3 = Orders.objects.filter(status=3)
    items = ItemInCart.objects.filter(status=0)
    list_items = []
    for item in items:
        orders2 = Orders.objects.filter(itemInCart=item,status=4)
        if len(orders2) > 0 :
            list_items.append(item)
    
    total = 0
    b = 0
    c = 0
    e = 0

    for i in list_items:
        total += i.amount
        if i.product.type == 'Book':
            b += i.amount
        elif i.product.type == 'Clothes':
            c += i.amount
        else:
            e += i.amount

    if total == 0:
        pb = 0
        pc = 0
        pe = 0
    else:
        pb = b/total*100
        pc = c/total*100
        pe = e/total*100

    print(total)
    return render(request,'ship/table.html',{'orders':orders,'orders1':orders1,'b':b,'c':c,'e':e,'pb':pb,'pc':pc,'pe':pe,'orders3':orders3})

def confirm(request,order_id):
    order = Orders.objects.get(id=order_id)
    order.status = 3
    order.statusstr = 'đang giao hàng'
    order.process = 80
    order.save()
    return redirect('ship')

def confirm1(request,order_id):
    order = Orders.objects.get(id=order_id)
    order.status = 4
    order.statusstr = 'giao hàng thành công'
    order.process = 100
    order.save()
    return redirect('ship')

    


