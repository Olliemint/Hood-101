from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile

# register form

class Register_Form(UserCreationForm):
    
    
    class Meta:
        model = User
        fields =['first_name','username', 'email', 'password1', 'password2']


class UserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = User
        fields = ('username', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
       model = Profile
       fields = '__all__'
       exclude = ['username']      