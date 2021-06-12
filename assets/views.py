from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import date
from django.contrib import messages

from .models import Asset
from .forms import AssetForm

@login_required
def index(request):
    today = date.today()
    sDate = str(today.year) + '-' + str(today.month) + '-01'
    eDate = str(today.year) + '-' + str(today.month) + '-' + str(today.day)
    if request.GET.get('range'):
        dates = request.GET.get('range').split(sep=" - ")
        sDate = dates[0]
        eDate = dates[1]
    assets = Asset.objects.filter(
        person=request.user.person,
        date_made__range=[sDate+'T00:00:00+0300', eDate +'T23:59:59+0300']
    )
    
    args = {
        'nav': 'assets',
        'assets': assets,
        'startDate': sDate,
        'endDate': eDate,
        'range': sDate + ' - ' + eDate
    }

    return render(request, 'assets/index.html', args)

@login_required
def add(request):
    if request.method == 'POST':
        form = AssetForm(request.POST, request.FILES)
        if form.is_valid():
            asset = form.save()

            messages.add_message(
                request, messages.SUCCESS, 
                'Successfully Added Asset! Particulars: ' + asset.particulars
            )
            return redirect('assets')

    else:
        form = AssetForm()
    
    args = {
        'nav': 'assets',
        'form': form,
    }

    return render(request, 'assets/add.html', args)

def change(request, pk):
    asset = get_object_or_404(Asset, pk=pk)

    if request.method == 'POST':
        form = AssetForm(request.POST, request.FILES, instance=asset)
        if form.is_valid():
            try:
                if asset.receipt and request.FILES['receipt']:
                    default_storage.delete(asset.receipt.path)
                if asset.document and request.FILES['document']:
                    default_storage.delete(asset.document.path)
            except:  
                pass

            asset = form.save()
            messages.add_message(
                request, messages.SUCCESS, 
                'Successfully Updated Asset! Particulars: ' + asset.particulars
            ) 
            return redirect(asset.get_absolute_url())
    else:
        form = AssetForm(instance=asset)

    args = {
        'nav': 'assets',
        'asset': asset,
        'form': form
    }

    return render(request, 'assets/change.html', args)

@login_required
def detail(request, pk):
    asset = get_object_or_404(Asset, pk=pk)

    args = {
        'nav': 'assets',
        'asset': asset
    }
    return render(request, 'assets/details.html', args)

@login_required
def delete(request, pk):
    asset = get_object_or_404(Asset, pk=pk)
    if asset.receipt:
        asset.receipt.delete()
    if asset.document:
        asset.document.delete()
    asset.delete()
    messages.add_message(
        request, messages.INFO, 
        'Successfully Deleted Asset! Particulars: ' + asset.particulars
    )
    return redirect('assets')
