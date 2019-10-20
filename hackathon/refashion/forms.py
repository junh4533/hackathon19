from django import forms
from django.forms import ModelForm
from .models import *

class DonateForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ('combined_weight','user')

# class LoginForm(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)

# class RedeemForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('points_balance')