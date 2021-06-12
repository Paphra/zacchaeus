from django import forms
from .models import Purchase, PurchasesReturn

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['person', 'user', 'particulars', 'details', 'amount', 'receipt', 'document', 'date_made']
        
class PurchasesReturnForm(forms.ModelForm):
    class Meta:
        model = PurchasesReturn
        fields = ['person', 'user', 'particulars', 'details', 'amount', 'receipt', 'document', 'date_made']
