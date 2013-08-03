from django.db import models

class Feeds( models.Model ):
    name = models.CharField( max_length = 130 )
    url = models.CharField( max_length = 200 )

    def __unicode__( self ):
        return self.name
