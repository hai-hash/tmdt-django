from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from .models import Account
from product.models import *

# Create your views here.
def home(request):
   if 'username' not in request.session:
        session_name = ""
   else:
        session_name = request.session.get('username')

   products = Product.objects.all()[:9]
   amountB = len(Book.objects.all()) 
   amountE = len(Electronic.objects.all())
   amountC = len(Clothes.objects.all())
   if len(products) == 0:
       products = ""

   return render(request,'index.html',{'user':session_name,'products':products,'amountB':amountB,'amountE':amountE,'amountC':amountC})

def login(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        pass_word = request.POST['password']
        try:
            user = Account.objects.filter(user_name=user_name,pass_word=pass_word)
        except Account.DoesNotExist:
            user = None

        if user != None:
            request.session['username'] = user_name
            session_name = request.session['username']
            return render(request,'index.html',{'user':session_name})
        else:
            messages.info(request,'tài khoản hoặc mật khẩu đã sai')

    if 'username' in request.session:
        del request.session['username'] 
    print(request.session.get('username'))   
    return render(request,'login.html')

def logout(request):
    if 'username' in request.session:
        del request.session['username'] 
    redirect('home')

def register(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        pass_word = request.POST['password']
        Account.objects.create(user_name=user_name,pass_word=pass_word)
        return redirect('home')

    
    return render(request,'register.html')