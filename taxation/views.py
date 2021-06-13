from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .tax_calculator import calculator
from .models import IncomeTaxRange

def endDay(month, day):
    if day == '01':
        if month in ['01', '03', '05', '07', '08', '10', '12']:
            return '31'
        elif month == '02':
            return '28'
        else:
            return '30'
    else:
        return str(int(day) - 1)

def endMonth(sMonth):
    if sMonth == 1:
        return 12
    else:
        return sMonth - 1

@login_required
def index(request):
    today = date.today()
    cMonth = today.month

    sYear = today.year
    sMonth = 7
    sDay = '01'
    
    eMonth = '06'
    eDay = '30'

    if cMonth < sMonth:
        sYear -= 1
    
    if request.GET.get('startDate'):
        startDate = request.GET.get('startDate')
        spd = startDate.split(sep='-')
        try:
            sYear = int(spd[0])
            sMonth = int(spd[1])
            sDay = spd[2]

            eMonth = str(endMonth(sMonth))
            eDay = endDay(eMonth, sDay)

            if sMonth < 7:
                sYear -= 1

        except:
            pass

    
    eYear = sYear + 1
                
        
    sDate = str(sYear) + '-' + str(sMonth) + '-' + sDay
    eDate = str(eYear) + '-' + eMonth + '-' + eDay

    person = request.user.person

    income_tax_ranges = IncomeTaxRange.objects.filter(is_active=True, person_type=person.person_type)
    calc = calculator(person, income_tax_ranges, sDate, eDate)

    args = {
        'nav': 'taxation',
        'startDate': sDate,
        'range': sDate + ' to ' + eDate,
        'income_tax_ranges': income_tax_ranges,

        **calc['totals'],
        **calc,

    }

    return render(request, 'taxation/index.html', args)

def pay_tax(request):
    pass