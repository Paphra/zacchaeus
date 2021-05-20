from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.contrib.auth.models import Group

from businesses.forms import BusinessForm, UserForm
from businesses.models import User, Business

@login_required
def index(request):
    
    return render(request, 'businesses/users/index.html')

@login_required
def add(request):
    groups = Group.objects.all()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.groups.add(request.POST['group'])

            messages.add_message(
                request, messages.SUCCESS, 
                'Successfully Added Business User! Username: ' + user.username
            )
            return redirect('users')
    else:
        form = UserForm()
    
    args = {
        'form': form,
        'groups': groups
    }
    return render(request, 'businesses/users/add.html', args)

@login_required
def delete(request, pk):
    user = User.objects.get(pk=pk)
    user.delete()
    messages.add_message(
        request, messages.INFO, 
        'Successfully Deleted Business User! Username: ' + user.username
    )
    return redirect('users')


@login_required
def view(request, pk):
    user = User.objects.get(pk=pk)
    args = {
        'user': user
    }
    return render(request, 'businesses/users/view.html', args)