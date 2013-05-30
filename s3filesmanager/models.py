import os
from uuid import uuid4

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel


def get_random_filename(instance, file_name):
    ext = file_name.split('.')[-1]
    file_name = '%s.%s' % (str(uuid4()), ext)
    file_path = '%s/' % instance.owner
    return os.path.join(file_path, file_name)


class S3File(TimeStampedModel):
    owner = models.ForeignKey(User, verbose_name=_(u'Owner'))
    file_name = models.CharField(max_length=255, verbose_name=_(u'File Name'))
    file_size = models.PositiveIntegerField(verbose_name=_(u'File Size'))
    s3_file = models.FileField(verbose_name=_(u'File'), upload_to=get_random_filename)
    thumbnail_url = models.URLField(verbose_name=_(u'Thumbnail Url'))
