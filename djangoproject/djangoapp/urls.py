from django.urls import path
from djangoapp.views import *


urlpatterns=[
    path("first",display),
    path("",show)
]