from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.contrib.auth.models import Group

from businesses.forms import BusinessForm, UserForm
from businesses.models import User, Business

@login_required
def index(request):

    return render(request, 'businesses/index.html')

def register(request):
    
    if request.method == 'POST':
        tin = request.GET.get('tin', 0)
        if tin != 0:
            # work around for tin number
            # By Connecting to the URA/URSB API to check details and register

            tin = request.POST['tin']

        else:
            # work for business registration
            form = BusinessForm(request.POST)
            if form.is_valid():
                business = form.save()
                request.user.business = business
                request.user.save()
                messages.add_message(
                    request, messages.SUCCESS, 
                    'Successfully Registered Business! Business Name: ' + business.name
                )
                return redirect('business')
    else:
        form = BusinessForm()
        
    args = {
        'form': form
    }
    return render(request, 'businesses/register.html', args)

@login_required
def pay_fees(request):

    return render(request, 'businesses/pay-fees.html')
