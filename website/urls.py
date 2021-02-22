from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='web-Home'),
    path('about/', views.about, name='web-About'),

]