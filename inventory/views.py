from django.shortcuts import render, redirect
from .forms import ProductForm, TransactionForm
from .models import Product, Transaction
from datetime import datetime, timedelta
from django.db.models import Sum

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redirect to a list view or another page after saving
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})

def edit_product(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redirect to a list view or another page after saving
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_form.html', {'form': form})

def sales_report(request, period='daily'):
    if period == 'daily':
        start_date = datetime.now().date()
    elif period == 'weekly':
        start_date = datetime.now().date() - timedelta(days=7)
    elif period == 'monthly':
        start_date = datetime.now().date() - timedelta(days=30)
    elif period == 'yearly':
        start_date = datetime.now().date() - timedelta(days=365)
    else:
        start_date = None

    transactions = Transaction.objects.filter(
        date__gte=start_date,
        transaction_type='sale'
    ).values('product__name', 'product__vat_rate', 'product__vat_included').annotate(
        total_quantity=Sum('quantity'),
        total_sales=Sum('selling_price'),
        total_vat=Sum('selling_price') * Sum('quantity') * Sum('product__vat_rate') / 100
    ).order_by('-total_quantity')

    total_vat = transactions.aggregate(total_vat=Sum('total_vat'))['total_vat'] or 0

    context = {
        'transactions': transactions,
        'period': period,
        'total_vat': total_vat,
    }
    return render(request, 'sales_report.html', context)

def custom_sales_report(request):
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        transactions = Transaction.objects.filter(
            date__range=[start_date, end_date],
            transaction_type='sale'
        ).values('product__name', 'product__vat_rate', 'product__vat_included').annotate(
            total_quantity=Sum('quantity'),
            total_sales=Sum('selling_price'),
            total_vat=Sum('selling_price') * Sum('quantity') * Sum('product__vat_rate') / 100
        ).order_by('-total_quantity')

        total_vat = transactions.aggregate(total_vat=Sum('total_vat'))['total_vat'] or 0

        context = {
            'transactions': transactions,
            'start_date': start_date,
            'end_date': end_date,
            'total_vat': total_vat,
        }
        return render(request, 'sales_report.html', context)
    return render(request, 'custom_sales_report.html')