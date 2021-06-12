from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from sales.models import Sale, SalesReturn
from purchases.models import Purchase, PurchasesReturn
from expenses.models import Depreciation, Expense
from incomes.models import Interest, Income
from assets.models import Debtor, Asset
from liabilities.models import Creditor, Liability
from stock.models import OpeningStock, ClosingStock

from .calculations import totals

@login_required
def index(request):
    today = date.today()
    sDate = str(today.year) + '-01-01'
    eDate = str(today.year) + '-' + str(today.month) + '-' + str(today.day)
    
    sM = 1
    eM = today.month

    if request.GET.get('range'):
        dates = request.GET.get('range').split(sep=" - ")
        sDate = dates[0]
        eDate = dates[1]
        sM = int(sDate.split('-')[1])
        eM = int(eDate.split('-')[1])

    person = request.user.person
    
    args = {
        'nav': 'statements',
        **totals(person, sDate, eDate),
        'startDate': sDate,
        'endDate': eDate,
        'range': sDate + ' - ' + eDate,
    }

    return render(request, 'statements/index.html', args)

@login_required
def income(request):
    today = date.today()
    sDate = str(today.year) + '-01-01'
    eDate = str(today.year) + '-' + str(today.month) + '-' + str(today.day)
    
    sM = 1
    eM = today.month

    if request.GET.get('range'):
        dates = request.GET.get('range').split(sep=" - ")
        sDate = dates[0]
        eDate = dates[1]
        sM = int(sDate.split('-')[1])
        eM = int(eDate.split('-')[1])

    person = request.user.person

    args = {
        'nav': 'income_statement',
        **totals(person, sDate, eDate),
        'startDate': sDate,
        'endDate': eDate,
        'range': sDate + ' - ' + eDate,
    }

    return render(request, 'statements/income.html', args)

@login_required
def balance(request):
    today = date.today()
    sDate = str(today.year) + '-01-01'
    eDate = str(today.year) + '-' + str(today.month) + '-' + str(today.day)
    
    sM = 1
    eM = today.month

    if request.GET.get('range'):
        dates = request.GET.get('range').split(sep=" - ")
        sDate = dates[0]
        eDate = dates[1]
        sM = int(sDate.split('-')[1])
        eM = int(eDate.split('-')[1])

    person = request.user.person
    
    args = {
        'nav': 'balance_sheet',
        **totals(person, sDate, eDate),
        'startDate': sDate,
        'endDate': eDate,
        'range': sDate + ' - ' + eDate,
    }

    return render(request, 'statements/balance.html', args)
