# inventory/admin.py

from django.contrib import admin
from .models import Category, Product, Transaction  # Ensure correct models are imported

# Customizing the Category admin interface
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Customizing the Product admin interface
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'buying_price', 'selling_price', 'stock', 'category', 'vat_included', 'pos_listing')
    search_fields = ('name', 'barcode')
    list_filter = ('category', 'vat_included', 'pos_listing')
    readonly_fields = ('barcode',)

    def mark_as_out_of_stock(self, request, queryset):
        queryset.update(stock=0)
        self.message_user(request, "Selected products marked as out of stock.")
    mark_as_out_of_stock.short_description = "Mark selected products as out of stock"

    actions = [mark_as_out_of_stock]

# Customizing the Transaction admin interface
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'transaction_type', 'selling_price', 'date')
    list_filter = ('transaction_type', 'date')
    date_hierarchy = 'date'

# Registering the models with their custom admin interfaces
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Transaction, TransactionAdmin)