from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import date
from django.contrib import messages

from .models import OpeningStock
from .forms import OpeningForm

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
    
    args = {
        'nav': 'stock',
        'opening_stocks': opening_stocks,
        'startDate': sDate,
        'endDate': eDate,
        'range': sDate + ' - ' + eDate
    }

    return render(request, 'stocks/opening/index.html', args)

@login_required
def add(request):
    if request.method == 'POST':
        form = OpeningForm(request.POST, request.FILES)
        if form.is_valid():
            opening = form.save()

            messages.add_message(
                request, messages.SUCCESS, 
                'Successfully Added Sales Return! Particulars: ' + opening.particulars
            )
            return redirect('opening_stocks')

    else:
        form = OpeningForm()
    
    args = {
        'nav': 'stock',
        'form': form,
    }

    return render(request, 'stocks/opening/add.html', args)

def change(request, pk):
    opening_stock = get_object_or_404(OpeningStock, pk=pk)

    if request.method == 'POST':
        form = OpeningForm(request.POST, request.FILES, instance=opening_stock)
        if form.is_valid():
            try:
                if opening.receipt and request.FILES['receipt']:
                    default_storage.delete(opening.receipt.path)
                if opening.document and request.FILES['document']:
                    default_storage.delete(opening.document.path)
            except:  
                pass

            opening = form.save()
            messages.add_message(
                request, messages.SUCCESS, 
                'Successfully Updated Sales Return! Particulars: ' + opening.particulars
            ) 
            return redirect(opening.get_absolute_url())
    else:
        form = OpeningForm(instance=opening_stock)

    args = {
        'nav': 'stock',
        'opening_stock': opening_stock,
        'form': form
    }

    return render(request, 'stocks/opening/change.html', args)

@login_required
def detail(request, pk):
    opening_stock = get_object_or_404(OpeningStock, pk=pk)

    args = {
        'nav': 'stock',
        'opening_stock': opening_stock
    }
    return render(request, 'stocks/opening/details.html', args)

@login_required
def delete(request, pk):
    opening = get_object_or_404(OpeningStock, pk=pk)
    if opening.receipt:
        opening.receipt.delete()
    if opening.document:
        opening.document.delete()
    opening.delete()
    messages.add_message(
        request, messages.INFO, 
        'Successfully Deleted Sales Return! Particulars: ' + opening.particulars
    )
    return redirect('opening_stocks')
