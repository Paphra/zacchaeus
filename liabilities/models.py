from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from datetime import datetime

class Liability(models.Model):
    business = models.ForeignKey('businesses.Business', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    particulars = models.CharField(max_length = 150)
    details = models.TextField()
    l_type = models.IntegerField(default=1) # if l_type == 1: long else short
        
    amount = models.IntegerField(default=0)

    receipt = models.ImageField(upload_to='receipts/%Y-%m-%d/liabilities/', null=True)
    document = models.FileField(upload_to='documents/%Y-%m-%d/liabilities/', null=True)

    date_made = models.DateTimeField(default=datetime.now)
    created = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Liability"
        verbose_name_plural = "Liabilities"
        ordering = ['-date_made']

    def __str__(self):
        return self.particulars

    def get_absolute_url(self):
        return reverse("expense_detail", kwargs={"pk": self.pk})


class Creditor(models.Model):
    business = models.ForeignKey('businesses.Business', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    particulars = models.CharField(max_length = 150)
    details = models.TextField()
    amount = models.IntegerField(default=0)
    cleared = models.BooleanField(default=False)
    
    date_made = models.DateTimeField(default=datetime.now)
    created = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Creditor"
        verbose_name_plural = "Creditors"
        ordering = ['-date_made']

    def __str__(self):
        return self.particulars

    def get_absolute_url(self):
        return reverse("creditor_detail", kwargs={"pk": self.pk})