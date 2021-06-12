from django import forms
from .models import Income, Interest, PropertyIncome

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['person', 'user', 'particulars', 'details', 'amount', 'receipt', 'document', 'date_made']

class InterestForm(forms.ModelForm):
    class Meta:
        model = Interest
        fields = ['person', 'user', 'particulars', 'details', 'amount', 'receipt', 'document', 'date_made']

class PropertyIncomeForm(forms.ModelForm):
    class Meta:
        model = PropertyIncome
        fields = ['person', 'user', 'particulars', 'details', 'amount', 'receipt', 'document', 'date_made']
