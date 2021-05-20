from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from datetime import datetime

class Expense(models.Model):
    business = models.ForeignKey('businesses.Business', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    particulars = models.CharField(max_length = 150)
    details = models.TextField()
    amount = models.IntegerField(default=0)

    receipt = models.ImageField(upload_to='receipts/%Y-%m-%d/expenses/', null=True)
    document = models.FileField(upload_to='documents/%Y-%m-%d/expenses/', null=True)

    date_made = models.DateTimeField(default=datetime.now)
    created = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Expense"
        verbose_name_plural = "Expenses"
        ordering = ['-date_made']

    def __str__(self):
        return self.particulars

    def get_absolute_url(self):
        return reverse("expense_detail", kwargs={"pk": self.pk})
