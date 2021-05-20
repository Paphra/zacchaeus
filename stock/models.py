from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from datetime import datetime 

class OpeningStock(models.Model):
    business = models.ForeignKey('businesses.Business', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    particulars = models.CharField(max_length = 150)
    details = models.TextField()

    document = models.FileField(upload_to='documents/%Y-%m-%d/stock/opening/', null=True)

    amount = models.IntegerField(default=0)
    date_made = models.DateTimeField(default=datetime.now)
    created = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Opening Stock"
        verbose_name_plural = "Opening Stocks"
        ordering = ['-date_made']

    def __str__(self):
        return self.particulars

    def get_absolute_url(self):
        return reverse("opening_stock_detail", kwargs={"pk": self.pk})


class ClosingStock(models.Model):
    business = models.ForeignKey('businesses.Business', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    particulars = models.CharField(max_length = 150)
    details = models.TextField()
    amount = models.IntegerField(default=0)
    
    document = models.FileField(upload_to='documents/%Y-%m-%d/stock/closing/', null=True)
    
    date_made = models.DateTimeField(default=datetime.now)
    created = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Closing Stock"
        verbose_name_plural = "Closing Stocks"
        ordering = ['-date_made']

    def __str__(self):
        return self.particulars

    def get_absolute_url(self):
        return reverse("closing_stock_detail", kwargs={"pk": self.pk})
