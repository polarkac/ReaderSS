from django.db import models
from django import forms

class Feeds( models.Model ):
    name = models.CharField( max_length = 130 )
    url = models.CharField( max_length = 200 )

    def __unicode__( self ):
        return self.name

class AuthForm( forms.Form ):
    username = forms.CharField( max_length = 30 )
    password = forms.CharField( max_length = 30, widget = forms.PasswordInput() )
