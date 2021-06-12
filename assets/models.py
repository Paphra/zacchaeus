from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from datetime import datetime 

class Asset(models.Model):
    person = models.ForeignKey('persons.Person', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    particulars = models.CharField(max_length = 150)
    details = models.TextField()
    amount = models.IntegerField(default=0)

    receipt = models.ImageField(upload_to='uploads/receipts/%Y-%m-%d/assets/', null=True, blank=True)
    document = models.FileField(upload_to='uploads/documents/%Y-%m-%d/assets/', null=True, blank=True)
    
    date_made = models.DateTimeField(default=datetime.now)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Debtor"
        verbose_name_plural = "Debtors"
        ordering = ['-date_made']

    def __str__(self):
        return self.particulars

    def get_absolute_url(self):
        return reverse("asset_detail", kwargs={"pk": self.pk})

class Debtor(models.Model):
    person = models.ForeignKey('persons.Person', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    particulars = models.CharField(max_length = 150)
    details = models.TextField()
    receipt = models.ImageField(upload_to='uploads/receipts/%Y-%m-%d/assets/debtors/', null=True, blank=True)
    document = models.FileField(upload_to='uploads/documents/%Y-%m-%d/assets/debtors/', null=True, blank=True)

    amount = models.IntegerField(default=0)
    
    date_made = models.DateTimeField(default=datetime.now)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Debtor"
        verbose_name_plural = "Debtors"
        ordering = ['-date_made']

    def __str__(self):
        return self.particulars

    def get_absolute_url(self):
        return reverse("debtor_detail", kwargs={"pk": self.pk})
