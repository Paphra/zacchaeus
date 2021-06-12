from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import OpeningStock, ClosingStock

@login_required
def index(request):
	today = date.today()
	sDate = str(today.year) + '-01-01'
	eDate = str(today.year) + '-' + str(today.month) + '-' + str(today.day)
	if request.GET.get('range'):
		dates = request.GET.get('range').split(sep=" - ")
		sDate = dates[0]
		eDate = dates[1]
	opening_stocks = OpeningStock.objects.filter(
		person=request.user.person,
		date_made__range=[sDate+'T00:00:00+0300', eDate +'T23:59:59+0300']
	)
	closing_stocks = ClosingStock.objects.filter(
		person=request.user.person,
		date_made__range=[sDate+'T00:00:00+0300', eDate +'T23:59:59+0300']
	)
    
	args = {
		'closing_stocks': closing_stocks,
		'opening_stocks': opening_stocks,
		'nav': 'stock',
        'startDate': sDate,
        'endDate': eDate,
        'range': sDate + ' - ' + eDate
	}

	return render(request, 'stocks/index.html', args)
