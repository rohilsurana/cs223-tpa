import datetime

from django.db import models
from django.utils import timezone
from django import forms

# Create your models here.

class User(models.Model):
	age = models.IntegerField(default=20)
	id = models.CharField(max_length=50, primary_key=True)
	name = models.CharField(max_length=50)
	address = models.CharField(max_length=100)
	email = models.CharField(max_length=50)
	DOB = models.DateTimeField('ate of birth')
	owner = models.ForeignKey('auth.User')
	class Meta:
		abstract = True

class Student(User):
	pass

class Faculty(User):
	pass

class Admin(User):
	pass

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	marks = models.IntegerField(default=2)

	def __str__(self):
		return self.question_text

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text	


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your Name', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput())


