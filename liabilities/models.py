from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from datetime import datetime 

class Liability(models.Model):
    person = models.ForeignKey('persons.Person', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    particulars = models.CharField(max_length = 150)
    details = models.TextField()
    amount = models.IntegerField(default=0)

    receipt = models.ImageField(upload_to='uploads/receipts/%Y-%m-%d/liabilities/', null=True, blank=True)
    document = models.FileField(upload_to='uploads/documents/%Y-%m-%d/liabilities/', null=True, blank=True)
    
    date_made = models.DateTimeField(default=datetime.now)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Liability"
        verbose_name_plural = "Liabilities"
        ordering = ['-date_made']

    def __str__(self):
        return self.particulars

    def get_absolute_url(self):
        return reverse("liability_detail", kwargs={"pk": self.pk})

class Creditor(models.Model):
    person = models.ForeignKey('persons.Person', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    particulars = models.CharField(max_length = 150)
    details = models.TextField()

    receipt = models.ImageField(upload_to='uploads/receipts/%Y-%m-%d/liabilities/creditors/', null=True, blank=True)
    document = models.FileField(upload_to='uploads/documents/%Y-%m-%d/liabilities/creditors/', null=True, blank=True)

    amount = models.IntegerField(default=0)

    date_made = models.DateTimeField(default=datetime.now)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Creditor"
        verbose_name_plural = "Creditors"
        ordering = ['-date_made']

    def __str__(self):
        return self.particulars

    def get_absolute_url(self):
        return reverse("creditor_detail", kwargs={"pk": self.pk})

class Withdrawal(models.Model):
    person = models.ForeignKey('persons.Person', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    particulars = models.CharField(max_length = 150)
    details = models.TextField()

    receipt = models.ImageField(upload_to='uploads/receipts/%Y-%m-%d/liabilities/withdrawals/', null=True, blank=True)
    document = models.FileField(upload_to='uploads/documents/%Y-%m-%d/liabilities/withdrawals/', null=True, blank=True)

    amount = models.IntegerField(default=0)

    date_made = models.DateTimeField(default=datetime.now)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Withdrawal"
        verbose_name_plural = "Withdrawals"
        ordering = ['-date_made']

    def __str__(self):
        return self.particulars

    def get_absolute_url(self):
        return reverse("withdrawal_detail", kwargs={"pk": self.pk})
