from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import date
from django.contrib import messages

from .models import Sale
from .forms import SaleForm

@login_required
def index(request):
    today = date.today()
    sDate = str(today.year) + '-' + str(today.month) + '-01'
    eDate = str(today.year) + '-' + str(today.month) + '-' + str(today.day)
    if request.GET.get('range'):
        dates = request.GET.get('range').split(sep=" - ")
        sDate = dates[0]
        eDate = dates[1]
    sales = Sale.objects.filter(
        person=request.user.person,
        date_made__range=[sDate+'T00:00:00+0300', eDate +'T23:59:59+0300']
    )
    
    args = {
        'nav': 'sales',
        'sales': sales,
        'startDate': sDate,
        'endDate': eDate,
        'range': sDate + ' - ' + eDate
    }

    return render(request, 'sales/index.html', args)

@login_required
def add(request):
    if request.method == 'POST':
        form = SaleForm(request.POST, request.FILES)
        if form.is_valid():
            sale = form.save()

            messages.add_message(
                request, messages.SUCCESS, 
                'Successfully Added Sale! Particulars: ' + sale.particulars
            )
            return redirect('sales')

    else:
        form = SaleForm()
    
    args = {
        'nav': 'sales',
        'form': form,
    }

    return render(request, 'sales/add.html', args)

def change(request, pk):
    sale = get_object_or_404(Sale, pk=pk)

    if request.method == 'POST':
        form = SaleForm(request.POST, request.FILES, instance=sale)
        if form.is_valid():
            try:
                if sale.receipt and request.FILES['receipt']:
                    default_storage.delete(sale.receipt.path)
                if sale.document and request.FILES['document']:
                    default_storage.delete(sale.document.path)
            except:  
                pass

            sale = form.save()
            messages.add_message(
                request, messages.SUCCESS, 
                'Successfully Updated Sale! Particulars: ' + sale.particulars
            ) 
            return redirect(sale.get_absolute_url())
    else:
        form = SaleForm(instance=sale)

    args = {
        'nav': 'sales',
        'sale': sale,
        'form': form
    }

    return render(request, 'sales/change.html', args)

@login_required
def detail(request, pk):
    sale = get_object_or_404(Sale, pk=pk)

    args = {
        'nav': 'sales',
        'sale': sale
    }
    return render(request, 'sales/details.html', args)

@login_required
def delete(request, pk):
    sale = get_object_or_404(Sale, pk=pk)
    if sale.receipt:
        sale.receipt.delete()
    if sale.document:
        sale.document.delete()
    sale.delete()
    messages.add_message(
        request, messages.INFO, 
        'Successfully Deleted Sale! Particulars: ' + sale.particulars
    )
    return redirect('sales')
