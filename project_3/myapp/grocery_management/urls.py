from django.urls import path
from . import views

urlpatterns = [
    path('products/create/', views.create_product, name='create_product'),
    path('products/list/', views.list_products, name='list_products'),
    path('products/update/<int:product_id>/', views.update_product, name='update_product'),
    path('products/delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('products/sell/<int:product_id>/', views.sell_product, name='sell_product'),
]