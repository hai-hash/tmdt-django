from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="sale"),
    path('confirm/<int:order_id>',views.confirm,name="confirm"),
    
]
