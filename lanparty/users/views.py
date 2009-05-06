from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from models import *

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User.objects.create_user(username, email, password)
            return render_to_response('users/signup-complete.html', {
                'form': form,
            })
    else:
        form = SignupForm()

    return render_to_response('users/signup.html', {
        'form': form,
        'user': request.user,
    })

def signin(request):
    if request.method == "POST":
        form = SigninForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = form.cleaned_data['user']
            login(request, user)
            return HttpResponse("""
                Signin successful!
            """)
    else:
        form = SigninForm()

    return render_to_response('users/signin.html', {
        'form': form,
        'user': request.user,
    })


def signout(request):
    logout(request)
    return HttpResponse("""
        You have successfuly signed out.
    """)
