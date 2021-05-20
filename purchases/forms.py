from django import forms
from purchases.models import Purchase

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['business', 'user', 'particulars', 'details', 'amount', 'date_made']
        