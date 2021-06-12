from django.dispatch import receiver
from django_registration.signals import user_activated
from django.contrib.auth.models import Group
from persons.models import Person

@receiver(user_activated)
def after_user_activation(sender, user, request, **kwargs):
    person = Person()
    person.owner = user
    person.name = user.username
    person.save()
    groups = Group.objects.all()
    if groups:
        for group in groups:
            if group.name.find('Owner') != -1 or group.name.find('owner') != -1:
                user.groups.add(group)
    user.person = person
    user.save()
