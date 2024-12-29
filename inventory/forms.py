from django import forms
from .models import Product, Transaction, Category

class ProductForm(forms.ModelForm):
    vat_included = forms.BooleanField(required=False, initial=True, label="VAT Included")
    vat_rate = forms.DecimalField(max_digits=5, decimal_places=2, initial=16.00, label="VAT Rate")
    pos_listing = forms.BooleanField(required=False, initial=False, label="List on POS")

    class Meta:
        model = Product
        fields = ['name', 'description', 'buying_price', 'selling_price', 'stock', 'category', 'vat_included', 'vat_rate', 'pos_listing']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
        return super().save(commit=commit)

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['product', 'quantity', 'transaction_type', 'selling_price']
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'transaction_type': forms.Select(attrs={'class': 'form-control'}),
            'selling_price': forms.NumberInput(attrs={'class': 'form-control'}),
        }