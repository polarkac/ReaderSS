from django.shortcuts import render
from homepage.models import Feeds
import feedparser

def index( request ):
    feeds = Feeds.objects.all()
    parsedFeeds = dict() 
    for f in feeds:
        parsedFeeds[ f.name ] = feedparser.parse( f.url )
    context = { 'title': 'ReaderSS', 'feeds': parsedFeeds }
    return render( request, 'homepage/homepage.html', context )

