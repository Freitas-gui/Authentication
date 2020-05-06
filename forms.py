from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ProfilePerson

class SignUpForm(UserCreationForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    first_name = forms.CharField(max_length=30)
    location = forms.CharField(max_length=300)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'birth_date', 'location')


class SignUpFormPsi(forms.ModelForm):
    crp = forms.CharField(max_length=10)
    class Meta:
        model = ProfilePerson
        fields = ('bio','crp')
