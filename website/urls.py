from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='web-Home'),
    path('store/', views.store, name='web-store'),
    path('cart/', views.cart, name='web-cart'),
    path('checkout/', views.checkout, name='web-checkout'),
    path('update_item/', views.updateItem, name='web-update_item')

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)