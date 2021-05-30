from django.db import models

# Create your models here.

class Account(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

class Staff(models.Model):
    name = models.CharField(max_length=100)
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
class Address(models.Model):
    location = models.CharField(max_length=100)
class FullName(models.Model):
    firstName = models.CharField(max_length=100,default='')
    lastName = models.CharField(max_length=100,default='')
class Customer(models.Model):
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    address = models.ForeignKey(Address,on_delete=models.CASCADE)
    fullName = models.ForeignKey(FullName,on_delete=models.CASCADE)

class Material(models.Model):
    name = models.CharField(max_length=100,default='')

class Brand(models.Model):
    name = models.CharField(max_length=100,default='')
class Author(models.Model):
    name = models.CharField(max_length=100,default='')
class Category(models.Model):
    name = models.CharField(max_length=100,default='')

class Types(models.Model):
    name = models.CharField(max_length=100,default='')
class Supplier(models.Model):
    name =  models.CharField(max_length=100,default='')

class Product(models.Model):
    name =models.CharField(max_length=100,default='')
    salePrice = models.FloatField(default=0)
    importPrice = models.FloatField(default=0)
    amount = models.IntegerField(default=0)
    saleOff = models.FloatField(default=0)
    discriminator = models.CharField(max_length=100,default='')
    supplier = models.ForeignKey(Supplier,on_delete=models.CASCADE,default='')
    types =  models.ForeignKey(Types,on_delete=models.CASCADE,default='')
    author =  models.ForeignKey(Author,on_delete=models.CASCADE,default='')
    category =  models.ForeignKey(Category,on_delete=models.CASCADE,default='')
    brand =  models.ForeignKey(Brand,on_delete=models.CASCADE,default='')
    material =  models.ForeignKey(Material,on_delete=models.CASCADE,default='')

class Loves(models.Model):
    customer =  models.ForeignKey(Customer,on_delete=models.CASCADE,default='')
    product =  models.ForeignKey(Product,on_delete=models.CASCADE,default='')

class Comment(models.Model):
    product =  models.ForeignKey(Product,on_delete=models.CASCADE,default='')
    customer =  models.ForeignKey(Customer,on_delete=models.CASCADE,default='')
    content = models.CharField(max_length=200,default='')

class Cart(models.Model):
    customer =  models.ForeignKey(Customer,on_delete=models.CASCADE,default='')

class Shipment(models.Model):
    type = models.CharField(max_length=100,default='')
class Payment(models.Model):
    type = models.CharField(max_length=100,default='')
class ItemInCart(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,default='')
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,default='')
    createDate = models.DateField()
    status = models.IntegerField(default=1)

class Order(models.Model):
    itemInCart = models.ForeignKey(ItemInCart,on_delete=models.CASCADE,default='')
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,default='')
    payment = models.ForeignKey(Payment,on_delete=models.CASCADE,default='')
    shipment = models.ForeignKey(Shipment,on_delete=models.CASCADE,default='')
    status = models.IntegerField(default=0)
    total = models.FloatField(default=0)
    address = models.CharField(max_length=100,default='')
    phone = models.CharField(max_length=100,default='')


