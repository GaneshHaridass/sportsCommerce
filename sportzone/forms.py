from django import forms
from.models import *
from django.forms import ModelForm

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)

class CustomerRegisterForm(ModelForm):
    class Meta:
        model =CustomerApplicantTable
        fields = '__all__'
