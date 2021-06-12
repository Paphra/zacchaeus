from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import date
from django.contrib import messages

from .models import Debtor
from .forms import DebtorForm

@login_required
def index(request):
    today = date.today()
    sDate = str(today.year) + '-' + str(today.month) + '-01'
    eDate = str(today.year) + '-' + str(today.month) + '-' + str(today.day)
    if request.GET.get('range'):
        dates = request.GET.get('range').split(sep=" - ")
        sDate = dates[0]
        eDate = dates[1]
    debtors = Debtor.objects.filter(
        person=request.user.person,
        date_made__range=[sDate+'T00:00:00+0300', eDate +'T23:59:59+0300']
    )
    
    args = {
        'nav': 'debtors',
        'debtors': debtors,
        'startDate': sDate,
        'endDate': eDate,
        'range': sDate + ' - ' + eDate
    }

    return render(request, 'assets/debtors/index.html', args)

@login_required
def add(request):
    if request.method == 'POST':
        form = DebtorForm(request.POST, request.FILES)
        if form.is_valid():
            debtor = form.save()
            messages.add_message(
                request, messages.SUCCESS, 
                'Successfully Added Debtors Return! Particulars: ' + debtor.particulars
            )
            return redirect('debtors')

    else:
        form = DebtorForm()
    
    args = {
        'nav': 'debtors',
        'form': form,
    }

    return render(request, 'assets/debtors/add.html', args)

def change(request, pk):
    debtor = get_object_or_404(Debtor, pk=pk)

    if request.method == 'POST':
        form = DebtorForm(request.POST, request.FILES, instance=debtor)
        if form.is_valid():
            # print(request.POST['status'])
            try:
                if debtor.receipt and request.FILES['receipt']:
                    default_storage.delete(debtor.receipt.path)
                if debtor.document and request.FILES['document']:
                    default_storage.delete(debtor.document.path)
            except:  
                pass

            debtor = form.save()
            messages.add_message(
                request, messages.SUCCESS, 
                'Successfully Updated Debtors Return! Particulars: ' + debtor.particulars
            ) 
            return redirect(debtor.get_absolute_url())
    else:
        form = DebtorForm(instance=debtor)

    args = {
        'nav': 'debtors',
        'debtor': debtor,
        'form': form
    }

    return render(request, 'assets/debtors/change.html', args)

@login_required
def detail(request, pk):
    debtor = get_object_or_404(Debtor, pk=pk)

    args = {
        'nav': 'debtors',
        'debtor': debtor
    }
    return render(request, 'assets/debtors/details.html', args)

@login_required
def delete(request, pk):
    debtor = get_object_or_404(Debtor, pk=pk)
    if debtor.receipt:
        debtor.receipt.delete()
    if debtor.document:
        debtor.document.delete()
    debtor.delete()
    messages.add_message(
        request, messages.INFO, 
        'Successfully Deleted Debtors Return! Particulars: ' + debtor.particulars
    )
    return redirect('debtors')
