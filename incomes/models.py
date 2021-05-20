from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from datetime import datetime

class Income(models.Model):
    business = models.ForeignKey('businesses.Business', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    particulars = models.CharField(max_length = 150)
    details = models.TextField()
    amount = models.IntegerField(default=0)

    receipt = models.ImageField(upload_to='receipts/%Y-%m-%d/incomes/', null=True)
    document = models.FileField(upload_to='documents/%Y-%m-%d/incomes/', null=True)

    date_made = models.DateTimeField(default=datetime.now)
    created = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Income"
        verbose_name_plural = "Incomes"
        ordering = ['-date_made']

    def __str__(self):
        return self.particulars

    def get_absolute_url(self):
        return reverse("income_detail", kwargs={"pk": self.pk})
