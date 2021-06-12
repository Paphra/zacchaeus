from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import date, datetime

from sales.models import Sale, SalesReturn
from purchases.models import Purchase, PurchasesReturn
from expenses.models import Expense
from persons.models import Person

def getMonthText(monthInt):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Nov', 'Dec']
    return months[monthInt - 1]

def graphWork(request, model, sDate, eDate, months):
    total = 0
    lItems = []
    for month in months:
        lItems.append(0)

    items = model.objects.filter(
        person=request.user.person,
        date_made__range=[sDate+'T00:00:00+0300', eDate+'T23:59:59+0300']
    )

    for item in items:
        total += item.amount
        item_month = item.date_made.month
        month_text = getMonthText(item_month)
        
        for month in months:
            monthIndex = months.index(month)
            if month == month_text:
                lItems[monthIndex] = lItems[monthIndex] + item.amount
    
    return {
        'list': lItems,
        'total': total
    }

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

    if request.user.person:
        person = request.user.person
    else:
        person = Person()
        person.name=request.user.username
        person.owner=request.user
        person.save()

        request.user.person = person
        request.user.save()

    months = []
    for i in range(sM, eM + 1):
        months.append(getMonthText(i))
    
    # get working
    wSales = graphWork(request, Sale, sDate, eDate, months)
    wSalesReturns = graphWork(request, SalesReturn, sDate, eDate, months)
    wPurchases = graphWork(request, Purchase, sDate, eDate, months)
    wPurchasesReturns = graphWork(request, PurchasesReturn, sDate, eDate, months)
    wExpenses = graphWork(request, Expense, sDate, eDate, months)
    

    args = {
        'nav': 'charts',
        'months': months,
        
        'sales': wSales['list'],
        'total_sales': wSales['total'],
        
        'sales_returns': wSalesReturns['list'],
        'total_sales_returns': wSalesReturns['total'],
        
        'purchases': wPurchases['list'],
        'total_purchases': wPurchases['total'],
        
        'purchases_returns': wPurchasesReturns['list'],
        'total_purchases_returns': wPurchasesReturns['total'],
        
        'expenses': wExpenses['list'],
        'total_expenses': wExpenses['total'],

        'startDate': sDate,
        'endDate': eDate,
        'range': sDate + ' - ' + eDate,
    }

    return render(request, 'charts/index.html', args)
