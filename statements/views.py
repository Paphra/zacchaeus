from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required
def index(request):

    return render(request, 'statements/index.html')

@login_required
def balance(request):
    
    return render(request, 'statements/balance.html')

@login_required
def income(request):

    return render(request, 'statements/income.html')