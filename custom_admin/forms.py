# custom_admin/forms.py

from django import forms
from inventory.models import Category, Product, Transaction

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'buying_price', 'selling_price', 'stock', 'barcode', 'category', 'vat_included', 'vat_rate', 'pos_listing']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['product', 'quantity', 'transaction_type', 'selling_price']  # Exclude the 'date' field