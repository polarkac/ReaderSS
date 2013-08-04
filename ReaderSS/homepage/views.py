from django.shortcuts import render, redirect
from homepage.models import Feeds, AuthForm
import feedparser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def index( request ):
    feeds = Feeds.objects.all()
    parsedFeeds = dict() 
    for f in feeds:
        parsedFeeds[ f.name ] = feedparser.parse( f.url )
    context = { 'title': 'ReaderSS', 'feeds': parsedFeeds, 'user': request.user }

    if request.method == 'POST':
        form = AuthForm( request.POST )
        if form.is_valid():
            user = authenticate( username = form.cleaned_data['username'], password = form.cleaned_data['password'] )
            if user is not None:
                login( request, user )
                return redirect( '/' )
    else:
        form = AuthForm()

    context['form'] = form;

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

