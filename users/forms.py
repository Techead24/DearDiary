from django import forms
from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model

from django.contrib.auth.forms import  UserCreationForm

# Userr = get_user_model()

class UserRegister(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
