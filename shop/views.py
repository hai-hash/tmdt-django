
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate
from django.contrib.auth.models import User, Group
from django.views import View
from .models import *
import datetime
from .models import Product
from django.contrib.auth.decorators import login_required
from .decorators import allowed_user
# Create your views here.


def default(request):
    user = request.user
    print(user.username)
    print("ten:"+str(user.groups.name))
    if user.groups.filter(name="user").exists():
        return redirect("/")
    elif user.groups.filter(name="store").exists():
        return redirect("/store/")
    elif user.groups.filter(name="busi").exists():
        return redirect("/busi/")
    else:
        return redirect("/sale/")

def index(request):
    list = Product.objects.all()
    list.reverse()
    return render(request,"shop/index.html",{"list":list})


def detail(request,pro_id):
    product=Product.objects.get(pk=pro_id)
    list_comment=[]
    list_comment=Comment.objects.filter(product=product)

    user = request.user
    totalLike = len(Loves.objects.filter(product=product))
    liked = 0
    if user.is_authenticated:
        customer = Customer.objects.get(account=user)
        love = Loves.objects.filter(customer=customer, product=product)

        if len(love) == 0:
            liked=0
        else:
            liked=1

    return render(request,"shop/detail.html",{"product":product,"list_comment":list_comment,"liked":liked, "totalLike":totalLike})

def search(request):
    name=request.GET['name']
    list=[]
    list=Product.objects.filter(name=name)
    return render(request,"shop/index.html",{"list":list})

@login_required(login_url="/login")
@allowed_user(allowed_role=["user"])
def cart(request):
    if request.user.is_authenticated:
        user=request.user
        customer=Customer.objects.get(account=user)
        cart=Cart.objects.get(customer=customer)

        list_item=[]
        list_item = ItemInCart.objects.filter(cart=cart,status=1)
        total=0.0
        for item in list_item:
            total+=((item.product.salePrice*(1-item.product.saleOff))*item.amount)

        list_ship=Shipment.objects.all()
        list_pay=Payment.objects.all()
        return render(request, "shop/cart.html", {"list_item": list_item,"list_ship":list_ship,"list_pay":list_pay,"total":total})
    else:
        redirect(request,"/login")

def elec(request):
    list = Electronic.objects.all()
    return render(request, "shop/index.html", {"list": list})
def book(request):
    list = Book.objects.all()
    return render(request, "shop/index.html", {"list": list})
def clothes(request):
    list = Clothes.objects.all()
    return render(request, "shop/index.html", {"list": list})


def cancelOrder(request,order_id):
    order = Orders.objects.get(id=order_id)
    order.delete()
    item=order.itemInCart
    item.status=1
    item.delete()
    return  redirect("/order")


def addToCart(request,pro_id):
    user = request.user
    customer = Customer.objects.get(account=user)
    cart = Cart.objects.get(customer=customer)
    product=Product.objects.get(id=pro_id)

    item=ItemInCart(cart=cart,createDate=datetime.datetime.now(),status=1,amount=1,product=product)
    item.save()
    return redirect("/cart")


def deleteInCart(request,item_id):
    item = ItemInCart.objects.get(id=item_id)
    item.delete()
    return redirect("/cart")

def editForm(request,item_id):
    item = ItemInCart.objects.get(id=item_id)
    return render(request,"shop/editCart.html",{"item":item})

def editCart(request):
    id = request.POST['id']
    amount=request.POST['amount']
    item=ItemInCart.objects.get(id=id)
    item.amount=amount
    item.save()
    return redirect("/cart")


def addComment(request):
    user = request.user
    customer = Customer.objects.get(account=user)
    id=request.POST['id']
    comment=request.POST['comment']
    product = Product.objects.get(id=id)

    comment=Comment(customer=customer,content=comment,product=product)
    comment.save()
    return redirect("/detail/"+id)


def like(request,pro_id):
    user = request.user
    customer = Customer.objects.get(account=user)
    product = Product.objects.get(pk=pro_id)
    love=Loves(customer=customer,product=product)
    love.save()
    return redirect("/detail/" + str(pro_id))

def dislike(request,pro_id):
    user = request.user
    customer = Customer.objects.get(account=user)
    product = Product.objects.get(pk=pro_id)
    love=Loves.objects.get(customer=customer,product=product)
    love.delete()
    return redirect("/detail/" + str(pro_id))


class Login(View):
    def get(self,request):
        return render(request, "shop/login.html",{"message":""})
    def post(self,request):
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is None:
            return redirect("/login",context={"message":"Tài khoản hoặc mật khẩu không chính xác"})
        return redirect("/")


class Register(View):
    def get(self,request):
        return render(request, "shop/register.html",{"message":""})
    def post(self,request):
        username=request.POST['username']
        password=request.POST['password']
        print(password)
        user=[]
        user=User.objects.filter(username=username)
        if len(user)==0:
            group=Group.objects.get(name="user")
            newuser=User.objects.create_user(username=username,password=password)

            newuser.save()
            group.user_set.add(newuser)
            thisuser = User.objects.get(username=newuser.get_username())
            cus=Customer(account=thisuser)

            cus.save()
            cart=Cart(customer=cus)
            cart.save()
            return redirect("/login")

        return redirect("/register")


class Order(View):

    def get(self,request):
        list_order=[]
        user = request.user
        customer = Customer.objects.get(account=user)
        cart = Cart.objects.get(customer=customer)

        list_item = []
        list_item = ItemInCart.objects.filter(cart=cart)
        for item in list_item:
            try:
                order = Orders.objects.get(itemInCart=item)
                list_order.append(order)
            except order.DoesNotExist:
                pass
        list_order.reverse()

        return render(request,"shop/history.html",{"list_order":list_order})


    def post(self,request):
        user = request.user
        customer = Customer.objects.get(account=user)
        cart = Cart.objects.get(customer=customer)

        list_item = []
        list_item = ItemInCart.objects.filter(cart=cart, status=1)

        phone=request.POST['phone']
        address=request.POST['address']
        pay=request.POST['pay']
        ship=request.POST['ship']
        payment=Payment.objects.get(id=pay)
        shipment=Shipment.objects.get(id=ship)

        for item in list_item:
            total=(item.product.salePrice*(1-item.product.saleOff)*item.amount)
            order=Orders(itemInCart=item,shipment=shipment,payment=payment,total=total,address=address,phone=phone,status=0)
            order.save()
            item.status=0
            item.save()

        return redirect("/cart")