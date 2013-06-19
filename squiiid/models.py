from django.db import models

from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile

# Create your models here.

class Profile(UserenaBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='profile')
    #favourite_snack = models.CharField(_('favourite snack'),
    #                                   max_length=5)
                                       
    def __unicode__(self):
        return unicode('')

class SquiiidImage(models.Model):
    image = models.FileField(upload_to='images')
    name = models.CharField(max_length=10000)
    photographer = models.CharField(max_length=10000)
    date = models.DateTimeField()

    def __unicode__(self):
        return unicode('')

class Tag(models.Model):
    image = models.ForeignKey(SquiiidImage)
    url = models.CharField(max_length=10000)
    x = models.IntegerField()
    y = models.IntegerField()
    date = models.DateTimeField()

    def __unicode__(self):
        return unicode('')
    
class Invite(models.Model):
    email = models.CharField(max_length=10000)
    blog_url = models.CharField(max_length=10000)

    def __unicode__(self):
        return unicode('')