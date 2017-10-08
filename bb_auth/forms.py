from django import forms
from django.contrib.auth.models import User


def get_field(Model, fieldName):
    return Model._meta.get_field(fieldName)
    
    
class RegisterForm(forms.Form):
    username = forms.CharField(
        label="Username",
        max_length=get_field(User, 'username').max_length,
        widget=forms.TextInput(attrs={'placeholder' : "joebiden"}),
    )
    
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(
            attrs={'placeholder' : "joebiden@example.com"}
        ),
    )
    
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={'placeholder' : "*******"},
        ),
    )
    
    password2 = forms.CharField(
        label="Password (again)",
        widget=forms.PasswordInput(
            attrs={'placeholder' : "*******"},
        ),
    )
    
    