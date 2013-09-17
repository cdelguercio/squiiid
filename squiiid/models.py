import uuid

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile

import logging
logger = logging.getLogger('squiiid.errors')

class Profile(UserenaBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='profile')
    website = models.CharField(max_length=1000, null=True, blank=True)
                                       
    def __unicode__(self):
        return unicode('')

def name_file(instance, filename):
    try:
        img_ext = filename.split('.')[-1]
        img_name = str(uuid.uuid4()) + '.' + img_ext
        logger.info('saving...')
        logger.info('/'.join(['images', img_name]))
        logger.info(instance)
        return '/'.join(['images', img_name])
    except Exception as e:
        logger.info(e)
    #logger.info('/'.join(['images', img_name]))
    return None
    

class SquiiidImage(models.Model):
    profile = models.ForeignKey(Profile)
    image = models.ImageField(upload_to=name_file)
    image_1 = models.FileField(upload_to='images/', null=True, blank=True)
    image_2 = models.FileField(upload_to='images/', null=True, blank=True)
    likes = models.IntegerField(default=0)
    clicks = models.IntegerField(default=0)
    hovers = models.IntegerField(default=0)
    reblogs = models.IntegerField(default=0)
    title = models.CharField(max_length=300, null=True, blank=True)
    tags = models.CharField(max_length=1000, null=True, blank=True)
    contributor_type_1 = models.CharField(max_length=100, null=True, blank=True)
    contributor_type_2 = models.CharField(max_length=100, null=True, blank=True)
    contributor_type_3 = models.CharField(max_length=100, null=True, blank=True)
    contributor_type_4 = models.CharField(max_length=100, null=True, blank=True)
    contributor_type_5 = models.CharField(max_length=100, null=True, blank=True)
    contributor_name_1 = models.CharField(max_length=100, null=True, blank=True)
    contributor_name_2 = models.CharField(max_length=100, null=True, blank=True)
    contributor_name_3 = models.CharField(max_length=100, null=True, blank=True)
    contributor_name_4 = models.CharField(max_length=100, null=True, blank=True)
    contributor_name_5 = models.CharField(max_length=100, null=True, blank=True)
    street_address_1 = models.CharField(max_length=300, null=True, blank=True)
    street_address_2 = models.CharField(max_length=300, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    zip_code = models.CharField(max_length=100, null=True, blank=True)
    place = models.CharField(max_length=300, null=True, blank=True)
    tool = models.CharField(max_length=300, null=True, blank=True)
    iso = models.CharField(max_length=100, null=True, blank=True)
    aperture = models.CharField(max_length=100, null=True, blank=True)
    exposure = models.CharField(max_length=100, null=True, blank=True)
    focal_length = models.CharField(max_length=100, null=True, blank=True)
    private = models.BooleanField(default=False)
    brand_1 = models.CharField(max_length=300, null=True, blank=True)
    brand_2 = models.CharField(max_length=300, null=True, blank=True)
    brand_3 = models.CharField(max_length=300, null=True, blank=True)
    brand_4 = models.CharField(max_length=300, null=True, blank=True)
    brand_5 = models.CharField(max_length=300, null=True, blank=True)
    product_1 = models.CharField(max_length=300, null=True, blank=True)
    product_2 = models.CharField(max_length=300, null=True, blank=True)
    product_3 = models.CharField(max_length=300, null=True, blank=True)
    product_4 = models.CharField(max_length=300, null=True, blank=True)
    product_5 = models.CharField(max_length=300, null=True, blank=True)
    product_url_1 = models.CharField(max_length=300, null=True, blank=True)
    product_url_2 = models.CharField(max_length=300, null=True, blank=True)
    product_url_3 = models.CharField(max_length=300, null=True, blank=True)
    product_url_4 = models.CharField(max_length=300, null=True, blank=True)
    product_url_5 = models.CharField(max_length=300, null=True, blank=True)
    date = models.DateTimeField()

    def __unicode__(self):
        return unicode('')

class Tag(models.Model):
    image = models.ForeignKey(SquiiidImage)
    phrase = models.CharField(max_length=1000)
    date = models.DateTimeField()

    def __unicode__(self):
        return unicode('')
    
class Invite(models.Model):
    email = models.CharField(max_length=1000)
    blog_url = models.CharField(max_length=1000)
    name = models.CharField(max_length=1000)

    def __unicode__(self):
        return unicode('')