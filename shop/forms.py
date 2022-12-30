from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from shop.models import ContactUs
 

 
class UserRegisterForm(UserCreationForm):
    username = forms.EmailField(widget = forms.TextInput(attrs={'type': 'Email', 'class': 'form-control','placeholder':'Email'}))
    # email = forms.EmailField(widget = forms.TextInput(attrs={'type': 'text', 'class': 'form-control','placeholder':'Email'}))
    phone_no = forms.CharField(max_length = 20,widget = forms.NumberInput(attrs={'type': 'tel', 'class': 'form-control','placeholder':'Phone'}))
    first_name = forms.CharField(max_length = 20,widget = forms.TextInput(attrs={'type': 'text', 'class': 'form-control','placeholder':'First Name'}))
    last_name = forms.CharField(max_length = 20,widget = forms.TextInput(attrs={'type': 'text', 'class': 'form-control','placeholder':'Last Name'}))
    password1 = forms.CharField(max_length = 20,widget = forms.PasswordInput(attrs={'type': 'password', 'class': 'form-control','placeholder':'Password'}))
    password2 = forms.CharField(max_length = 20,widget = forms.PasswordInput(attrs={'type': 'password', 'class': 'form-control','placeholder':'Confirm Password'}),label='')
    class Meta:
        model = User
        def __init__(self, *args, **kwargs):
            super(UserRegisterForm, self).__init__(*args, **kwargs)
            self.fields['password2'].label = ""
        fields = ['username', 'phone_no', 'password1', 'password2']
class ContactUsForm(forms.ModelForm):
    Name = forms.CharField(widget = forms.TextInput(attrs={'type': 'text','placeholder':'Name'}))
    Subject = forms.CharField(widget = forms.TextInput(attrs={'type': 'text', 'placeholder':'Subject'}))
    Email = forms.EmailField(widget = forms.TextInput(attrs={'type': 'email','placeholder':'Email'}))
    Phone = forms.CharField(widget = forms.NumberInput(attrs={'type': 'text', 'placeholder':'Phone', "name":"telephone",'id':"telephone_input"}))
    Subject = forms.CharField(max_length = 20,widget = forms.NumberInput(attrs={'type': 'text', 'placeholder':'Subject'}))
    Chat = forms.CharField(max_length = 6000,widget = forms.Textarea(attrs={'type': 'text', 'placeholder':'Message',"cols":"30" ,"rows":"5" }))
    class Meta:
        model = ContactUs
        fields = ['Name', 'Subject', 'Email', 'Phone', 'Chat','Subject']

