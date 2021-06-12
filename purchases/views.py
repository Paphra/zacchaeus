from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import date
from django.contrib import messages

from .models import Purchase
from .forms import PurchaseForm

@login_required
def index(request):
    today = date.today()
    sDate = str(today.year) + '-' + str(today.month) + '-01'
    eDate = str(today.year) + '-' + str(today.month) + '-' + str(today.day)
    if request.GET.get('range'):
        dates = request.GET.get('range').split(sep=" - ")
        sDate = dates[0]
        eDate = dates[1]
    purchases = Purchase.objects.filter(
        person=request.user.person,
        date_made__range=[sDate+'T00:00:00+0300', eDate +'T23:59:59+0300']
    )
    
    args = {
        'nav': 'purchases',
        'purchases': purchases,
        'startDate': sDate,
        'endDate': eDate,
        'range': sDate + ' - ' + eDate
    }

    return render(request, 'purchases/index.html', args)

@login_required
def add(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST, request.FILES)
        if form.is_valid():
            purchase = form.save()

            messages.add_message(
                request, messages.SUCCESS, 
                'Successfully Added Purchase! Particulars: ' + purchase.particulars
            )
            return redirect('purchases')

    else:
        form = PurchaseForm()
    
    args = {
        'nav': 'purchases',
        'form': form,
    }

    return render(request, 'purchases/add.html', args)

def change(request, pk):
    purchase = get_object_or_404(Purchase, pk=pk)

    if request.method == 'POST':
        form = PurchaseForm(request.POST, request.FILES, instance=purchase)
        if form.is_valid():
            try:
                if purchase.receipt and request.FILES['receipt']:
                    default_storage.delete(purchase.receipt.path)
                if purchase.document and request.FILES['document']:
                    default_storage.delete(purchase.document.path)
            except:  
                pass

            purchase = form.save()
            messages.add_message(
                request, messages.SUCCESS, 
                'Successfully Updated Purchase! Particulars: ' + purchase.particulars
            ) 
            return redirect(purchase.get_absolute_url())
    else:
        form = PurchaseForm(instance=purchase)

    args = {
        'nav': 'purchases',
        'purchase': purchase,
        'form': form
    }

    return render(request, 'purchases/change.html', args)

@login_required
def detail(request, pk):
    purchase = get_object_or_404(Purchase, pk=pk)

    args = {
        'nav': 'purchases',
        'purchase': purchase
    }
    return render(request, 'purchases/details.html', args)

@login_required
def delete(request, pk):
    purchase = get_object_or_404(Purchase, pk=pk)
    if purchase.receipt:
        purchase.receipt.delete()
    if purchase.document:
        purchase.document.delete()
    purchase.delete()
    messages.add_message(
        request, messages.INFO, 
        'Successfully Deleted Purchase! Particulars: ' + purchase.particulars
    )
    return redirect('purchases')
