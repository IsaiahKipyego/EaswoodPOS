from django.urls import path
from . import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
  path('products/', views.product_list, name='product_list'),
    path('create_product/', views.create_product, name='create_product'),
    path('add_stock/', views.add_stock, name='add_stock'),  # Example URL, ensure you have this view
    path('make_sale/', views.make_sale, name='make_sale'),  # Example URL, ensure you have this view
    path('add_category/', views.add_category, name='add_category'),  # Example URL, ensure you have this view
    path('sales_report/<str:period>/', views.sales_report, name='sales_report'),
    path('custom_sales_report/', views.custom_sales_report, name='custom_sales_report'),
    path('sales_report/<str:period>/', views.sales_report, name='sales_report'),
    path('custom_sales_report/', views.custom_sales_report, name='custom_sales_report'),
    path('purchase_order/', views.purchase_order, name='purchase_order'),
    path('invoice/', views.invoice, name='invoice'),
    path('create_product/', views.create_product, name='create_product'),
    path('edit_product/<int:pk>/', views.edit_product, name='edit_product'),
    path('sales_report/<str:period>/', views.sales_report, name='sales_report'),
    path('custom_sales_report/', views.custom_sales_report, name='custom_sales_report'),
    path('create_product/', views.create_product, name='create_product'),
    path('edit_product/<int:pk>/', views.edit_product, name='edit_product'),
    path('sales_report/<str:period>/', views.sales_report, name='sales_report'),
    path('custom_sales_report/', views.custom_sales_report, name='custom_sales_report'),
    path('admin/', admin.site.urls),
    path('inventory/', include('inventory.urls')),
]