from django.db import models
from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

class Feeds( models.Model ):
    name = models.CharField( max_length = 130 )
    url = models.CharField( max_length = 200 )
    user = models.OneToOneField( User )

    def __unicode__( self ):
        return self.name

class AuthForm( forms.Form ):
    request = None
    user = None
    username = forms.CharField( min_length = 1, max_length = 30 )
    password = forms.CharField( min_length = 1, max_length = 30, widget = forms.PasswordInput() )

    def __init__( self, argRequest = None, *args, **kwargs ):
        self.request = argRequest;
        if 'login' in self.request.POST:
            super( AuthForm, self ).__init__( *args, **kwargs )
        else:
            super( AuthForm, self ).__init__()

    def clean( self ):
        cleanedUsername = None
        cleanedPassword = None
        if 'username' in self.cleaned_data and 'password' in self.cleaned_data:
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

class RegisterForm( forms.ModelForm ):
    register_username = forms.RegexField( max_length = 30,
            regex=r'^[\w.@+-]+$' )
    register_password = forms.CharField( min_length = 6, widget = forms.PasswordInput() )
    register_passwordVer = forms.CharField( min_length = 6, widget = forms.PasswordInput() )

    class Meta:
        model = User
        fields = ('register_username', 'register_password')

    def clean_username( self ):
        username = self.cleaned_data['register_username']
        try:
            User.objects.get( username = username )
        except User.DoesNotExist:
            return username
        
        raise forms.ValidationError( 'Duplicate username.', code = 'duplicate_username' )

    def clean_passwordVer( self ):
        pass1 = self.cleaned_data['register_password']
        pass2 = self.cleaned_data['register_passwordVer']

        if pass1 and pass2 and pass1 != pass2:
            raise forms.ValidationError( 'Passwords do not match.', code = 'wrong_passwords' )

        return pass1

    def save( self ):
        user = super( RegisterForm, self ).save( commit = False )
        user.set_password( self.cleaned_data['register_password'] )

        user.save()
        return user
