from django_registration.forms import RegistrationForm
from django.forms import ModelForm
from .models import User, Person

class UserForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = User
        fields = ['username', 'first_name', 'last_name', 'phone', 'group', 'email', 'password1', 'password2']

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['owner', 'name', 'person_type', 'tin']