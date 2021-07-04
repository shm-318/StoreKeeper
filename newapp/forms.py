from django import forms
from .models import Order,Contact,UserProfileInfo
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields= ('username','email','password')
        widgets={
            'password': forms.TextInput(attrs={'placeholder':'Enter your Password'})
        }

class UserProfileInfoForm(forms.ModelForm):

    class Meta:
        model= UserProfileInfo
        fields = ('profile_pic','StoreName')

class OrderForm(forms.ModelForm):

    class Meta():
        model=Order
        fields= '__all__'

        widgets={
            'item': forms.TextInput(attrs={'placeholder':'Enter the item Name'}),
            'quantity': forms.TextInput(attrs={'placeholder':'Enter the Quantity'})
        }

class ContactForm(forms.ModelForm):
    
    class Meta():
        model=Contact
        fields= '__all__'

        widgets={
            'name': forms.TextInput(attrs={'placeholder':'Enter your name'}),
            'email': forms.TextInput(attrs={'placeholder':'Enter you email'}),
            'message':forms.TextInput(attrs={'placeholder':'Enter you message to be sent'})
        }

