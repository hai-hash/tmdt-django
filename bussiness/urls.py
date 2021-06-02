from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="busi"),
    path('edit/<int:product_id>',views.edit,name="busiedit"),
]