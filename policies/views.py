from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    args = {
        'nav': 'policies',
    }
    return render(request, 'policies/index.html', args)