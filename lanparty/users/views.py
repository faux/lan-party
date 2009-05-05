from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.core.urlresolvers import reverse
from django import forms

from django.contrib.auth.models import User

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User.objects.create_user(username, email, password)
            return render_to_response('users/signup-completed.html', {
                'form': form,
            })
    else:
        form = SignupForm()

    return render_to_response('users/signup.html', {
        'form': form,
    })

def signin(request):
    return HttpResponse("""
               Cannot sign in yet :(
            """)




class SignupForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput(), max_length=100)
    
    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username__exact=username)
            raise forms.ValidationError("The username has already been taken")
        except User.DoesNotExist:
            pass
        return username
