from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import date
from django.contrib import messages

from .models import Withdrawal
from .forms import WithdrawalForm

@login_required
def index(request):
    today = date.today()
    sDate = str(today.year) + '-' + str(today.month) + '-01'
    eDate = str(today.year) + '-' + str(today.month) + '-' + str(today.day)
    if request.GET.get('range'):
        dates = request.GET.get('range').split(sep=" - ")
        sDate = dates[0]
        eDate = dates[1]
    withdrawals = Withdrawal.objects.filter(
        person=request.user.person,
        date_made__range=[sDate+'T00:00:00+0300', eDate +'T23:59:59+0300']
    )
    
    args = {
        'nav': 'withdrawals',
        'withdrawals': withdrawals,
        'startDate': sDate,
        'endDate': eDate,
        'range': sDate + ' - ' + eDate
    }

    return render(request, 'liabilities/withdrawals/index.html', args)

@login_required
def add(request):
    if request.method == 'POST':
        form = WithdrawalForm(request.POST, request.FILES)
        if form.is_valid():
            withdrawal = form.save()

            messages.add_message(
                request, messages.SUCCESS, 
                'Successfully Added Withdrawals Return! Particulars: ' + withdrawal.particulars
            )
            return redirect('withdrawals')

    else:
        form = WithdrawalForm()
    
    args = {
        'nav': 'withdrawals',
        'form': form,
    }

    return render(request, 'liabilities/withdrawals/add.html', args)

def change(request, pk):
    withdrawal = get_object_or_404(Withdrawal, pk=pk)

    if request.method == 'POST':
        form = WithdrawalForm(request.POST, request.FILES, instance=withdrawal)
        if form.is_valid():
            try:
                if withdrawal.receipt and request.FILES['receipt']:
                    default_storage.delete(withdrawal.receipt.path)
                if withdrawal.document and request.FILES['document']:
                    default_storage.delete(withdrawal.document.path)
            except:  
                pass

            withdrawal = form.save()
            messages.add_message(
                request, messages.SUCCESS, 
                'Successfully Updated Withdrawals Return! Particulars: ' + withdrawal.particulars
            ) 
            return redirect(withdrawal.get_absolute_url())
    else:
        form = WithdrawalForm(instance=withdrawal)

    args = {
        'nav': 'withdrawals',
        'withdrawal': withdrawal,
        'form': form
    }

    return render(request, 'liabilities/withdrawals/change.html', args)

@login_required
def detail(request, pk):
    withdrawal = get_object_or_404(Withdrawal, pk=pk)

    args = {
        'nav': 'withdrawals',
        'withdrawal': withdrawal
    }
    return render(request, 'liabilities/withdrawals/details.html', args)

@login_required
def delete(request, pk):
    withdrawal = get_object_or_404(Withdrawal, pk=pk)
    if withdrawal.receipt:
        withdrawal.receipt.delete()
    if withdrawal.document:
        withdrawal.document.delete()
    withdrawal.delete()
    messages.add_message(
        request, messages.INFO, 
        'Successfully Deleted Withdrawals Return! Particulars: ' + withdrawal.particulars
    )
    return redirect('withdrawals')
