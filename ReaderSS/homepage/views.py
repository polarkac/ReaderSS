from django.shortcuts import render, redirect
from homepage.models import Feeds, AuthForm, RegisterForm
import feedparser
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView

class HomeIndexView( TemplateView ):
    template_name = 'homepage/homepage.html'

    def get_context_data( self, request, **kwargs ):
        context = super( HomeIndexView, self).get_context_data( **kwargs )
        context['title'] = 'ReaderSS'
        context['form'] = AuthForm( request, request.POST )
        context['user'] = request.user

        return context

    def get( self, request, *args, **kwargs ):
        return self.render_to_response( self.get_context_data( request, **kwargs ) )

    def post( self, request, *args, **kwargs ):
        context = self.get_context_data( request, **kwargs )
        form = context['form']
        if form.is_valid() and form.getUser() is not None:
            return redirect( '/' )

        return self.render_to_response( context )

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

    def get_context_data( self, request, **kwargs ):
        context = super( HomeRegisterView, self ).get_context_data( request, **kwargs )
        context['register_form'] = RegisterForm( request, request.POST )

        return context

    def get( self, request, *args, **kwargs ):
        return self.render_to_response( self.get_context_data( request, **kwargs ) )

    def post( self, request, *args, **kwargs ):
        context = self.get_context_data( request, **kwargs )
        form = context['register_form']
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect( "/" )

        return self.render_to_response( context )
