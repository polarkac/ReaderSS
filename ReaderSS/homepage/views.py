from django.shortcuts import render, redirect
from homepage.models import Feeds, AuthForm
import feedparser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django import forms

def index( request ):
    context = { 'title': 'ReaderSS' }

    if request.method == 'POST':
        form = AuthForm( request, request.POST )
        if form.is_valid():
            if form.getUser() is not None:
                redirect( '/' )
    else:
        form = AuthForm( request )

    context['form'] = form;
    context['user'] = request.user

    return render( request, 'homepage/homepage.html', context )

def logout_page( request ):
    if request.user.is_authenticated():
        logout( request )
        return redirect( '/' )
    else:
        return redirect( 'login/' )

def login_page( request ):
    if request.method == 'POST':
        form = AuthForm( request.POST )
        if form.is_valid():
            user = authenticate( username = form.cleaned_data['username'], password = form.cleaned_data['password'] )
            if user is not None:
                login( request, user )
                return redirect( '/' )
    else:
        form = AuthForm()

    context = { 'form': form }

    return render( request, 'homepage/login.html', context )

def register_page( request ):
    context = {'title': 'ReaderSS - Registration'}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()

    context['register_form'] = form;
    return render(request, "homepage/register.html", context )
