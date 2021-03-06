from shop.models import ItemInCart, Orders
from django.shortcuts import render,redirect
from django.core.mail import send_mail
from shop.models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from shop.decorators import allowed_user

# Create your views here.
@login_required(login_url="/login")
@allowed_user(allowed_role=["sale"])
def index(request):
    if request.method == 'POST':
        name = request.POST['search1']
        if name == "":
            orders1 = Orders.objects.all()
        else:
            account = User.objects.get(username=name)
            customer = Customer.objects.get(account=account)
            cart = Cart.objects.get(customer=customer)
            items= ItemInCart.objects.filter(cart=cart)
            orders1 = []
            for item in items:
                order7 = Orders.objects.filter(itemInCart=item)
                if len(order7) > 0:
                    orders1.append(order7[0])
            
    else:
        orders1 = Orders.objects.all()
    orders = Orders.objects.filter(status=0)
    items = ItemInCart.objects.filter(status=0)
    list_items = []
    for item in items:
        orders2 = Orders.objects.filter(itemInCart=item,status=2)
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
    return render(request,'sale/table.html',{'orders':orders,'orders1':orders1,'b':b,'c':c,'e':e,'pb':pb,'pc':pc,'pe':pe})

def confirm(request,order_id):
    send_mail('Thông Báo đặt hàng thành công','xin chào , đơn hàng của bạn đã được chấp nhận, bạn hay thường xuyên theo dõi đơn hàng của mình nhé , Hoàng lol','whynotme1131999@gmail.com',['hoanga4bg@gmail.com'],fail_silently=False)
    order = Orders.objects.get(id=order_id)
    order.status = 1
    order.statusstr = 'đã xác nhận, chờ lấy hàng'
    order.process = 50
    order.save()
    return redirect('sale')

    

