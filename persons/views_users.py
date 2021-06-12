from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.contrib.auth.models import Group

from .forms import UserForm
from .models import User, Person

@login_required
def index(request):
    args = {
        'nav': 'users',
    }

    return render(request, 'users/index.html', args)

@login_required
def add(request):
    groups = Group.objects.all()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.person = request.user.person
            user.save()

            messages.add_message(
                request, messages.SUCCESS, 
                'Successfully Added Person User! Username: ' + user.username
            )
            return redirect('users')
    else:
        form = UserForm()
    
    args = {
        'nav': 'users',
        'form': form,
        'groups': groups
    }
    return render(request, 'users/add.html', args)

@login_required
def delete(request, pk):
    user = User.objects.get(pk=pk)
    user.delete()
    messages.add_message(
        request, messages.INFO, 
        'Successfully Deleted Person User! Username: ' + user.username
    )
    return redirect('users')


@login_required
def detail(request, pk):
    user = User.objects.get(pk=pk)
    args = {
        'nav': 'users',
        'user': user
    }
    return render(request, 'users/view.html', args)