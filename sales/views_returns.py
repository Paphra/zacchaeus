from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import date
from django.contrib import messages

from sales.models import SalesReturn
from sales.forms import SalesReturnForm

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
        business=request.user.business,
        date_made__gte=sDate,
        date_made__lte=eDate + ' 23:59:59'
    )
    
    args = {
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
                'Successfully Added SalesReturn! Particulars: ' + sales_return.particulars
            )
            return redirect('sales_returns')

    else:
        form = SalesReturnForm()

    return render(request, 'sales/returns/add.html')

def change(request, pk):
    sales_return = get_object_or_404(SalesReturn, pk=pk)

    if request.method == 'POST':
        form = SalesReturnForm(request.POST, instance=sales_return)
        if form.is_valid():
            sales_return = form.save()

            messages.add_message(
                request, messages.SUCCESS, 
                'Successfully Updated SalesReturn! Particulars: ' + sales_return.particulars
            )
            return redirect('sales_returns')
    else:
        form = SalesReturnForm(instance=sales_return)
        
    args = {
        'sales_return': sales_return,
        'form': form
    }
    return render(request, 'sales/returns/change.html', args)

@login_required
def detail(request, pk):
    sales_return = get_object_or_404(SalesReturn, pk=pk)

    args = {
        'sales_return': sales_return
    }
    return render(request, 'sales/returns/details.html', args)

@login_required
def delete(request, pk):
    sales_return = get_object_or_404(SalesReturn, pk=pk)
    sales_return.delete()
    messages.add_message(
        request, messages.INFO, 
        'Successfully Deleted SalesReturn! Particulars: ' + sales_return.particulars
    )
    return redirect('sales_returns')
