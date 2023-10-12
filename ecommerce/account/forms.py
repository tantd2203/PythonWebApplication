from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms


class  CreateUseForm(UserCreationForm) :

    class Meta:

        model = User 
        fields = ['username', 'email','password1', 'password2']
    
    

    def __init__(self, *args , **kwargs) :
        super(CreateUseForm,self).__init__(*args , **kwargs)

    
    #   Validation Email
    def  clean_email(self):

        email = self.changed_data.get("email")

        if User.objects.filter(email=email).exists():
            
            raise forms.ValidationError('This email is invalid')
        
        if len(email >=350) :
            
            raise forms.ValidationError('Your email is too long')
