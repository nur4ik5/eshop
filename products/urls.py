from django.urls import path
from products import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('detail', views.product_detail, name='product_detail'),
    path('create', views.create_product, name = 'create_product'),
]