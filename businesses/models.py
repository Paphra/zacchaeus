from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth.models import Group
from datetime import datetime

class User(AbstractUser):
    phone = models.CharField("Phone Number", max_length = 150, blank=True, null=True)
    nationality = models.CharField(max_length=50, blank=True, null=True)
    national_id = models.CharField(max_length=50, blank=True, null=True)
    business = models.ForeignKey('businesses.Business', on_delete=models.SET_NULL, related_name="users", blank=True, null=True)
    
    def get_full_name(self):
        if self.first_name and self.last_name:
            return self.first_name + ' ' + self.last_name
        elif self.first_name:
            return self.first_name
        elif self.last_name:
            return self.last_name
        else:
            return self.username

class Business(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name="business_owned")
    name = models.CharField(max_length=150)

    phone = models.CharField(max_length = 150, blank=True, null=True)
    email = models.CharField(max_length = 150, blank=True, null=True)
    website = models.CharField(max_length = 150, blank=True, null=True)

    image = models.ImageField(upload_to='business/%Y-%m-%d/', null=True)

    tin = models.CharField(max_length = 150, unique=True, blank=True, null=True)
    registered = models.DateTimeField(default=datetime.now)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Business"
        verbose_name_plural = "Businesses"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("business_detail", kwargs={"pk": self.pk})

class Address(models.Model):

    business = models.OneToOneField("businesses.Business", on_delete=models.CASCADE)
    district = models.CharField(max_length = 50, blank=True, null=True)
    city = models.CharField(max_length = 150, blank=True, null=True)
    county = models.CharField(max_length = 150, blank=True, null=True)
    subcounty = models.CharField(max_length = 150, blank=True, null=True)
    country = models.CharField(max_length = 150, blank=True, null=True)
    parish = models.CharField(max_length = 150, blank=True, null=True)
    
    address_line = models.CharField(max_length = 250, blank=True)    

    created = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __str__(self):
        return self.address_line

    def get_absolute_url(self):
        return reverse("address_detail", kwargs={"pk": self.pk})

class Sector(models.Model):

    business = models.OneToOneField("businesses.Business", on_delete=models.CASCADE)
    name = models.CharField(max_length = 150, blank=True)
    activities = models.TextField(blank=True)
    
    created = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Sector"
        verbose_name_plural = "Sectors"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("sector_detail", kwargs={"pk": self.pk})

class Size(models.Model):
    business = models.OneToOneField("businesses.Business", on_delete=models.CASCADE)
    size = models.CharField(max_length=150)
    
    employees = models.IntegerField(default=1)
    share_capital = models.IntegerField(default=0)
    
    created = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Size"
        verbose_name_plural = "Sizes"

    def __str__(self):
        return self.size

    def get_absolute_url(self):
        return reverse("size_detail", kwargs={"pk": self.pk})

class Directorship(models.Model):
    business = models.OneToOneField("businesses.Business", on_delete=models.CASCADE)
    no_directors = models.IntegerField(default=1)
    directors = models.TextField(blank=True)
    
    created = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Directorship"
        verbose_name_plural = "Directorships"

    def __str__(self):
        return self.no_directors

    def get_absolute_url(self):
        return reverse("directorship_detail", kwargs={"pk": self.pk})
