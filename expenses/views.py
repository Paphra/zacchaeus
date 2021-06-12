from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import date
from django.contrib import messages

from .models import Expense
from .forms import ExpenseForm

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
        person=request.user.person,
        date_made__range=[sDate+'T00:00:00+0300', eDate +'T23:59:59+0300']
    )
    
    args = {
        'nav': 'expenses',
        'expenses': expenses,
        'startDate': sDate,
        'endDate': eDate,
        'range': sDate + ' - ' + eDate
    }

    return render(request, 'expenses/index.html', args)

@login_required
def add(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST, request.FILES)
        if form.is_valid():
            expense = form.save()

            messages.add_message(
                request, messages.SUCCESS, 
                'Successfully Added Expense! Particulars: ' + expense.particulars
            )
            return redirect('expenses')

    else:
        form = ExpenseForm()
    
    args = {
        'nav': 'expenses',
        'form': form,
    }

    return render(request, 'expenses/add.html', args)

def change(request, pk):
    expense = get_object_or_404(Expense, pk=pk)

    if request.method == 'POST':
        form = ExpenseForm(request.POST, request.FILES, instance=expense)
        if form.is_valid():
            try:
                if expense.receipt and request.FILES['receipt']:
                    default_storage.delete(expense.receipt.path)
                if expense.document and request.FILES['document']:
                    default_storage.delete(expense.document.path)
            except:  
                pass

            expense = form.save()
            messages.add_message(
                request, messages.SUCCESS, 
                'Successfully Updated Expense! Particulars: ' + expense.particulars
            ) 
            return redirect(expense.get_absolute_url())
    else:
        form = ExpenseForm(instance=expense)

    args = {
        'nav': 'expenses',
        'expense': expense,
        'form': form
    }

    return render(request, 'expenses/change.html', args)

@login_required
def detail(request, pk):
    expense = get_object_or_404(Expense, pk=pk)

    args = {
        'nav': 'expenses',
        'expense': expense
    }
    return render(request, 'expenses/details.html', args)

@login_required
def delete(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if expense.receipt:
        expense.receipt.delete()
    if expense.document:
        expense.document.delete()
    expense.delete()
    messages.add_message(
        request, messages.INFO, 
        'Successfully Deleted Expense! Particulars: ' + expense.particulars
    )
    return redirect('expenses')
