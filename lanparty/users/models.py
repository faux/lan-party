from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class SigninForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(render_value=False), max_length=100)
    
    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if not user.is_active:
                raise forms.ValidationError("The account is disabled")
            else:
                self.cleaned_data['user'] = user
        else:
            raise forms.ValidationError("The username or password is incorrect")
        return self.cleaned_data

class SignupForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput(render_value=False), max_length=100)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username__exact=username)
            raise forms.ValidationError("The username has already been taken")
        except User.DoesNotExist:
            pass
        return username

