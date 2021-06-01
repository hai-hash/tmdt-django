from django.db import models

from django.contrib.auth.models import User


class Supplier(models.Model):
    name =  models.CharField(max_length=100,default='')
    def __str__(self):
        return self.name
class Staff(models.Model):
    name = models.CharField(max_length=100)
    account = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class Address(models.Model):
    location = models.CharField(max_length=100)
    def __str__(self):
        return self.location
class FullName(models.Model):
    firstName = models.CharField(max_length=100,default='')
    lastName = models.CharField(max_length=100,default='')
    def __str__(self):
        return self.firstName+self.lastName
class Customer(models.Model):
    account = models.ForeignKey(User,on_delete=models.CASCADE)


class Material(models.Model):
    name = models.CharField(max_length=100,default='')
    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=100,default='')
    def __str__(self):
        return self.name
class Author(models.Model):
    name = models.CharField(max_length=100,default='')
    def __str__(self):
        return self.name
class Category(models.Model):
    name = models.CharField(max_length=100,default='')
    def __str__(self):
        return self.name
class Types(models.Model):
    name = models.CharField(max_length=100,default='')
    def __str__(self):
        return self.name


class Product(models.Model):
    name =models.CharField(max_length=100,default='')
    salePrice = models.FloatField(default=0)
    importPrice = models.FloatField(default=0)
    amount = models.IntegerField(default=0)
    saleOff = models.FloatField(default=0)
    type=models.CharField(max_length=100,default='')
    image=models.CharField(max_length=100,default='')
    discriminator = models.CharField(max_length=100,default='')
    def __str__(self):
        return self.name

class Book(Product):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='')


class Electronic(Product):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, default='')
    types = models.ForeignKey(Types, on_delete=models.CASCADE, default='')

class Clothes(Product):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, default='')
    material = models.ForeignKey(Material, on_delete=models.CASCADE, default='')

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
    def __str__(self):
        return self.type
class Payment(models.Model):
    type = models.CharField(max_length=100,default='')
    def __str__(self):
        return self.type
class ItemInCart(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,default='')
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,default='')
    amount = models.IntegerField(default=1)
    createDate = models.DateField()
    status = models.IntegerField(default=1)


class Orders(models.Model):
    itemInCart = models.ForeignKey(ItemInCart,on_delete=models.CASCADE,default='')
    payment = models.ForeignKey(Payment,on_delete=models.CASCADE,default='')
    shipment = models.ForeignKey(Shipment,on_delete=models.CASCADE,default='')
    status = models.IntegerField(default=0)
    total = models.FloatField(default=0)
    address = models.CharField(max_length=100,default='')
    phone = models.CharField(max_length=100,default='')


