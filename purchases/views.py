from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import date
from django.contrib import messages

from purchases.models import Purchase
from purchases.forms import PurchaseForm

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
        business=request.user.business,
        date_made__gte=sDate,
        date_made__lte=eDate + ' 23:59:59'
    )
    
    args = {
        'purchases': purchases,
        'startDate': sDate,
        'endDate': eDate,
        'range': sDate + ' - ' + eDate
    }

    return render(request, 'purchases/index.html', args)

@login_required
def purchase_add(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            purchase = form.save()

            messages.add_message(
                request, messages.SUCCESS, 
                'Successfully Added Purchase! Particulars: ' + purchase.particulars
            )
            return redirect('purchases')

    else:
        form = PurchaseForm()

    return render(request, 'purchases/add.html')

def purchase_change(request, pk):
    purchase = get_object_or_404(Purchase, pk=pk)

    if request.method == 'POST':
        form = PurchaseForm(request.POST, instance=purchase)
        if form.is_valid():
            purchase = form.save()

            messages.add_message(
                request, messages.SUCCESS, 
                'Successfully Updated Purchase! Particulars: ' + purchase.particulars
            )
            return redirect('purchases')
    else:
        form = PurchaseForm(instance=purchase)
        
    args = {
        'purchase': purchase,
        'form': form
    }
    return render(request, 'purchases/change.html', args)

@login_required
def purchase_detail(request, pk):

    return render(request, 'purchases/details.html')

@login_required
def purchase_delete(request, pk):
    purchase = get_object_or_404(Purchase, pk=pk)
    purchase.delete()
    messages.add_message(
        request, messages.INFO, 
        'Successfully Deleted Purchase! Particulars: ' + purchase.particulars
    )
    return redirect('purchases')
