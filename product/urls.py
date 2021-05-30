from django.urls import path
from . import views

urlpatterns = [
    path('',views.display,name='product'),
    path('detail/',views.detail,name='detailproduct'),
    
]