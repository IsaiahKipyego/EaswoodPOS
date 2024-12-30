# custom_admin/urls.py

from django.urls import path
from . import views

app_name = 'custom_admin'

urlpatterns = [
    path('', views.index, name='index'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/add/', views.category_add, name='category_add'),
    path('categories/<int:pk>/edit/', views.category_edit, name='category_edit'),
    path('categories/<int:pk>/delete/', views.category_delete, name='category_delete'),
    path('products/', views.product_list, name='product_list'),
    path('products/add/', views.product_add, name='product_add'),  # Add this line
    path('products/<int:pk>/edit/', views.product_edit, name='product_edit'),  # Add this line
    path('products/<int:pk>/delete/', views.product_delete, name='product_delete'),  # Add this line
    path('transactions/', views.transaction_list, name='transaction_list'),
]