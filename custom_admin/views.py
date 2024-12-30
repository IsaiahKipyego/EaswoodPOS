# custom_admin/views.py

from django.shortcuts import render, get_object_or_404, redirect
from inventory.models import Category, Product, Transaction
from .forms import CategoryForm, ProductForm, TransactionForm

def index(request):
    return render(request, 'custom_admin/index.html')

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'custom_admin/category_list.html', {'categories': categories})

def category_add(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('custom_admin:category_list')
    else:
        form = CategoryForm()
    return render(request, 'custom_admin/category_form.html', {'form': form})

def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('custom_admin:category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'custom_admin/category_form.html', {'form': form})

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('custom_admin:category_list')
    return render(request, 'custom_admin/category_confirm_delete.html', {'category': category})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'custom_admin/product_list.html', {'products': products})

def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('custom_admin:product_list')
    else:
        form = ProductForm()
    return render(request, 'custom_admin/product_form.html', {'form': form})

def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('custom_admin:product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'custom_admin/product_form.html', {'form': form})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('custom_admin:product_list')
    return render(request, 'custom_admin/product_confirm_delete.html', {'product': product})

def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'custom_admin/transaction_list.html', {'transactions': transactions})