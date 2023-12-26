from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User, Profile




class RegisterForm(UserCreationForm):

     username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }), required=True)
     email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control'
    }), required=True)
     password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id':'yourPasssword'
    }), required=True)
     password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control'        
    }), required=True)
     
     class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ProfileForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Full Name", 'class': 'form-control'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={"placeholder":"Bio", 'class': 'form-control'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Phone", 'class': 'form-control'}))

    class Meta:
        model = Profile
        fields = ['full_name', 'image', 'bio', 'phone']