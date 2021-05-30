from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Color)
admin.site.register(Product_Color)
admin.site.register(Book)
admin.site.register(Clothes)
admin.site.register(Electronic)
admin.site.register(Size)
admin.site.register(Clothes_Size)
admin.site.register(Supplier)