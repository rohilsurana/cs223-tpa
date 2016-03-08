from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User as Main_user
from exam.models import Course


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    class Meta:
        abstract = True


class Student(User):
    user = models.OneToOneField(Main_user, limit_choices_to={'is_staff': False})
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.user.username


class Faculty(User):
    user = models.OneToOneField(Main_user, limit_choices_to={'is_staff': True})
    
    def __str__(self):
        return self.name
        # return "Faculty" + str(self.id) + "-" + str(self.name)


class Admin(User):
    user = models.OneToOneField(Main_user, limit_choices_to={'is_superuser': True})
    pass