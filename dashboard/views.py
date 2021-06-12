from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import date, datetime

from sales.models import Sale
from purchases.models import Purchase
from expenses.models import Expense
from incomes.models import Income
from persons.models import Person

from statements.calculations import totals

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

    person = request.user.person
    # person.name = request.user.username
    # person.save()

    months = []
    for i in range(sM, eM + 1):
        months.append(getMonthText(i))
    
    # get working
    wSales = graphWork(request, Sale, sDate, eDate, months)
    wPurchases = graphWork(request, Purchase, sDate, eDate, months)
    wExpenses = graphWork(request, Expense, sDate, eDate, months)
    wIncomes = graphWork(request, Income, sDate, eDate, months)

    totos = totals(person, sDate, eDate)

    args = {
        'nav': 'dashboard',
        'months': months,
        'sales': wSales['list'],
        'total_sales': wSales['total'],

        'purchases': wPurchases['list'],
        'total_purchases': wPurchases['total'],

        'expenses': wExpenses['list'],
        'total_expenses': wExpenses['total'],

        'total_incomes': totos['incomes'],
        'incomes': wIncomes['list'],
        'closing_stock': totos['closing_stock'],
        'cost_of_sales': totos['cost_of_sales'],
        'gross_profit': totos['gross_profit'],
        'net_profit': totos['net_profit'],

        'startDate': sDate,
        'endDate': eDate,
        'range': sDate + ' - ' + eDate,
    }

    return render(request, 'dashboard/index.html', args)

def profile(request):

    args = {
        'nav': 'profile'
    }

    return render(request, 'profile.html', args)

def profile_update(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.phone = request.POST['phone']

        user.save()

        messages.add_message(
            request, messages.SUCCESS, 
            'Successfully Updated User Profile Information!'
        )
    return redirect('profile')

    args = {
        'nav': 'profile'
    }

    return render(request, 'profile.html', args)
    