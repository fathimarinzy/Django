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
