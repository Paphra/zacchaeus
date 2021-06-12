from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import date
from django.contrib import messages

from .models import Income
from .forms import IncomeForm

@login_required
def index(request):
    today = date.today()
    sDate = str(today.year) + '-' + str(today.month) + '-01'
    eDate = str(today.year) + '-' + str(today.month) + '-' + str(today.day)
    if request.GET.get('range'):
        dates = request.GET.get('range').split(sep=" - ")
        sDate = dates[0]
        eDate = dates[1]
    incomes = Income.objects.filter(
        person=request.user.person,
        date_made__range=[sDate+'T00:00:00+0300', eDate +'T23:59:59+0300']
    )
    
    args = {
        'nav': 'incomes',
        'incomes': incomes,
        'startDate': sDate,
        'endDate': eDate,
        'range': sDate + ' - ' + eDate
    }

    return render(request, 'incomes/index.html', args)

@login_required
def add(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST, request.FILES)
        if form.is_valid():
            income = form.save()

            messages.add_message(
                request, messages.SUCCESS, 
                'Successfully Added Income! Particulars: ' + income.particulars
            )
            return redirect('incomes')

    else:
        form = IncomeForm()
    
    args = {
        'nav': 'incomes',
        'form': form,
    }

    return render(request, 'incomes/add.html', args)

def change(request, pk):
    income = get_object_or_404(Income, pk=pk)

    if request.method == 'POST':
        form = IncomeForm(request.POST, request.FILES, instance=income)
        if form.is_valid():
            try:
                if income.receipt and request.FILES['receipt']:
                    default_storage.delete(income.receipt.path)
                if income.document and request.FILES['document']:
                    default_storage.delete(income.document.path)
            except:  
                pass

            income = form.save()
            messages.add_message(
                request, messages.SUCCESS, 
                'Successfully Updated Income! Particulars: ' + income.particulars
            ) 
            return redirect(income.get_absolute_url())
    else:
        form = IncomeForm(instance=income)

    args = {
        'nav': 'incomes',
        'income': income,
        'form': form
    }

    return render(request, 'incomes/change.html', args)

@login_required
def detail(request, pk):
    income = get_object_or_404(Income, pk=pk)

    args = {
        'nav': 'incomes',
        'income': income
    }
    return render(request, 'incomes/details.html', args)

@login_required
def delete(request, pk):
    income = get_object_or_404(Income, pk=pk)
    if income.receipt:
        income.receipt.delete()
    if income.document:
        income.document.delete()
    income.delete()
    messages.add_message(
        request, messages.INFO, 
        'Successfully Deleted Income! Particulars: ' + income.particulars
    )
    return redirect('incomes')
