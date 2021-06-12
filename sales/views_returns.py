from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import date
from django.contrib import messages

from .models import SalesReturn
from .forms import SalesReturnForm

@login_required
def index(request):
    today = date.today()
    sDate = str(today.year) + '-' + str(today.month) + '-01'
    eDate = str(today.year) + '-' + str(today.month) + '-' + str(today.day)
    if request.GET.get('range'):
        dates = request.GET.get('range').split(sep=" - ")
        sDate = dates[0]
        eDate = dates[1]
    sales_returns = SalesReturn.objects.filter(
        person=request.user.person,
        date_made__range=[sDate+'T00:00:00+0300', eDate +'T23:59:59+0300']
    )
    
    args = {
        'nav': 'sales_returns',
        'sales_returns': sales_returns,
        'startDate': sDate,
        'endDate': eDate,
        'range': sDate + ' - ' + eDate
    }

    return render(request, 'sales/returns/index.html', args)

@login_required
def add(request):
    if request.method == 'POST':
        form = SalesReturnForm(request.POST, request.FILES)
        if form.is_valid():
            sales_return = form.save()

            messages.add_message(
                request, messages.SUCCESS, 
                'Successfully Added Sales Return! Particulars: ' + sales_return.particulars
            )
            return redirect('sales_returns')

    else:
        form = SalesReturnForm()
    
    args = {
        'nav': 'sales_returns',
        'form': form,
    }

    return render(request, 'sales/returns/add.html', args)

def change(request, pk):
    sales_return = get_object_or_404(SalesReturn, pk=pk)

    if request.method == 'POST':
        form = SalesReturnForm(request.POST, request.FILES, instance=sales_return)
        if form.is_valid():
            try:
                if sales_return.receipt and request.FILES['receipt']:
                    default_storage.delete(sales_return.receipt.path)
                if sales_return.document and request.FILES['document']:
                    default_storage.delete(sales_return.document.path)
            except:  
                pass

            sales_return = form.save()
            messages.add_message(
                request, messages.SUCCESS, 
                'Successfully Updated Sales Return! Particulars: ' + sales_return.particulars
            ) 
            return redirect(sales_return.get_absolute_url())
    else:
        form = SalesReturnForm(instance=sales_return)

    args = {
        'nav': 'sales_returns',
        'sales_return': sales_return,
        'form': form
    }

    return render(request, 'sales/returns/change.html', args)

@login_required
def detail(request, pk):
    sales_return = get_object_or_404(SalesReturn, pk=pk)

    args = {
        'nav': 'sales_returns',
        'sales_return': sales_return
    }
    return render(request, 'sales/returns/details.html', args)

@login_required
def delete(request, pk):
    sales_return = get_object_or_404(SalesReturn, pk=pk)
    if sales_return.receipt:
        sales_return.receipt.delete()
    if sales_return.document:
        sales_return.document.delete()
    sales_return.delete()
    messages.add_message(
        request, messages.INFO, 
        'Successfully Deleted Sales Return! Particulars: ' + sales_return.particulars
    )
    return redirect('sales_returns')
