from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from datetime import datetime 

class Sale(models.Model):
    business = models.ForeignKey('businesses.Business', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    particulars = models.CharField(max_length = 150)
    details = models.TextField()
    amount = models.IntegerField(default=0)

    receipt = models.ImageField(upload_to='receipts/%Y-%m-%d/sales/', null=True)
    document = models.FileField(upload_to='documents/%Y-%m-%d/sales/', null=True)
    
    date_made = models.DateTimeField(default=datetime.now)
    created = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Sale"
        verbose_name_plural = "Sales"
        ordering = ['-date_made']

    def __str__(self):
        return self.particulars

    def get_absolute_url(self):
        return reverse("sale_detail", kwargs={"pk": self.pk})

class SalesReturn(models.Model):

    sale = models.ForeignKey('sales.Sale', on_delete=models.CASCADE)
    particulars = models.CharField(max_length = 150)
    details = models.TextField()
    receipt = models.ImageField(upload_to='receipts/%Y-%m-%d/sales/returns/', null=True)
    document = models.FileField(upload_to='documents/%Y-%m-%d/sales/returns/', null=True)

    amount = models.IntegerField(default=0)
    date_made = models.DateTimeField(default=datetime.now)
    
    created = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Sales Return"
        verbose_name_plural = "Sales Returns"
        ordering = ['-date_made']

    def __str__(self):
        return self.particulars

    def get_absolute_url(self):
        return reverse("sales_return_detail", kwargs={"pk": self.pk})
