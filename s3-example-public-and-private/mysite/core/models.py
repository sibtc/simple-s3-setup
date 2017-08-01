from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

from mysite.storage_backends import PrivateMediaStorage


class Document(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    upload = models.FileField()


class PrivateDocument(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    upload = models.FileField(storage=PrivateMediaStorage())
    user = models.ForeignKey(User, related_name='documents')
