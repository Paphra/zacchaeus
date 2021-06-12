from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import date
from django.contrib import messages

from .models import PropertyIncome
from .forms import PropertyIncomeForm

@login_required
def index(request):
    today = date.today()
    sDate = str(today.year) + '-' + str(today.month) + '-01'
    eDate = str(today.year) + '-' + str(today.month) + '-' + str(today.day)
    if request.GET.get('range'):
        dates = request.GET.get('range').split(sep=" - ")
        sDate = dates[0]
        eDate = dates[1]
    property_incomes = PropertyIncome.objects.filter(
        person=request.user.person,
        date_made__range=[sDate+'T00:00:00+0300', eDate +'T23:59:59+0300']
    )
    
    args = {
        'nav': 'property_incomes',
        'property_incomes': property_incomes,
        'startDate': sDate,
        'endDate': eDate,
        'range': sDate + ' - ' + eDate
    }

    return render(request, 'incomes/property/index.html', args)

@login_required
def add(request):
    if request.method == 'POST':
        form = PropertyIncomeForm(request.POST, request.FILES)
        if form.is_valid():
            property_income = form.save()

            messages.add_message(
                request, messages.SUCCESS, 
                'Successfully Added PropertyIncome! Particulars: ' + property_income.particulars
            )
            return redirect('property_incomes')

    else:
        form = PropertyIncomeForm()
    
    args = {
        'nav': 'property_incomes',
        'form': form,
    }

    return render(request, 'incomes/property/add.html', args)

def change(request, pk):
    property_income = get_object_or_404(PropertyIncome, pk=pk)

    if request.method == 'POST':
        form = PropertyIncomeForm(request.POST, request.FILES, instance=property_income)
        if form.is_valid():
            try:
                if property_income.receipt and request.FILES['receipt']:
                    default_storage.delete(property_income.receipt.path)
                if property_income.document and request.FILES['document']:
                    default_storage.delete(property_income.document.path)
            except:  
                pass

            property_income = form.save()
            messages.add_message(
                request, messages.SUCCESS, 
                'Successfully Updated PropertyIncome! Particulars: ' + property_income.particulars
            ) 
            return redirect(property_income.get_absolute_url())
    else:
        form = PropertyIncomeForm(instance=property_income)

    args = {
        'nav': 'property_incomes',
        'property_income': property_income,
        'form': form
    }

    return render(request, 'incomes/property/change.html', args)

@login_required
def detail(request, pk):
    property_income = get_object_or_404(PropertyIncome, pk=pk)

    args = {
        'nav': 'property_incomes',
        'property_income': property_income
    }
    return render(request, 'incomes/property/details.html', args)

@login_required
def delete(request, pk):
    property_income = get_object_or_404(PropertyIncome, pk=pk)
    if property_income.receipt:
        property_income.receipt.delete()
    if property_income.document:
        property_income.document.delete()
    property_income.delete()
    messages.add_message(
        request, messages.INFO, 
        'Successfully Deleted PropertyIncome! Particulars: ' + property_income.particulars
    )
    return redirect('property_incomes')
