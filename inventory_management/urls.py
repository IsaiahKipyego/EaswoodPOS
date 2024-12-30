# inventory_management/urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/home/', permanent=True)),  # Redirect root URL to the home view
    path('', include('inventory.urls')),  # Include the URLs from the inventory app without additional prefix
    path('custom_admin/', include('custom_admin.urls')),
    path('accounts/', include('accounts.urls')),  # Include the accounts app URLs
]