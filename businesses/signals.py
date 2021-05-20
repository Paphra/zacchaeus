from django.dispatch import receiver
from django_registration.signals import user_activated
from django.contrib.auth.models import Group

@receiver(user_activated)
def after_user_activation(sender, user, request, **kwargs):
    owners = Group.objects.get(name="Business Owner")
    owners.user_set.add(user)
