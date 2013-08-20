from django.shortcuts import render, redirect
from homepage.models import Feeds, AuthForm, RegisterForm
import feedparser
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView

class HomeIndexView( TemplateView ):
    templateName = 'homepage/homepage.html'
    context = { 'title': 'ReaderSS' }

    def get( self, request, *args, **kwargs ):
        self.context['form'] = AuthForm( request )
        self.context['user'] = request.user
        return render( request, self.templateName, self.context )

    def post( self, request, *args, **kwargs ):
        form = AuthForm( request, request.POST )
        self.context['form'] = form
        self.context['user'] = request.user
        if form.is_valid() and form.getUser() is not None:
            return redirect( '/' )
        else:
            return render( request, self.templateName, self.context )

class HomeLoginView( HomeIndexView ):
    templateName = 'homepage/login.html'

class HomeLogoutView( TemplateView ):

    def get( self, request, *args, **kwargs ):
        if request.user.is_authenticated():
            logout( request )
            return redirect( '/' )
        else:
            return redirect( 'login/' )

class HomeRegisterView( TemplateView ):
    templateName = 'homepage/register.html'
    context = { 'title': 'ReaderSS - Registration' }

    def get( self, request, *args, **kwargs ):
        form = RegisterForm()
        self.context['register_form'] = form
        return render( request, self.templateName, self.context )

    def post( self, request, *args, **kwargs ):
        form = RegisterForm( request.POST )
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect( "/" )

        self.context['register_form'] = form;
        return render( request, self.templateName, self.context )
