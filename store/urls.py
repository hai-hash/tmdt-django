from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="store"),
    path('add/book',views.addbook,name="addbook"),
    path('add/clothes',views.addclothes,name="addclothes"),
    path('add/electronic',views.electronic,name="addelectronic"),
]