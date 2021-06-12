from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.core.files.storage import default_storage
from .models import Mail
from .forms import MailForm
from persons.models import Person

@login_required
def index(request):
    person = request.user.person
    mail_list = Mail.objects.filter(receipient=person, receipient_trash=False)

    page = request.GET.get('page', 1)
    paginator = Paginator(mail_list, 15)
    try:
        mails = paginator.page(page)
    except PageNotAnInteger:
        mails = paginator.page(1)
    except EmptyPage:
        mails = paginator.page(paginator.num_pages)

    args = {
        'nav': 'mails',
        'nav_mails': 'inbox',
        'url': 'mails',
        'heading': 'Inbox',
        'mails': mails,
    }
    
    return render(request, 'mails/index.html', args)

@login_required
def compose(request):
    persons = Person.objects.all()
    if request.method == 'POST':
        form = MailForm(request.POST, request.FILES)
        if form.is_valid():
            mail = form.save()

            messages.add_message(
                request, messages.SUCCESS, 
                'Mssage Sent! Subject: ' + mail.subject
            )

            return redirect('mails')

    else:
        form = MailForm()
    
    args = {
        'nav': 'mails',
        'nav_mails': 'compose',
        'persons': persons,
        'form': form,
    }
    
    return render(request, 'mails/compose.html', args)

@login_required
def detail(request, pk):
    person = request.user.person
    mail = get_object_or_404(Mail, pk=pk)
    if mail.receipient != person and mail.sender_person != person:
        messages.add_message(
            request, messages.INFO,
            'Tried to Access an unauthorized message'
            )
        return redirect('mails')

    if mail.receipient == person and not mail.read:
        mail.read = True
        mail.date_read = datetime.now()
        mail.save()

    args = {
        'nav': 'mails',
        'nav_mails': 'inbox',
        'mail': mail,
    }

    return render(request, 'mails/read.html', args)

@login_required
def sent(request):
    person = request.user.person
    mail_list = Mail.objects.filter(sender_trash=False, sender_person=person)

    page = request.GET.get('page', 1)    
    paginator = Paginator(mail_list, 15)
    try:
        mails = paginator.page(page)
    except PageNotAnInteger:
        mails = paginator.page(1)
    except EmptyPage:
        mails = paginator.page(paginator.num_pages)

    args = {
        'nav': 'mails',
        'heading': 'Sent Mails',
        'nav_mails': 'sent',
        'url': 'mail_sent',
        'mails': mails,
    }
    
    return render(request, 'mails/index.html', args)

@login_required
def delete(request, pk):
    person = request.user.person
    mail = get_object_or_404(Mail, pk=pk)
    if mail.receipient != person and mail.sender_person != person:
        messages.add_message(
            request, messages.INFO,
            'Tried to Access an unauthorized Mail'
            )
        return redirect('mails')

    if mail.receipient_trash or mail.sender_trash or mail.draft:
        if mail.attachment:
            mail.attachment.delete()
        mail.delete()
    else:
        if mail.receipient == person:
            mail.receipient_trash = True
        if mail.sender_person == person:
            mail.sender_trash = True
        mail.save()

    messages.add_message(
        request, messages.INFO,
        'Mail Deleted!'
        )
    return redirect('mails')
