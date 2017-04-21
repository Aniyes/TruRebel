from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Person(AbstractUser):

    REQUIRED_FIELDS = ['gram_name',
                       'website',
                       'snap_name',
                       'email',
                       ]

    gram_name = models.CharField(max_length=20)
    snap_name = models.CharField(max_length=20)
    website = models.CharField(max_length=20)

