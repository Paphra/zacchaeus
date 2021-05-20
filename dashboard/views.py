from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import date

from sales.models import Sale
from purchases.models import Purchase
from expenses.models import Expense

def getMonthText(monthInt):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Nov', 'Dec']
    return months[monthInt - 1]

def graphWork(request, model, sDate, eDate, months):
    total = 0
    lItems = []
    for month in months:
        lItems.append(0)

    items = model.objects.filter(
        business=request.user.business,
        date_made__gte=sDate, date_made__lte=eDate + ' 23:59:59'
    )
    for item in items:
        total += item.amount
        item_month = item.date_made.month
        for month in months:
            monthIndex = months.index(month)
                
            if monthIndex + 1 == item_month:
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

    months = []
    for i in range(sM, eM + 1):
        months.append(getMonthText(i))
    
    # get working
    wSales = graphWork(request, Sale, sDate, eDate, months)
    wPurchases = graphWork(request, Purchase, sDate, eDate, months)
    wExpenses = graphWork(request, Expense, sDate, eDate, months)

    args = {
        'months': months,
        'sales': wSales['list'],
        'total_sales': wSales['total'],

        'purchases': wPurchases['list'],
        'total_purchases': wPurchases['total'],

        'expenses': wExpenses['list'],
        'total_expenses': wExpenses['total'],

        'startDate': sDate,
        'endDate': eDate,
        'range': sDate + ' - ' + eDate,
    }

    return render(request, 'dashboard/index.html', args)
