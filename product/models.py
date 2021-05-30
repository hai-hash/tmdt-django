from django.db import models

# Create your models here.

class Color(models.Model):
    name_color = models.CharField(max_length=100,default='')
    code_color = models.CharField(max_length=100,default='')
    def __str__(self):
        return self.name_color

class Product(models.Model):
    name_product = models.CharField(max_length=100,default='')
    price = models.FloatField(default=0)
    image_main_product = models.ImageField()
    def __str__(self):
        return self.name_product
class Product_Color(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    color = models.ForeignKey(Color,on_delete=models.CASCADE)

class Image(models.Model):
    path_image = models.ImageField()
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    def __str__(self):
        return self.product.name_product

class Book(models.Model):
    category =  models.CharField(max_length=100,default='')
    author =  models.CharField(max_length=100,default='')
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    def __str__(self):
        return self.product.name_product

class Size(models.Model):
    value = models.CharField(max_length=100,default='')
    def __str__(self):
        return self.value

class Clothes(models.Model):
    material = models.CharField(max_length=100,default='')
    brand = models.CharField(max_length=100,default='')
    def __str__(self):
        return self.product.name_product

class Clothes_Size(models.Model):
    size = models.ForeignKey(Size,on_delete=models.CASCADE)
    clothes = models.ForeignKey(Clothes,on_delete=models.CASCADE)

class Supplier(models.Model):
    name = models.CharField(max_length=100,default='')
    email = models.CharField(max_length=100,default='')
    number_phone = models.CharField(max_length=100,default='')
    address = models.CharField(max_length=100,default='')
    def __str__(self):
        return self.name
class Electronic(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier,on_delete=models.CASCADE)
    def __str__(self):
        return self.product.name_product





