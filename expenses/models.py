from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from datetime import datetime 

class Expense(models.Model):
    person = models.ForeignKey('persons.Person', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    particulars = models.CharField(max_length = 150)
    details = models.TextField()
    amount = models.IntegerField(default=0)

    receipt = models.ImageField(upload_to='uploads/receipts/%Y-%m-%d/expenses/', null=True, blank=True)
    document = models.FileField(upload_to='uploads/documents/%Y-%m-%d/expenses/', null=True, blank=True)
    
    date_made = models.DateTimeField(default=datetime.now)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Expense"
        verbose_name_plural = "Expenses"
        ordering = ['-date_made']

    def __str__(self):
        return self.particulars

    def get_absolute_url(self):
        return reverse("expense_detail", kwargs={"pk": self.pk})

class Depreciation(models.Model):
    person = models.ForeignKey('persons.Person', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    particulars = models.CharField(max_length = 150)
    details = models.TextField()
    amount = models.IntegerField(default=0)

    receipt = models.ImageField(upload_to='uploads/receipts/%Y-%m-%d/depreciations/', null=True, blank=True)
    document = models.FileField(upload_to='uploads/documents/%Y-%m-%d/depreciations/', null=True, blank=True)
    
    date_made = models.DateTimeField(default=datetime.now)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Depreciation"
        verbose_name_plural = "Depreciations"
        ordering = ['-date_made']

    def __str__(self):
        return self.particulars

    def get_absolute_url(self):
        return reverse("depreciation_detail", kwargs={"pk": self.pk})
