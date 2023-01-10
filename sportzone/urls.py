from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/',views.login_view,name='login'),
    path('store/',views.store,name="store"),
    
    path('customerRegister/', views.customerRegister, name='customerRegister'),
    path('adminDash/', views.adminDashboard, name='adminDash'),
    path('productsList/',views.productsList,name='productsList'),
    path('addproducts/',views.addproducts,name='addproducts'),
    path('orderdetail/',views.orderdetail,name='orderdetail'),
    path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),

]

