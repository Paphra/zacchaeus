from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import date
from django.contrib import messages

from .models import PurchasesReturn
from .forms import PurchasesReturnForm

@login_required
def index(request):
    today = date.today()
    sDate = str(today.year) + '-' + str(today.month) + '-01'
    eDate = str(today.year) + '-' + str(today.month) + '-' + str(today.day)
    if request.GET.get('range'):
        dates = request.GET.get('range').split(sep=" - ")
        sDate = dates[0]
        eDate = dates[1]
    purchases_returns = PurchasesReturn.objects.filter(
        person=request.user.person,
        date_made__range=[sDate+'T00:00:00+0300', eDate +'T23:59:59+0300']
    )
    
    args = {
        'nav': 'purchases_returns',
        'purchases_returns': purchases_returns,
        'startDate': sDate,
        'endDate': eDate,
        'range': sDate + ' - ' + eDate
    }

    return render(request, 'purchases/returns/index.html', args)

@login_required
def add(request):
    if request.method == 'POST':
        form = PurchasesReturnForm(request.POST, request.FILES)
        if form.is_valid():
            purchases_return = form.save()

            messages.add_message(
                request, messages.SUCCESS, 
                'Successfully Added Purchases Return! Particulars: ' + purchases_return.particulars
            )
            return redirect('purchases_returns')

    else:
        form = PurchasesReturnForm()
    
    args = {
        'nav': 'purchases_returns',
        'form': form,
    }

    return render(request, 'purchases/returns/add.html', args)

def change(request, pk):
    purchases_return = get_object_or_404(PurchasesReturn, pk=pk)

    if request.method == 'POST':
        form = PurchasesReturnForm(request.POST, request.FILES, instance=purchases_return)
        if form.is_valid():
            try:
                if purchases_return.receipt and request.FILES['receipt']:
                    default_storage.delete(purchases_return.receipt.path)
                if purchases_return.document and request.FILES['document']:
                    default_storage.delete(purchases_return.document.path)
            except:  
                pass

            purchases_return = form.save()
            messages.add_message(
                request, messages.SUCCESS, 
                'Successfully Updated Purchases Return! Particulars: ' + purchases_return.particulars
            ) 
            return redirect(purchases_return.get_absolute_url())
    else:
        form = PurchasesReturnForm(instance=purchases_return)

    args = {
        'nav': 'purchases_returns',
        'purchases_return': purchases_return,
        'form': form
    }

    return render(request, 'purchases/returns/change.html', args)

@login_required
def detail(request, pk):
    purchases_return = get_object_or_404(PurchasesReturn, pk=pk)

    args = {
        'nav': 'purchases_returns',
        'purchases_return': purchases_return
    }
    return render(request, 'purchases/returns/details.html', args)

@login_required
def delete(request, pk):
    purchases_return = get_object_or_404(PurchasesReturn, pk=pk)
    if purchases_return.receipt:
        purchases_return.receipt.delete()
    if purchases_return.document:
        purchases_return.document.delete()
    purchases_return.delete()
    messages.add_message(
        request, messages.INFO, 
        'Successfully Deleted Purchases Return! Particulars: ' + purchases_return.particulars
    )
    return redirect('purchases_returns')
