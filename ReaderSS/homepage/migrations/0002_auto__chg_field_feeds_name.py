# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Feeds.name'
        db.alter_column(u'homepage_feeds', 'name', self.gf('django.db.models.fields.CharField')(max_length=130))

    def backwards(self, orm):

        # Changing field 'Feeds.name'
        db.alter_column(u'homepage_feeds', 'name', self.gf('django.db.models.fields.CharField')(max_length=150))

    models = {
        u'homepage.feeds': {
            'Meta': {'object_name': 'Feeds'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '130'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['homepage']