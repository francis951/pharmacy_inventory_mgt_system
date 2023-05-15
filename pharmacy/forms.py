from django.forms import ModelForm, TextInput
#accessing our models
from .models import *


class Addform(ModelForm):
    class Meta:
        model = Product
        fields = ['recieved_quantity']
        widgets = {
            'recieved_quantity': TextInput(attrs={'placeholder': 'Enter recieved quantity'}),
            }


class SaleForm(ModelForm):
    class Meta:
        model = Sale
        fields = ['quantity','amount_received', 'issue_to', 'date']
        widgets = {
            'quantity': TextInput(attrs={'placeholder': 'Enter quantity'}),
            'amount_received': TextInput(attrs={'placeholder': 'Enter amount received'}),
            'issue_to': TextInput(attrs={'placeholder': 'Enter issue_to'}),
            'date': TextInput(attrs={'placeholder': 'Enter Exactly Date'}),
        }