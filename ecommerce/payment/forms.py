

from . models import ShippingAddress

from django import forms

#Shipping Address

class ShippingForm(forms.ModelForm):
    
    class Meta:

        model = ShippingAddress
        
        fields= ['full_name', 'email','address','city']

        exclude = ['user',]