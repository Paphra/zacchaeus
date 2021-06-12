from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import date
from django.contrib import messages

from .models import Interest
from .forms import InterestForm

@login_required
def index(request):
    today = date.today()
    sDate = str(today.year) + '-' + str(today.month) + '-01'
    eDate = str(today.year) + '-' + str(today.month) + '-' + str(today.day)
    if request.GET.get('range'):
        dates = request.GET.get('range').split(sep=" - ")
        sDate = dates[0]
        eDate = dates[1]
    interests = Interest.objects.filter(
        person=request.user.person,
        date_made__range=[sDate+'T00:00:00+0300', eDate +'T23:59:59+0300']
    )
    
    args = {
        'nav': 'interests',
        'interests': interests,
        'startDate': sDate,
        'endDate': eDate,
        'range': sDate + ' - ' + eDate
    }

    return render(request, 'incomes/interests/index.html', args)

@login_required
def add(request):
    if request.method == 'POST':
        form = InterestForm(request.POST, request.FILES)
        if form.is_valid():
            interest = form.save()

            messages.add_message(
                request, messages.SUCCESS, 
                'Successfully Added Interest! Particulars: ' + interest.particulars
            )
            return redirect('interests')

    else:
        form = InterestForm()
    
    args = {
        'nav': 'interests',
        'form': form,
    }

    return render(request, 'incomes/interests/add.html', args)

def change(request, pk):
    interest = get_object_or_404(Interest, pk=pk)

    if request.method == 'POST':
        form = InterestForm(request.POST, request.FILES, instance=interest)
        if form.is_valid():
            try:
                if interest.receipt and request.FILES['receipt']:
                    default_storage.delete(interest.receipt.path)
                if interest.document and request.FILES['document']:
                    default_storage.delete(interest.document.path)
            except:  
                pass

            interest = form.save()
            messages.add_message(
                request, messages.SUCCESS, 
                'Successfully Updated Interest! Particulars: ' + interest.particulars
            ) 
            return redirect(interest.get_absolute_url())
    else:
        form = InterestForm(instance=interest)

    args = {
        'nav': 'interests',
        'interest': interest,
        'form': form
    }

    return render(request, 'incomes/interests/change.html', args)

@login_required
def detail(request, pk):
    interest = get_object_or_404(Interest, pk=pk)

    args = {
        'nav': 'interests',
        'interest': interest
    }
    return render(request, 'incomes/interests/details.html', args)

@login_required
def delete(request, pk):
    interest = get_object_or_404(Interest, pk=pk)
    if interest.receipt:
        interest.receipt.delete()
    if interest.document:
        interest.document.delete()
    interest.delete()
    messages.add_message(
        request, messages.INFO, 
        'Successfully Deleted Interest! Particulars: ' + interest.particulars
    )
    return redirect('interests')
