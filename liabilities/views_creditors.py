from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import date
from django.contrib import messages

from .models import Creditor
from .forms import CreditorForm

@login_required
def index(request):
    today = date.today()
    sDate = str(today.year) + '-' + str(today.month) + '-01'
    eDate = str(today.year) + '-' + str(today.month) + '-' + str(today.day)
    if request.GET.get('range'):
        dates = request.GET.get('range').split(sep=" - ")
        sDate = dates[0]
        eDate = dates[1]
    creditors = Creditor.objects.filter(
        person=request.user.person,
        date_made__range=[sDate+'T00:00:00+0300', eDate +'T23:59:59+0300']
    )
    
    args = {
        'nav': 'creditors',
        'creditors': creditors,
        'startDate': sDate,
        'endDate': eDate,
        'range': sDate + ' - ' + eDate
    }

    return render(request, 'liabilities/creditors/index.html', args)

@login_required
def add(request):
    if request.method == 'POST':
        form = CreditorForm(request.POST, request.FILES)
        if form.is_valid():
            creditor = form.save()

            messages.add_message(
                request, messages.SUCCESS, 
                'Successfully Added Creditors Return! Particulars: ' + creditor.particulars
            )
            return redirect('creditors')

    else:
        form = CreditorForm()
    
    args = {
        'nav': 'creditors',
        'form': form,
    }

    return render(request, 'liabilities/creditors/add.html', args)

def change(request, pk):
    creditor = get_object_or_404(Creditor, pk=pk)

    if request.method == 'POST':
        form = CreditorForm(request.POST, request.FILES, instance=creditor)
        if form.is_valid():
            try:
                if creditor.receipt and request.FILES['receipt']:
                    default_storage.delete(creditor.receipt.path)
                if creditor.document and request.FILES['document']:
                    default_storage.delete(creditor.document.path)
            except:  
                pass

            creditor = form.save()
            messages.add_message(
                request, messages.SUCCESS, 
                'Successfully Updated Creditors Return! Particulars: ' + creditor.particulars
            ) 
            return redirect(creditor.get_absolute_url())
    else:
        form = CreditorForm(instance=creditor)

    args = {
        'nav': 'creditors',
        'creditor': creditor,
        'form': form
    }

    return render(request, 'liabilities/creditors/change.html', args)

@login_required
def detail(request, pk):
    creditor = get_object_or_404(Creditor, pk=pk)

    args = {
        'nav': 'creditors',
        'creditor': creditor
    }
    return render(request, 'liabilities/creditors/details.html', args)

@login_required
def delete(request, pk):
    creditor = get_object_or_404(Creditor, pk=pk)
    if creditor.receipt:
        creditor.receipt.delete()
    if creditor.document:
        creditor.document.delete()
    creditor.delete()
    messages.add_message(
        request, messages.INFO, 
        'Successfully Deleted Creditors Return! Particulars: ' + creditor.particulars
    )
    return redirect('creditors')
