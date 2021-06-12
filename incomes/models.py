from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from datetime import datetime 

class Income(models.Model):
    person = models.ForeignKey('persons.Person', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    particulars = models.CharField(max_length = 150)
    details = models.TextField()
    amount = models.IntegerField(default=0)

    receipt = models.ImageField(upload_to='uploads/receipts/%Y-%m-%d/incomes/', null=True, blank=True)
    document = models.FileField(upload_to='uploads/documents/%Y-%m-%d/incomes/', null=True, blank=True)
    
    date_made = models.DateTimeField(default=datetime.now)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Income"
        verbose_name_plural = "Incomes"
        ordering = ['-date_made']

    def __str__(self):
        return self.particulars

    def get_absolute_url(self):
        return reverse("income_detail", kwargs={"pk": self.pk})

class Interest(models.Model):
    person = models.ForeignKey('persons.Person', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    particulars = models.CharField(max_length = 150)
    details = models.TextField()
    amount = models.IntegerField(default=0)

    receipt = models.ImageField(upload_to='uploads/receipts/%Y-%m-%d/interests/', null=True, blank=True)
    document = models.FileField(upload_to='uploads/documents/%Y-%m-%d/interests/', null=True, blank=True)
    
    date_made = models.DateTimeField(default=datetime.now)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Interest"
        verbose_name_plural = "Interests"
        ordering = ['-date_made']

    def __str__(self):
        return self.particulars

    def get_absolute_url(self):
        return reverse("interest_detail", kwargs={"pk": self.pk})

class PropertyIncome(models.Model):
    person = models.ForeignKey('persons.Person', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    particulars = models.CharField(max_length = 150)
    details = models.TextField()
    amount = models.IntegerField(default=0)

    receipt = models.ImageField(upload_to='uploads/receipts/%Y-%m-%d/incomes/property/', null=True, blank=True)
    document = models.FileField(upload_to='uploads/documents/%Y-%m-%d/incomes/property/', null=True, blank=True)
    
    date_made = models.DateTimeField(default=datetime.now)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Property Income"
        verbose_name_plural = "Property Incomes"
        ordering = ['-date_made']

    def __str__(self):
        return self.particulars

    def get_absolute_url(self):
        return reverse("property_income_detail", kwargs={"pk": self.pk})
