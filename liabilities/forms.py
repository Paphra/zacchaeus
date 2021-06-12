from django import forms
from .models import Liability, Creditor, Withdrawal

class LiabilityForm(forms.ModelForm):
    class Meta:
        model = Liability
        fields = ['person', 'user', 'particulars', 'details', 'amount', 'receipt', 'document', 'date_made']
        
class CreditorForm(forms.ModelForm):
    class Meta:
        model = Creditor
        fields = ['person', 'user', 'particulars', 'details', 'amount', 'receipt', 'document', 'date_made']
        
class WithdrawalForm(forms.ModelForm):
    class Meta:
        model = Withdrawal
        fields = ['person', 'user', 'particulars', 'details', 'amount', 'receipt', 'document', 'date_made']
