from django.urls import path

from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('register', views.register, name='register'),
    path('login', views.cust_login, name='login'),
    path('accounts/login/', views.cust_login),
    path('my-orders', views.myorders, name='myorders'),
    path('account', views.account, name='account'),
    path('logout', views.cust_logout, name='logout'),
    path('product/<prodName>', views.product, name='product'),
    path('update-cart/<int:prodId><action>', views.updateCart, name='updatecart'),
    path('delete-item/<int:itemId>', views.deleteitem, name='deleteitem'),
    path('delete-account', views.deleteaccount, name='deleteaccount'),
]