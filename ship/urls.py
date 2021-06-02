from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="ship"),
    path('confirm/<int:order_id>',views.confirm,name="confirm"),
    path('confirm1/<int:order_id>',views.confirm1,name="confirm1"),
    
]
