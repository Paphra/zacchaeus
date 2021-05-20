from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from datetime import datetime

class Purchase(models.Model):
    business = models.ForeignKey('businesses.Business', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    particulars = models.CharField(max_length = 150)
    details = models.TextField()
    amount = models.IntegerField(default=0)

    receipt = models.ImageField(upload_to='receipts/%Y-%m-%d/purchases/', null=True)
    document = models.FileField(upload_to='documents/%Y-%m-%d/purchases/', null=True)

    date_made = models.DateTimeField(default=datetime.now)
    created = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Purchase"
        verbose_name_plural = "Purchases"
        ordering = ['-date_made']

    def __str__(self):
        return self.particulars

    def get_absolute_url(self):
        return reverse("purchase_detail", kwargs={"pk": self.pk})

class PurchasesReturn(models.Model):

    purchase = models.ForeignKey('purchases.Purchase', on_delete=models.CASCADE)
    particulars = models.CharField(max_length = 150)
    details = models.TextField()

    receipt = models.ImageField(upload_to='receipts/%Y-%m-%d/purchases/returns/', null=True)
    document = models.FileField(upload_to='documents/%Y-%m-%d/purchases/returns/', null=True)

    amount = models.IntegerField(default=0)
    date_made = models.DateTimeField(default=datetime.now)
    
    created = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Purchases Return"
        verbose_name_plural = "Purchases Returns"
        ordering = ['-date_made']

    def __str__(self):
        return self.particulars

    def get_absolute_url(self):
        return reverse("purchases_return_detail", kwargs={"pk": self.pk})
