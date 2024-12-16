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

#    to connect two table using fk
class Author(models.Model):
    name=models.CharField(max_length=30)
    phone=models.IntegerField()
    email=models.EmailField()
class Book(models.Model):
    Author_id=models.ForeignKey(Author,on_delete=models.CASCADE)
    price=models.IntegerField()
  

# image case
class Testing(models.Model):
    image_lawn=models.ImageField(upload_to="image")
    phone=models.IntegerField()


# hw
class Authors(models.Model):
    author_name=models.CharField(max_length=30)
    language=models.CharField(max_length=30)
    published_year=models.IntegerField()

class Books(models.Model):
    auth_id=models.ForeignKey(Authors,on_delete=models.CASCADE)
    book_name=models.CharField(max_length=30)




