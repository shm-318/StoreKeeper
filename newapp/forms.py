from django import forms
from .models import Order,Contact


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

