from django import forms
from .models import Login

class Author(forms.Form):
    name=forms.CharField(max_length=30)
    book_name=forms.CharField(max_length=30)
    price=forms.IntegerField()

class Loginform(forms.ModelForm):
    class Meta:
        model=Login
        fields="__all__"
