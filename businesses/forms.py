from django_registration.forms import RegistrationForm
from django.forms import ModelForm
from businesses.models import User, Business

class UserForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = User
        fields = ['username', 'business', 'first_name', 'last_name', 'phone', 'email', 'password1', 'password2']

class BusinessForm(ModelForm):
    class Meta:
        model = Business
        fields = ['owner', 'name', 'phone', 'email', 'website']