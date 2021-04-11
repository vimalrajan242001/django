from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='web-Home'),
    path('about/', views.about, name='web-About'),
    path('store/', views.store, name='web-store'),
    path('cart/', views.cart, name='web-cart'),
    path('checkout/', views.checkout, name='web-checkout'),

]
