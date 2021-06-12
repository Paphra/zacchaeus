from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    
    args = {
        'nav': 'contact'
    }

    return render(request, 'contact/index.html', args)
