from django.db import models
from django import forms
from django.contrib.auth import authenticate, login

class Feeds( models.Model ):
    name = models.CharField( max_length = 130 )
    url = models.CharField( max_length = 200 )

    def __unicode__( self ):
        return self.name

class AuthForm( forms.Form ):
    request = None
    user = None
    username = forms.CharField( max_length = 30 )
    password = forms.CharField( max_length = 30, widget = forms.PasswordInput() )

    def __init__( self, argRequest = None, *args, **kwargs ):
        self.request = argRequest;
        super( AuthForm, self ).__init__( *args, **kwargs )

    def clean( self ):
        cleanedUsername = self.cleaned_data['username']
        cleanedPassword = self.cleaned_data['password']

        if cleanedUsername and cleanedPassword:
            self.user = authenticate( username = cleanedUsername, password = cleanedPassword )
            if self.user is None:
                raise forms.ValidationError( 'Invalid username or password.', 
                    code = 'invalid_login' )
            else:
                self.loginUser()

        return self.cleaned_data

    def loginUser( self ):
        login( self.request, self.user )

    def getUser( self ):
        return self.user
