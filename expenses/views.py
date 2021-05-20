from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import date
from django.contrib import messages

from expenses.models import Expense
from expenses.forms import ExpenseForm

@login_required
def index(request):
    today = date.today()
    sDate = str(today.year) + '-' + str(today.month) + '-01'
    eDate = str(today.year) + '-' + str(today.month) + '-' + str(today.day)
    if request.GET.get('range'):
        dates = request.GET.get('range').split(sep=" - ")
        sDate = dates[0]
        eDate = dates[1]
    expenses = Expense.objects.filter(
        business=request.user.business,
        date_made__gte=sDate,
        date_made__lte=eDate + ' 23:59:59'
    )
    
    args = {
        'expenses': expenses,
        'startDate': sDate,
        'endDate': eDate,
        'range': sDate + ' - ' + eDate
    }

    return render(request, 'expenses/index.html', args)

@login_required
def expense_add(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save()

            messages.add_message(
                request, messages.SUCCESS, 
                'Successfully Added Expense! Particulars: ' + expense.particulars
            )
            return redirect('expenses')

    else:
        form = ExpenseForm()

    return render(request, 'expenses/add.html')

def expense_change(request, pk):
    expense = get_object_or_404(Expense, pk=pk)

    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            expense = form.save()

            messages.add_message(
                request, messages.SUCCESS, 
                'Successfully Updated Expense! Particulars: ' + expense.particulars
            )
            return redirect('expenses')
    else:
        form = ExpenseForm(instance=expense)
        
    args = {
        'expense': expense,
        'form': form
    }
    return render(request, 'expenses/change.html', args)

@login_required
def expense_detail(request, pk):

    return render(request, 'expenses/details.html')

@login_required
def expense_delete(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    expense.delete()
    messages.add_message(
        request, messages.INFO, 
        'Successfully Deleted Expense! Particulars: ' + expense.particulars
    )
    return redirect('expenses')
