from django.shortcuts import render, redirect
from homepage.models import Feeds, AuthForm, RegisterForm
import feedparser
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView

class HomeIndexView( TemplateView ):
    template_name = 'homepage/homepage.html'
    context = { 'title': 'ReaderSS' }

    def get( self, request, *args, **kwargs ):
        self.context['form'] = AuthForm( request, request.POST )
        self.context['user'] = request.user
        return self.render_to_response( self.context )

    def post( self, request, *args, **kwargs ):
        form = AuthForm( request, request.POST )
        self.context['form'] = form
        if form.is_valid() and form.getUser() is not None:
            return redirect( '/' )

        self.context['user'] = request.user
        return self.render_to_response( self.context )

class HomeLoginView( HomeIndexView ):
    template_name = 'homepage/login.html'

class HomeLogoutView( TemplateView ):

    def get( self, request, *args, **kwargs ):
        if request.user.is_authenticated():
            logout( request )
            return redirect( '/' )
        else:
            return redirect( 'login/' )

class HomeRegisterView( HomeIndexView ):
    template_name = 'homepage/register.html'
    context = { 'title': 'ReaderSS - Registration' }

    def get( self, request, *args, **kwargs ):
        super( HomeRegisterView, self).get( request, *args, **kwargs )
        form = RegisterForm()
        self.context['register_form'] = form
        return self.render_to_response( self.context )

    def post( self, request, *args, **kwargs ):
        super( HomeRegisterView, self).post( request, *args, **kwargs )
        form = RegisterForm( request.POST )
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect( "/" )

        self.context['register_form'] = form;
        return self.render_to_response( self.context )
