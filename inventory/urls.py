# inventory/urls.py

from django.urls import path
from . import views  # Import the views module from the current directory

urlpatterns = [
    path('home/', views.home, name='home'),  # Define the URL pattern for the home view
    path('products/', views.product_list, name='product_list'),  # Define the URL pattern for the product list view
    path('add_stock/', views.add_stock, name='add_stock'),  # Define the URL pattern for the add stock view
    path('make_sale/', views.make_sale, name='make_sale'),  # Define the URL pattern for the make sale view
    path('add_category/', views.add_category, name='add_category'),  # Define the URL pattern for the add category view
    path('purchase_order/', views.purchase_order, name='purchase_order'),  # Define the URL pattern for the purchase order view
    path('invoice/', views.invoice, name='invoice'),  # Define the URL pattern for the invoice view
]