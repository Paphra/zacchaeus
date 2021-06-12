from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import date
from django.contrib import messages

from .models import Depreciation
from .forms import DepreciationForm

@login_required
def index(request):
    today = date.today()
    sDate = str(today.year) + '-' + str(today.month) + '-01'
    eDate = str(today.year) + '-' + str(today.month) + '-' + str(today.day)
    if request.GET.get('range'):
        dates = request.GET.get('range').split(sep=" - ")
        sDate = dates[0]
        eDate = dates[1]
    depreciations = Depreciation.objects.filter(
        person=request.user.person,
        date_made__range=[sDate+'T00:00:00+0300', eDate +'T23:59:59+0300']
    )
    
    args = {
        'nav': 'depreciations',
        'depreciations': depreciations,
        'startDate': sDate,
        'endDate': eDate,
        'range': sDate + ' - ' + eDate
    }

    return render(request, 'expenses/depreciations/index.html', args)

@login_required
def add(request):
    if request.method == 'POST':
        form = DepreciationForm(request.POST, request.FILES)
        if form.is_valid():
            depreciation = form.save()

            messages.add_message(
                request, messages.SUCCESS, 
                'Successfully Added Depreciation! Particulars: ' + depreciation.particulars
            )
            return redirect('depreciations')

    else:
        form = DepreciationForm()
    
    args = {
        'nav': 'depreciations',
        'form': form,
    }

    return render(request, 'expenses/depreciations/add.html', args)

def change(request, pk):
    depreciation = get_object_or_404(Depreciation, pk=pk)

    if request.method == 'POST':
        form = DepreciationForm(request.POST, request.FILES, instance=depreciation)
        if form.is_valid():
            try:
                if depreciation.receipt and request.FILES['receipt']:
                    default_storage.delete(depreciation.receipt.path)
                if depreciation.document and request.FILES['document']:
                    default_storage.delete(depreciation.document.path)
            except:  
                pass

            depreciation = form.save()
            messages.add_message(
                request, messages.SUCCESS, 
                'Successfully Updated Depreciation! Particulars: ' + depreciation.particulars
            ) 
            return redirect(depreciation.get_absolute_url())
    else:
        form = DepreciationForm(instance=depreciation)

    args = {
        'nav': 'depreciations',
        'depreciation': depreciation,
        'form': form
    }

    return render(request, 'expenses/depreciations/change.html', args)

@login_required
def detail(request, pk):
    depreciation = get_object_or_404(Depreciation, pk=pk)

    args = {
        'nav': 'depreciations',
        'depreciation': depreciation
    }
    return render(request, 'expenses/depreciations/details.html', args)

@login_required
def delete(request, pk):
    depreciation = get_object_or_404(Depreciation, pk=pk)
    if depreciation.receipt:
        depreciation.receipt.delete()
    if depreciation.document:
        depreciation.document.delete()
    depreciation.delete()
    messages.add_message(
        request, messages.INFO, 
        'Successfully Deleted Depreciation! Particulars: ' + depreciation.particulars
    )
    return redirect('depreciations')
