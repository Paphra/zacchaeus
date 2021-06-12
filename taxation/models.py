from django.shortcuts import reverse
from django.db import models

class PersonType(models.Model):
    """
    Description: Model Description
    The Person Types May Inclde:
    1 - Company/NGO
    2 - Inidivuals
        - Property
    3 - Small Business
    """
    name = models.CharField(max_length=200)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Person Type"
        verbose_name_plural = "Person Types"
        ordering = ['-updated',]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('person_type_detail', kwargs={'pk': self.pk})

class IncomeTaxRange(models.Model):
    """
    Description: Model Description
    """
    name = models.CharField(max_length=100)
    person_type = models.ForeignKey(PersonType, on_delete=models.CASCADE)
    low = models.IntegerField(default=0)
    high = models.IntegerField(default=0)
    addition = models.IntegerField(default=0)
    subtraction = models.IntegerField(default=0)
    percentage = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True)

    is_active = models.BooleanField(default=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Income Tax Range"
        verbose_name_plural = "Income Tax Ranges"
        ordering = ['low']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("income_tax_range_detail", kwargs={"pk": self.pk})

class OtherIncomeTaxRange(models.Model):
    """
    Description: Model Description
    """
    name = models.CharField(max_length=100)
    person_type = models.ForeignKey(PersonType, on_delete=models.CASCADE)
    threshhold = models.IntegerField(default=0)
    alternative = models.IntegerField(default=0)
    subtraction = models.IntegerField(default=0)
    addition = models.IntegerField(default=0)
    percentage = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True)

    is_active = models.BooleanField(default=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Other Income Tax Range"
        verbose_name_plural = "Other Income Tax Ranges"
        ordering = ['-updated']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("income_tax_range_detail", kwargs={"pk": self.pk})
