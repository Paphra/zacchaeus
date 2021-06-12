from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import AbstractUser, Group
from django.conf import settings
from datetime import datetime

from taxation.models import PersonType

class User(AbstractUser):
    phone = models.CharField("Phone Number", max_length = 150, blank=True, null=True)
    person = models.ForeignKey('persons.Person', on_delete=models.SET_NULL, related_name='workers', null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, blank=True, null=True, related_name='group_users')

    photo = models.ImageField(upload_to="uploads/users/images", blank=True, null=True)

    def get_full_name(self):
        if self.first_name and self.last_name:
            return self.first_name + ' ' + self.last_name
        elif self.first_name:
            return self.first_name
        elif self.last_name:
            return self.last_name
        else:
            return self.username

    class Meta:
        ordering = ['-date_joined',]

    def get_absolute_url(self):
        return reverse('user_detail', kwargs={'pk': self.pk})

class Person(models.Model):
    
    name = models.CharField(max_length = 250)
    tin = models.CharField(max_length = 150, blank=True, null=True)
    password = models.CharField(max_length = 20, blank=True, null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='personOwned')
    person_type = models.ForeignKey(PersonType, on_delete=models.SET_NULL, null=True, default=1)
    
    # indivual
    identification = models.FileField(upload_to='uploads/persons/ids/%Y-%m-%d', blank=True, null=True)
    form_individual = models.FileField(upload_to='uploads/persons/forms/individual/%Y-%m-%d', blank=True, null=True)
    
    # company, partnership, ngo
    form_7 = models.FileField(upload_to='uploads/persons/forms/7/%Y-%m-%d', blank=True, null=True)
    form_non_individual = models.FileField(upload_to='uploads/persons/forms/non-indivual/%Y-%m-%d', blank=True, null=True)
    tenancy = models.FileField(upload_to='uploads/persons/tenancy/%Y-%m-%d', blank=True, null=True)

    reg_cert = models.FileField(upload_to='uploads/persons/certificates/%Y-%m-%d', blank=True, null=True)

    # Partnership/NGO
    deed_constitution = models.FileField(upload_to='uploads/persons/deed-or-constitution/%Y-%m-%d', blank=True, null=True)
    
    other_docs = models.FileField(upload_to='uploads/persons/others/%Y-%m-%d', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/persons/images/%Y-%m-%d', blank=True, null=True)

    # Status
    org_registration = models.BooleanField(default=False)
    ura_submitted = models.BooleanField(default=False)
    ura_registered = models.BooleanField(default=False)
    
    date_started = models.DateTimeField(default=datetime.now)
    date_created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Persons"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("person_detail", kwargs={"pk": self.pk})

    def unread_mails(self):
        mails = self.received_mails.filter(read=False)
        return mails
