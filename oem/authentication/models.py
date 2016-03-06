from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User as Main_user


# Create your models here.

class User(models.Model):
    age = models.IntegerField(default=20)
    roll_number = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    date_of_birth = models.DateTimeField()
    owner = models.ForeignKey(Main_user)

    class Meta:
        abstract = True


class Student(User):
    pass


class Faculty(User):
    pass


class Admin(User):
    pass