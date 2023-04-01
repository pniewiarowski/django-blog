from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': r'Username...',
            'class': r'form__text-input',
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': r'Password...',
            'class': 'form__text-input form__text-input--password'
        })
    )
