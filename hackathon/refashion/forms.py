from django import forms
from django.forms import ModelForm
from .models import *

class DonateForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ('combined_weight','user')
