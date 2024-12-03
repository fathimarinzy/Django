"""
URL configuration for djangoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
# from djangoapp import views
from djangoapp.views import *


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # path("first/",views.display),
#     # path("second/",views.display1),
#     path("first/",display),
#     path("second/",display1),
#     path("",show),
# ]

# urlpatterns=[
#     path('admin/', admin.site.urls),
#     path("",include("djangoapp.urls")),
#     # path("secondapp",include("djangoapp2.urls")),


# ]


urlpatterns = [
    path('admin/', admin.site.urls),
 
    path("first/",display),
    path("first1/",display1),
    path("second/",second),
    path("third/",third,name=third),
]
