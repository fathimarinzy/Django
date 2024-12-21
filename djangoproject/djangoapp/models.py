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


class Students(models.Model):
    std_name=models.CharField(max_length=30)
    course=models.CharField(max_length=30)
    place=models.CharField(max_length=30)
    age=models.IntegerField()
    phone=models.IntegerField()
    email=models.EmailField()

class Marks(models.Model):
    std_id=models.ForeignKey(Students,on_delete=models.CASCADE)
    mark=models.IntegerField()

class Teachers(models.Model):
    name=models.CharField(max_length=30)
    sub=models.CharField(max_length=30)

class Department(models.Model):
    tchr_id=models.ForeignKey(Teachers,on_delete=models.CASCADE)
    dept_name=models.CharField(max_length=30)



class Loginpage(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=128)