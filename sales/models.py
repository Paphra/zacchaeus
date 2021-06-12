from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from datetime import datetime 

class Sale(models.Model):
    person = models.ForeignKey('persons.Person', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    particulars = models.CharField(max_length = 150)
    details = models.TextField()
    amount = models.IntegerField(default=0)

    receipt = models.ImageField(upload_to='uploads/receipts/%Y-%m-%d/sales/', null=True, blank=True)
    document = models.FileField(upload_to='uploads/documents/%Y-%m-%d/sales/', null=True, blank=True)
    
    date_made = models.DateTimeField(default=datetime.now)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Sale"
        verbose_name_plural = "Sales"
        ordering = ['-date_made']

    def __str__(self):
        return self.particulars

    def get_absolute_url(self):
        return reverse("sale_detail", kwargs={"pk": self.pk})

class SalesReturn(models.Model):
    person = models.ForeignKey('persons.Person', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    particulars = models.CharField(max_length = 150)
    details = models.TextField()
    receipt = models.ImageField(upload_to='uploads/receipts/%Y-%m-%d/sales/returns/', null=True, blank=True)
    document = models.FileField(upload_to='uploads/documents/%Y-%m-%d/sales/returns/', null=True, blank=True)

    amount = models.IntegerField(default=0)

    date_made = models.DateTimeField(default=datetime.now)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Sales Return"
        verbose_name_plural = "Sales Returns"
        ordering = ['-date_made']

    def __str__(self):
        return self.particulars

    def get_absolute_url(self):
        return reverse("sales_return_detail", kwargs={"pk": self.pk})
