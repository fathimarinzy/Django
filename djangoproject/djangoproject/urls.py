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


# urlpatterns = [
#     path('admin/', admin.site.urls),
 
#     path("first/",display),
#     path("first1/",display1),
#     path("second/",second),
#     path("third/",third,name="third"),
#     path("forth/",four),
#     path("five/",five),
#     path("six/",six),
#     path("seven/",seven),
#     path("eight/",eight),
#     path("dic/",dic),
#     path("parent",parent),
#     path("child",child),

# ]

# downloded django templtes
urlpatterns=[
    path('admin/', admin.site.urls),
    path("index",index),
    path("child",child),
     
]

#django form case
urlpatterns=[
    path('admin/', admin.site.urls),
    path("form",form,name="form"), 
    path("authorform",authorform,name="authorform"),   
   

]

#model form case
urlpatterns=[
    path('admin/', admin.site.urls),
    path("login/",login,name="login"), 
    path("view/",view,name="view"),
    path("delete_log/<int:id>/",deletes,name="deletes"),  
    path("edit_log/<int:id>/",edit,name="edit"),  
    path("update_log/<int:id>/",updates,name="updates"),  

    path("college",college,name="college"), 
    path("viewcollege",viewcollege,name="viewcollege"), 

]
#modelform with file
from django.conf import settings
from django.conf.urls.static import static


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



#normal from
urlpatterns=[
    path('admin/', admin.site.urls),
    path('employee/',emp,name="emp" ),
    path("views/",viewemp,name="view"),
    path("delete_emp/<int:id>/",delete_emp,name="deletes"),  
    path("edit_emp/<int:id>/",edit_emp,name="editt"),   
    path("update_emp/<int:id>/",update_emp,name="updates"),  

]
      #to connect two table using fk
urlpatterns=[
    path('admin/', admin.site.urls),
    path('authorfm/',authorfm,name="authorfm" ),
    path('author/',author,name="author" ),
    path('price/',price,name="book" ),
    path('price_view/',price_view,name="priceview" ),
    path('pricedelete/<int:id>/',pricedelete,name="book" ),
    path('priceedit/<int:id>/',priceedit,name="book" ),
    path('updateprice/<int:id>/',updateprice,name="book" ),

]

 #image case
urlpatterns=[
    path('admin/', admin.site.urls),
    path('test/',testing,name="test"),

 ]

# session cookie
urlpatterns=[
    path('admin/', admin.site.urls),
    path('setcookie/',setcookie,name='session'),
    path('getcookie/',getcookie,name='session'),
    path('setsession/',setsession,name='session'),
    path('getsession/',getsession,name='session'),
    path('deletesession/',deletesession,name='session'),

 ]
# hw
urlpatterns=[
    path('admin/',admin.site.urls),
    path("authdetail/",authdetail,name='authdetail'),
    path("authors/",authors,name='authors'),
    path("bookname/",book_name,name='bookname'),
    path("detailview/",detailview,name='detailview'),
    path("bookdelete/<int:id>/",bookdelete,name='bookdelete'),
    path("bookedit/<int:id>/",bookedit,name='bookedit'),
    path("bookupdate/<int:id>/",bookupdate,name='bookupdate'),



]
