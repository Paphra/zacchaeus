from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    args = {
        'nav': 'faq'
    }
    return render(request, 'faq/index.html', args)