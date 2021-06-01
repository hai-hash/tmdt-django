from django.urls import path,include

from . import views
from .views import Login,Register,Order
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login',auth_views.LoginView.as_view(template_name="shop/login.html"),name="login"),
    path('logout',auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('register',Register.as_view()),
    path('search',views.search),
    path('detail/<int:pro_id>',views.detail),
    path('cart',views.cart),
    path('', views.index),
    path('order',Order.as_view()),
    path('order/cancel/<int:order_id>',views.cancelOrder),
    path('book',views.book),
    path('clothes',views.clothes),
    path('electric',views.elec),
    path('cart/add/<int:pro_id>',views.addToCart),
    path('cart/delete/<int:item_id>',views.deleteInCart),
    path('cart/edit/<int:item_id>',views.editForm),
    path('cart/edit',views.editCart),
    path('comment',views.addComment),
    path('like/<int:pro_id>',views.like),
    path('dislike/<int:pro_id>',views.dislike)
]
