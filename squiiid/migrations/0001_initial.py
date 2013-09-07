# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Profile'
        db.create_table(u'squiiid_profile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mugshot', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('privacy', self.gf('django.db.models.fields.CharField')(default='registered', max_length=15)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(related_name='profile', unique=True, to=orm['auth.User'])),
            ('website', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True)),
        ))
        db.send_create_signal(u'squiiid', ['Profile'])

        # Adding model 'SquiiidImage'
        db.create_table(u'squiiid_squiiidimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['squiiid.Profile'])),
            ('image', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('image_1', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('image_2', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('likes', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('clicks', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('hovers', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('reblogs', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('tags', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True)),
            ('contributor_type_1', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('contributor_type_2', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('contributor_type_3', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('contributor_type_4', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('contributor_type_5', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('contributor_name_1', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('contributor_name_2', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('contributor_name_3', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('contributor_name_4', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('contributor_name_5', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('street_address_1', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('street_address_2', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('place', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('tool', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('iso', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('aperture', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('exposure', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('focal_length', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('private', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('brand_1', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('brand_2', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('brand_3', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('brand_4', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('brand_5', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('product_1', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('product_2', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('product_3', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('product_4', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('product_5', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('product_url_1', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('product_url_2', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('product_url_3', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('product_url_4', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('product_url_5', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'squiiid', ['SquiiidImage'])

        # Adding model 'Tag'
        db.create_table(u'squiiid_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['squiiid.SquiiidImage'])),
            ('phrase', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'squiiid', ['Tag'])

        # Adding model 'Invite'
        db.create_table(u'squiiid_invite', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('blog_url', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1000)),
        ))
        db.send_create_signal(u'squiiid', ['Invite'])


    def backwards(self, orm):
        # Deleting model 'Profile'
        db.delete_table(u'squiiid_profile')

        # Deleting model 'SquiiidImage'
        db.delete_table(u'squiiid_squiiidimage')

        # Deleting model 'Tag'
        db.delete_table(u'squiiid_tag')

        # Deleting model 'Invite'
        db.delete_table(u'squiiid_invite')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'squiiid.invite': {
            'Meta': {'object_name': 'Invite'},
            'blog_url': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1000'})
        },
        u'squiiid.profile': {
            'Meta': {'object_name': 'Profile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mugshot': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'privacy': ('django.db.models.fields.CharField', [], {'default': "'registered'", 'max_length': '15'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'profile'", 'unique': 'True', 'to': u"orm['auth.User']"}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'})
        },
        u'squiiid.squiiidimage': {
            'Meta': {'object_name': 'SquiiidImage'},
            'aperture': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'brand_1': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'brand_2': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'brand_3': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'brand_4': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'brand_5': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'clicks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'contributor_name_1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'contributor_name_2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'contributor_name_3': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'contributor_name_4': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'contributor_name_5': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'contributor_type_1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'contributor_type_2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'contributor_type_3': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'contributor_type_4': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'contributor_type_5': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'exposure': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'focal_length': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'hovers': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'image_1': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'image_2': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'iso': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'likes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'private': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'product_1': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'product_2': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'product_3': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'product_4': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'product_5': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'product_url_1': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'product_url_2': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'product_url_3': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'product_url_4': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'product_url_5': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['squiiid.Profile']"}),
            'reblogs': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'street_address_1': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'street_address_2': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'tool': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'squiiid.tag': {
            'Meta': {'object_name': 'Tag'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['squiiid.SquiiidImage']"}),
            'phrase': ('django.db.models.fields.CharField', [], {'max_length': '1000'})
        }
    }

    complete_apps = ['squiiid']