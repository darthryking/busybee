from django import forms
from django.contrib.auth.models import User


def get_field(Model, fieldName):
    return Model._meta.get_field(fieldName)
    
    
def username_validator(username):
    if User.objects.filter(username__iexact=username).exists():
        raise forms.ValidationError("Username already exists!")
        
        
class RegisterForm(forms.Form):
    username = forms.CharField(
        label="Username",
        max_length=get_field(User, 'username').max_length,
        validators=[username_validator],
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
    
    def clean(self):
        super().clean()
        
        password1 = self.cleaned_data['password1']
        if password1 != self.cleaned_data['password2']:
            self.add_error('password1', "Passwords don't match!")
            
            