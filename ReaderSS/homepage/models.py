from django.db import models
from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

class Feeds( models.Model ):
    name = models.CharField( max_length = 130 )
    url = models.CharField( max_length = 200 )
    user = models.ForeignKey( User )

    class Meta:
        verbose_name = ( 'Feeds' )
        verbose_name_plural = ( 'Feeds' )

    def __unicode__( self ):
        return self.name

class AuthForm( forms.Form ):
    request = None
    user = None
    username = forms.CharField( max_length = 30 )
    password = forms.CharField( max_length = 30, widget = forms.PasswordInput() )

    def __init__( self, argRequest = None, *args, **kwargs ):
        self.request = argRequest;
        if 'login' in self.request.POST:
            super( AuthForm, self ).__init__( *args, **kwargs )
        else:
            super( AuthForm, self ).__init__()

    def clean( self ):
        if not self.is_valid():
            return self.cleaned_data
        cleanedUsername = self.cleaned_data['username']
        cleanedPassword = self.cleaned_data['password']

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

class RegisterForm( forms.ModelForm ):
    username = forms.RegexField( max_length = 30,
            regex=r'^[\w.@+-]+$' )
    password = forms.CharField( min_length = 6, widget = forms.PasswordInput() )
    passwordVer = forms.CharField( min_length = 6, widget = forms.PasswordInput() )

    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__( self, argRequest = None, *args, **kwargs ):
        self.request = argRequest;
        if 'register' in self.request.POST:
            super( RegisterForm, self ).__init__( *args, **kwargs )
        else:
            super( RegisterForm, self ).__init__()
            
    def clean_register_username( self ):
        username = self.cleaned_data['username']
        try:
            User.objects.get( username = username )
        except User.DoesNotExist:
            return username
        
        raise forms.ValidationError( 'Duplicate username.', code = 'duplicate_username' )

    def clean_register_passwordVer( self ):
        pass1 = self.cleaned_data['password']
        pass2 = self.cleaned_data['passwordVer']

        if pass1 and pass2 and pass1 != pass2:
            raise forms.ValidationError( 'Passwords do not match.', code = 'wrong_passwords' )

        return pass1

    def save( self ):
        user = super( RegisterForm, self ).save( commit = False )
        user.set_password( self.cleaned_data['password'] )

        user.save()
        return user
