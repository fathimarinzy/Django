from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()


class Teacher(models.Model):
    name=models.CharField(max_length=30)
    course=models.CharField(max_length=30)
    salary=models.FloatField()


class Login(models.Model):
    name=models.CharField(max_length=30)
    course=models.CharField(max_length=30)
    salary=models.FloatField()
class College(models.Model):
    name=models.CharField(max_length=30)
    file=models.FileField(upload_to='media')

#normal form
class Employee(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    age=models.IntegerField()
    place=models.CharField(max_length=255)
