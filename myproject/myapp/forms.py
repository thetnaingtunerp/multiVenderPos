from django import forms
from .models import *


class ULoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())


class AdminLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())


# class messengerbotform(forms.ModelForm):
#     class Meta:
#         model = messengerbot
#         fields = ['message']
#         widgets ={
#             'message':forms.Textarea(attrs={'placeholder':'Type Message'})
#         }

class itemcreateform(forms.ModelForm):
    class Meta:
        model = product
        fields = ['name', 'saleprice', 'purchaseprice']
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control', 'required':'True'}),
            'saleprice' : forms.NumberInput(attrs={'class': 'form-control'}),
            'purchaseprice' : forms.NumberInput(attrs={'class': 'form-control'}),
            
        }