from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import date
from django.contrib import messages

from .models import ClosingStock
from .forms import ClosingForm

@login_required
def index(request):
    today = date.today()
    sDate = str(today.year) + '-01-01'
    eDate = str(today.year) + '-' + str(today.month) + '-' + str(today.day)
    if request.GET.get('range'):
        dates = request.GET.get('range').split(sep=" - ")
        sDate = dates[0]
        eDate = dates[1]
    closing_stocks = ClosingStock.objects.filter(
        person=request.user.person,
        date_made__range=[sDate+'T00:00:00+0300', eDate +'T23:59:59+0300']
    )
    
    args = {
        'nav': 'stock',
        'closing_stocks': closing_stocks,
        'startDate': sDate,
        'endDate': eDate,
        'range': sDate + ' - ' + eDate
    }

    return render(request, 'stocks/closing/index.html', args)

@login_required
def add(request):
    if request.method == 'POST':
        form = ClosingForm(request.POST, request.FILES)
        if form.is_valid():
            closing = form.save()

            messages.add_message(
                request, messages.SUCCESS, 
                'Successfully Added Sales Return! Particulars: ' + closing.particulars
            )
            return redirect('closing_stocks')

    else:
        form = ClosingForm()
    
    args = {
        'nav': 'stock',
        'form': form,
    }

    return render(request, 'stocks/closing/add.html', args)

def change(request, pk):
    closing_stock = get_object_or_404(ClosingStock, pk=pk)

    if request.method == 'POST':
        form = ClosingForm(request.POST, request.FILES, instance=closing_stock)
        if form.is_valid():
            try:
                if closing.receipt and request.FILES['receipt']:
                    default_storage.delete(closing.receipt.path)
                if closing.document and request.FILES['document']:
                    default_storage.delete(closing.document.path)
            except:  
                pass

            closing_stock = form.save()
            messages.add_message(
                request, messages.SUCCESS, 
                'Successfully Updated Sales Return! Particulars: ' + closing_stock.particulars
            ) 
            return redirect(closing_stock.get_absolute_url())
    else:
        form = ClosingForm(instance=closing_stock)

    args = {
        'nav': 'stock',
        'closing_stock': closing_stock,
        'form': form
    }

    return render(request, 'stocks/closing/change.html', args)

@login_required
def detail(request, pk):
    closing_stock = get_object_or_404(ClosingStock, pk=pk)

    args = {
        'nav': 'stock',
        'closing_stock': closing_stock
    }
    return render(request, 'stocks/closing/details.html', args)

@login_required
def delete(request, pk):
    closing = get_object_or_404(ClosingStock, pk=pk)
    if closing.receipt:
        closing.receipt.delete()
    if closing.document:
        closing.document.delete()
    closing.delete()
    messages.add_message(
        request, messages.INFO, 
        'Successfully Deleted Sales Return! Particulars: ' + closing.particulars
    )
    return redirect('closing_stocks')
