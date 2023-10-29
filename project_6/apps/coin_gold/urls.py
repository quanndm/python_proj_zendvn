from django.urls import path
from . import views

urlpatterns = [
    path('coin/', views.list_coin, name='list_coin'),
    path('gold/', views.list_gold, name='list_gold'),
]