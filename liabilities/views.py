from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import date
from django.contrib import messages

from .models import Liability
from .forms import LiabilityForm

@login_required
def index(request):
    today = date.today()
    sDate = str(today.year) + '-' + str(today.month) + '-01'
    eDate = str(today.year) + '-' + str(today.month) + '-' + str(today.day)
    if request.GET.get('range'):
        dates = request.GET.get('range').split(sep=" - ")
        sDate = dates[0]
        eDate = dates[1]
    liabilities = Liability.objects.filter(
        person=request.user.person,
        date_made__range=[sDate+'T00:00:00+0300', eDate +'T23:59:59+0300']
    )
    
    args = {
        'nav': 'liabilities',
        'liabilities': liabilities,
        'startDate': sDate,
        'endDate': eDate,
        'range': sDate + ' - ' + eDate
    }

    return render(request, 'liabilities/index.html', args)

@login_required
def add(request):
    if request.method == 'POST':
        form = LiabilityForm(request.POST, request.FILES)
        if form.is_valid():
            liability = form.save()

            messages.add_message(
                request, messages.SUCCESS, 
                'Successfully Added Liability! Particulars: ' + liability.particulars
            )
            return redirect('liabilities')

    else:
        form = LiabilityForm()
    
    args = {
        'nav': 'liabilities',
        'form': form,
    }

    return render(request, 'liabilities/add.html', args)

def change(request, pk):
    liability = get_object_or_404(Liability, pk=pk)

    if request.method == 'POST':
        form = LiabilityForm(request.POST, request.FILES, instance=liability)
        if form.is_valid():
            try:
                if liability.receipt and request.FILES['receipt']:
                    default_storage.delete(liability.receipt.path)
                if liability.document and request.FILES['document']:
                    default_storage.delete(liability.document.path)
            except:  
                pass

            liability = form.save()
            messages.add_message(
                request, messages.SUCCESS, 
                'Successfully Updated Liability! Particulars: ' + liability.particulars
            ) 
            return redirect(liability.get_absolute_url())
    else:
        form = LiabilityForm(instance=liability)

    args = {
        'nav': 'liabilities',
        'liability': liability,
        'form': form
    }

    return render(request, 'liabilities/change.html', args)

@login_required
def detail(request, pk):
    liability = get_object_or_404(Liability, pk=pk)

    args = {
        'nav': 'liabilities',
        'liability': liability
    }
    return render(request, 'liabilities/details.html', args)

@login_required
def delete(request, pk):
    liability = get_object_or_404(Liability, pk=pk)
    if liability.receipt:
        liability.receipt.delete()
    if liability.document:
        liability.document.delete()
    liability.delete()
    messages.add_message(
        request, messages.INFO, 
        'Successfully Deleted Liability! Particulars: ' + liability.particulars
    )
    return redirect('liabilities')
