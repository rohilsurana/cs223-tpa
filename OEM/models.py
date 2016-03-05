from django.db import models

class User(models.Model):
	age = models.IntegerField()
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

class Course(models.Model):
	faculty = models.CharField(max_length=50)
	description = models.CharField(max_length=1000)


class Question(models.Model):
	problem_statement = models.CharField(max_length=1000)
	marks = models.IntegerField()


class Option(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	text = models.CharField(max_length=500)


class Test(models.Model):
	course = models.CharField(max_length=500)


class Test_result(models.Model):
	result = models.ForeignKey(Test, on_delete=models.CASCADE)
	student = models.CharField(max_length=500)
	marks = models.IntegerField()