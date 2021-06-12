from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.contrib.auth.models import Group

from .forms import PersonForm, UserForm
from .models import User, Person

@login_required
def index(request):
    args = {
        'nav': 'person',
    }
    
    return render(request, 'persons/index.html', args)

def register(request):
    person = request.user.person

    if request.method == 'POST':
        tin = request.GET.get('tin', 0)
        if tin != 0:
            # work around for tin number
            # By Connecting to the URA/URSB API to check details and register

            tin = request.POST['tin']

        else:
            # work for person registration
            form = PersonForm(request.POST, request.FILES, instance=person)
            if form.is_valid():
                person = form.save()
                messages.add_message(
                    request, messages.SUCCESS, 
                    'Successfully Registered Person! Person Name: ' + person.name
                )

                # Do other things related to the Person
                
                return redirect('person')
    else:
        form = PersonForm(instance=person)
        
    args = {
        'nav': 'person',
        'form': form
    }
    return render(request, 'persons/register.html', args)

@login_required
def pay_fees(request):
    args = {
        'nav': 'person',
    }
    
    return render(request, 'persons/pay-fees.html', args)

@login_required
def detail(request, pk):
    person = get_object_or_404(Person, pk=pk)

    args = {
        'nav': 'person',
        'person': person
    }
    return render(request, 'persons/detail.html', args)