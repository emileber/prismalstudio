# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Link'
        db.create_table('resume_link', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('resume', ['Link'])

        # Adding model 'LifeOccupation'
        db.create_table('resume_lifeoccupation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('finished_date', self.gf('django.db.models.fields.DateField')(blank=True, null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('resume', ['LifeOccupation'])

        # Adding model 'Project'
        db.create_table('resume_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('link', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, to=orm['resume.Link'])),
            ('life_occupation', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['resume.LifeOccupation'], unique=True)),
        ))
        db.send_create_signal('resume', ['Project'])

        # Adding model 'Country'
        db.create_table('resume_country', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40, unique=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
        ))
        db.send_create_signal('resume', ['Country'])

        # Adding model 'City'
        db.create_table('resume_city', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40, unique=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['resume.Country'])),
        ))
        db.send_create_signal('resume', ['City'])

        # Adding model 'Place'
        db.create_table('resume_place', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['resume.City'])),
            ('link', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, to=orm['resume.Link'])),
        ))
        db.send_create_signal('resume', ['Place'])

        # Adding model 'Education'
        db.create_table('resume_education', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('life_occupation', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['resume.LifeOccupation'], unique=True)),
            ('place', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['resume.Place'])),
        ))
        db.send_create_signal('resume', ['Education'])

        # Adding model 'Task'
        db.create_table('resume_task', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('resume', ['Task'])

        # Adding model 'WorkExperience'
        db.create_table('resume_workexperience', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('life_occupation', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['resume.LifeOccupation'], unique=True)),
            ('place', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['resume.Place'])),
        ))
        db.send_create_signal('resume', ['WorkExperience'])

        # Adding M2M table for field task on 'WorkExperience'
        m2m_table_name = db.shorten_name('resume_workexperience_task')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('workexperience', models.ForeignKey(orm['resume.workexperience'], null=False)),
            ('task', models.ForeignKey(orm['resume.task'], null=False))
        ))
        db.create_unique(m2m_table_name, ['workexperience_id', 'task_id'])


    def backwards(self, orm):
        # Deleting model 'Link'
        db.delete_table('resume_link')

        # Deleting model 'LifeOccupation'
        db.delete_table('resume_lifeoccupation')

        # Deleting model 'Project'
        db.delete_table('resume_project')

        # Deleting model 'Country'
        db.delete_table('resume_country')

        # Deleting model 'City'
        db.delete_table('resume_city')

        # Deleting model 'Place'
        db.delete_table('resume_place')

        # Deleting model 'Education'
        db.delete_table('resume_education')

        # Deleting model 'Task'
        db.delete_table('resume_task')

        # Deleting model 'WorkExperience'
        db.delete_table('resume_workexperience')

        # Removing M2M table for field task on 'WorkExperience'
        db.delete_table(db.shorten_name('resume_workexperience_task'))


    models = {
        'resume.city': {
            'Meta': {'ordering': "('country', 'name')", 'object_name': 'City'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['resume.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40', 'unique': 'True'})
        },
        'resume.country': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Country'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40', 'unique': 'True'})
        },
        'resume.education': {
            'Meta': {'object_name': 'Education'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'life_occupation': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['resume.LifeOccupation']", 'unique': 'True'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['resume.Place']"})
        },
        'resume.lifeoccupation': {
            'Meta': {'ordering': "('finished_date', 'name')", 'object_name': 'LifeOccupation'},
            'finished_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
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
            'Meta': {'ordering': "('name',)", 'object_name': 'Place'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['resume.City']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['resume.Link']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'resume.project': {
            'Meta': {'object_name': 'Project'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'life_occupation': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['resume.LifeOccupation']", 'unique': 'True'}),
            'link': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['resume.Link']"})
        },
        'resume.task': {
            'Meta': {'object_name': 'Task'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'resume.workexperience': {
            'Meta': {'object_name': 'WorkExperience'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'life_occupation': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['resume.LifeOccupation']", 'unique': 'True'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['resume.Place']"}),
            'task': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['resume.Task']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['resume']