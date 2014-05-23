# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'LifeOccupation.hour_per_week'
        db.add_column('resume_lifeoccupation', 'hour_per_week',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'LifeOccupation.hour_per_week'
        db.delete_column('resume_lifeoccupation', 'hour_per_week')


    models = {
        'resume.city': {
            'Meta': {'object_name': 'City', 'ordering': "('country', 'name')"},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['resume.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40'})
        },
        'resume.country': {
            'Meta': {'object_name': 'Country', 'ordering': "('name',)"},
            'code': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40'})
        },
        'resume.education': {
            'Meta': {'object_name': 'Education'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'life_occupation': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['resume.LifeOccupation']"}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['resume.Place']"})
        },
        'resume.lifeoccupation': {
            'Meta': {'object_name': 'LifeOccupation', 'ordering': "('finished_date', 'name')"},
            'finished_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'hour_per_week': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        'resume.link': {
            'Meta': {'object_name': 'Link'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'resume.place': {
            'Meta': {'object_name': 'Place', 'ordering': "('name',)"},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['resume.City']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['resume.Link']", 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'resume.project': {
            'Meta': {'object_name': 'Project'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'life_occupation': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['resume.LifeOccupation']"}),
            'link': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['resume.Link']", 'blank': 'True'})
        },
        'resume.task': {
            'Meta': {'object_name': 'Task'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'resume.workexperience': {
            'Meta': {'object_name': 'WorkExperience'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'life_occupation': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['resume.LifeOccupation']"}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['resume.Place']"}),
            'task': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['resume.Task']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['resume']