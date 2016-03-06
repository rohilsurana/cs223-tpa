from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=50)
    faculty = models.ForeignKey(User, limit_choices_to={'is_staff': True})
    description = models.TextField()

    def __str__(self):
        return self.name


class Test(models.Model):
    course = models.ForeignKey(Course)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def authenticate_student_user(self,user):
        if(hasattr(user,'Student')):
            for c in user.Student.courses:
                if c == self.course:
                    return True
            return False
        else:
            return False
        

class TestResult(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    student = models.ForeignKey(User)
    marks = models.FloatField()

    def __str__(self):
        return str(self.marks)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    marks = models.IntegerField(default=2)
    test = models.ForeignKey(Test)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_text