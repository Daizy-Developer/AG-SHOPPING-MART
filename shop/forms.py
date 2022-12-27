from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
 

 
class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget = forms.TextInput(attrs={'type': 'text', 'class': 'form-control','placeholder':'Username'}))
    email = forms.EmailField(widget = forms.TextInput(attrs={'type': 'text', 'class': 'form-control','placeholder':'Email'}))
    phone_no = forms.CharField(max_length = 20,widget = forms.NumberInput(attrs={'type': 'tel', 'class': 'form-control','placeholder':'Phone'}))
    first_name = forms.CharField(max_length = 20,widget = forms.TextInput(attrs={'type': 'text', 'class': 'form-control','placeholder':'First Name'}))
    last_name = forms.CharField(max_length = 20,widget = forms.TextInput(attrs={'type': 'text', 'class': 'form-control','placeholder':'Last Name'}))
    password1 = forms.CharField(max_length = 20,widget = forms.PasswordInput(attrs={'type': 'password', 'class': 'form-control','placeholder':'Password'}))
    password2 = forms.CharField(max_length = 20,widget = forms.PasswordInput(attrs={'type': 'password', 'class': 'form-control','placeholder':'Confirm Password'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_no', 'password1', 'password2']