from django import forms
from django.db import models
from django.forms import fields
from App_Payment.models import BillingAddress


class BillingForm(forms.ModelForm):
    class Meta:
        model = BillingAddress
        fields = ['address','zipcode','city','country',]