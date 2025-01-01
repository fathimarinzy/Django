from django import forms
from .models import Login,College

class Author(forms.Form):
    name=forms.CharField(max_length=30)
    book_name=forms.CharField(max_length=30)
    price=forms.IntegerField()

class Loginform(forms.ModelForm):
    class Meta:
        model=Login
        fields="__all__"

class Collegeform(forms.ModelForm):
    class Meta:
        model=College
        fields="__all__"

class Home(forms.ModelForm):
    name=forms.CharField(max_length=30,label="enter your name")
    place=forms.CharField(max_length=30,label="enter your place")
    number=forms.IntegerField(label="enter your age")


