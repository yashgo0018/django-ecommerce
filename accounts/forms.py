from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

User = get_user_model()


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'class': 'form-control my-2',
            'placeholder': 'Username'
        }
    ))

    password = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control my-2',
            'placeholder': 'Password'
        }
    ))


class RegisterForm(forms.Form):
    firstname = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'class': 'form-control my-2',
            'placeholder': 'First Name'
        }
    ))

    lastname = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'class': 'form-control my-2',
            'placeholder': 'Last Name'
        }
    ))

    email = forms.EmailField(label='', widget=forms.EmailInput(
        attrs={
            'class': 'form-control my-2',
            'placeholder': 'Email'
        }
    ))

    username = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'class': 'form-control my-2',
            'placeholder': 'Username'
        }
    ))

    password = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control my-2',
            'placeholder': 'Password'
        }
    ))

    password2 = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control my-2',
            'placeholder': 'Confirm Password'
        }
    ))

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        super().__init__(*args, **kwargs)

    def clean(self):
        data = self.cleaned_data
        password = data.get("password")
        password2 = data.get("password2")
        if password != password2:
            raise forms.ValidationError("Password doesn't match")
        else:
            return data

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username Already Taken")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email Already Taken")
        return email

    def register_user(self):
        username = self.cleaned_data["username"]
        password = self.cleaned_data["password"]
        firstname = self.cleaned_data["firstname"]
        lastname = self.cleaned_data["lastname"]
        email = self.cleaned_data["email"]
        user = User.objects.create_user(username, email, password)
        user.last_name = lastname
        user.first_name = firstname
        user.save()
        return user
