from shop.models import Author, Book, Brand, Category, Clothes, Electronic, ItemInCart, Material, Orders, Product, Supplier, Types
from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    orders1 = Orders.objects.all()
    orders = Orders.objects.filter(status=1)
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
    
    books = Book.objects.all()
    clothes = Clothes.objects.all()
    elecs = Electronic.objects.all()

    print(total)
    return render(request,'store/table.html',{'orders':orders,'orders1':orders1,'b':b,'c':c,'e':e,'pb':pb,'pc':pc,'pe':pe,'books':books,'clothes':clothes,'elecs':elecs})


def confirm(request,order_id):
    order = Orders.objects.get(id=order_id)
    order.status = 2
    order.statusstr = 'đã lấy hàng, chờ ship hàng'
    order.process = 60
    order.save()
    return redirect('store')

def edit(request,product_id):
    product = Product.objects.get(id=product_id)
    return render(request,"store/edit.html",{'product':product})
def addbook(request):
    if request.method == 'POST':
        name = request.POST['name']
        importprice = request.POST['importprice']
        sale = request.POST['sale']
        amount = request.POST['amount']
        saleoff = request.POST['saleoff']
        image = request.POST['image']
        mota = request.POST['mota']
        id_cate = request.POST['category']
        category = Category.objects.get(id=id_cate)
        id_author = request.POST['author']
        author = Author.objects.get(id=id_author)
        Book.objects.create(name=name,salePrice=sale,importPrice=importprice,amount=amount,saleOff=saleoff,image=image,discriminator=mota,author=author,category=category,type="Book")
        return redirect('store')
    
    categorys = Category.objects.all()
    authors = Author.objects.all()
    return render(request,"store/addbook.html",{'categorys':categorys,'authors':authors})

def addclothes(request):
    if request.method == 'POST':
        name = request.POST['name']
        importprice = request.POST['importprice']
        sale = request.POST['sale']
        amount = request.POST['amount']
        saleoff = request.POST['saleoff']
        image = request.POST['image']
        mota = request.POST['mota']
        id_material = request.POST['material']
        material = Material.objects.get(id=id_material)
        id_brand = request.POST['brand']
        brand = Brand.objects.get(id=id_brand)
        Clothes.objects.create(name=name,salePrice=sale,importPrice=importprice,amount=amount,saleOff=saleoff,image=image,discriminator=mota,material=material,brand=brand,type="Clothes")
        return redirect('store')
    
    materials = Material.objects.all()
    brands = Brand.objects.all()
    return render(request,"store/addclothes.html",{'materials':materials,'brands':brands})

def electronic(request):
    if request.method == 'POST':
        name = request.POST['name']
        importprice = request.POST['importprice']
        sale = request.POST['sale']
        amount = request.POST['amount']
        saleoff = request.POST['saleoff']
        image = request.POST['image']
        mota = request.POST['mota']
        id_types = request.POST['type']
        types = Types.objects.get(id=id_types)
        id_supp = request.POST['supplier']
        supplier = Supplier.objects.get(id=id_supp)
        Electronic.objects.create(name=name,salePrice=sale,importPrice=importprice,amount=amount,saleOff=saleoff,image=image,discriminator=mota,supplier=supplier,types=types,type="Electronic")
        return redirect('store')
    
    types = Types.objects.all()
    suppliers = Supplier.objects.all()
    return render(request,"store/addelectronic.html",{'types':types,'suppliers':suppliers})