from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    email=forms.EmailField(required=True)
    role=forms.ChoiceField(choices=[
        ('customer','Customer'),
        ("restaurant_admin","Restaurant Admin"),
    ])
    class Meta:
        model=CustomUser
        fields=['username','email','phone','role','password1','password2']

