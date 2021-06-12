from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .tax_calculator import calculator
from .models import IncomeTaxRange

def day(month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return '31'
    elif month == 2:
        return '28'
    else:
        return '30'

@login_required
def index(request):
    today = date.today()
    sDate = str(today.year) + '-07-01'
    eDate = str(today.year + 1) + '-06-30'
    if today.month < 7:
        sDate = str(today.year - 1) + '-07-01'
        eDate = str(today.year) + '-06-30'

    if request.GET.get('range'):
        dates = request.GET.get('range').split(sep=" - ")
        sDate = dates[0] + '-01'
        eDate = dates[1] + '-' + day(int(dates[1].split(sep='-')[1]))
    person = request.user.person

    income_tax_ranges = IncomeTaxRange.objects.filter(is_active=True, person_type=person.person_type)
    calc = calculator(person, income_tax_ranges, sDate, eDate)

    args = {
        'nav': 'taxation',
        'startDate': sDate,
        'endDate': eDate,
        'range': sDate + ' - ' + eDate,
        'income_tax_ranges': income_tax_ranges,

        **calc['totals'],
        **calc,

    }

    return render(request, 'taxation/index.html', args)

def pay_tax(request):
    pass