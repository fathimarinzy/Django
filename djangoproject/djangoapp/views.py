from django.shortcuts import render,HttpResponse,redirect
from .forms import Author,Loginform,Collegeform
from .models import Login,College,Employee

# Create your views here.
def display(request):
    return HttpResponse("welcome to django")


def display1(request):
    return HttpResponse("haiiiii")


def show(request):
    return HttpResponse("<i>haiiiii<i>")

def second(request):
    return redirect("third")


def third(request):
    return render (request,"one.html")


def four(request):
    a="python"
    b="django"
    return render (request,"two.html",{"data":a,"view":b})
# if case
def five(request):
    a="python"
    b="django"
    c=""
    return render (request,"two.html",{"data":a,"view":b,"value":c})

def six(request):
    a=2
    b="django"
    c=""
    return render (request,"two.html",{"data":a,"view":b,"value":c})

def seven(request):
    a=2
    b=1
    c=[10,20,30]
    return render (request,"two.html",{"data":a,"view":b,"value":c})

def eight(request):
    a=2
    b=1
    c={"name":"ammu","course":"python"}
    return render (request,"two.html",{"data":a,"view":b,"value":c})

def dic(request):
    a=2
    b=1
    c={"name":"ammu","course":"python","age":20}
    return render (request,"dic1.html",{"data":a,"view":b,"value":c})

def parent(request):
    return render (request,"parent.html")

def child(request):
  
    return render (request,"child.html")


# downloded django templtes
def index(request):
    return render (request,"index.html")


#django form case
def form(request):
    x=Author()
    return render (request,"form.html",{"data":x})

# def authorform(request):
#     if request.method=="POST":
#         return HttpResponse("worked")
#     else:
#         x=Author()
#         return render (request,"form1.html",{"data":x})

# def authorform(request):
#     if request.method=="POST":
#        z=Author(request.POST)
#        print(z)
#        return HttpResponse("worked")

#     else:
#         x=Author()
#         return render (request,"form1.html",{"data":x})

# def authorform(request):
#     if request.method=="POST":
#        z=Author(request.POST)
#     #    print(z)
#         if z.is_valid():
#              y=z.cleaned_data
#              print(y)
#              print("working")
#              return HttpResponse("worked")

#     else:
#         x=Author()
#         return render (request,"form1.html",{"data":x})


def authorform(request):
    if request.method=="POST":
       z=Author(request.POST)
    #    print(z)
       if z.is_valid():
            y=z.cleaned_data
            print(y)
            print("working")
            return render (request,"table.html",{"i":y})
    else:
        x=Author()
        return render (request,"form1.html",{"data":x})

#model form case
# def login(request):
#     x=Loginform()
#     return render(request,"login.html",{"data":x})

def login(request):
    if request.method=="POST":
        z=Loginform(request.POST)
        if z.is_valid():
            z.save()
            return HttpResponse("worked")
    else:
        x=Loginform()
        return render(request,"login.html",{"data":x})
    
#    to view values inserted in database 
def view(request):
    x=Login.objects.all()
    return render(request,"view.html",{"data":x})

#to delete row 
def deletes(request,id):
    x=Login.objects.get(id=id)
    x.delete()
    return HttpResponse("deleted successfully")

#to edit
def edit(request,id):
    x=Login.objects.get(id=id)
    return render(request,"edit.html",{"data":x})

def updates(request,id):
    x=Login.objects.get(id=id)
    if request.method=="POST":
        z=Loginform(request.POST,instance=x)
        print(z)
        if z.is_valid():
            z.save()
            return redirect("view")
        else:
            return HttpResponse("not working")
    else:
        return render(request,"edit.html",{"data":x})

  
# modelform with file
def college(request):
    if request.method=="POST":
        y=Collegeform(request.POST,request.FILES)
        if y.is_valid():
            y.save()
            return HttpResponse("WORKED")
    else:
        x=Collegeform()
        return render(request,"college.html",{"data":x})
    
def viewcollege(request):
    y=College.objects.all()
    return render(request,'collegeview.html',{"data":y})


#normalform

def emp(request):
    if request.method=="POST":
        f=request.POST['firstname']
        l=request.POST['lastname']
        a=request.POST['age']
        p=request.POST['place']
        x=Employee.objects.create(firstname=f,lastname=l,age=a,place=p)
        x.save()
        return HttpResponse("worked")
    else:
        return render(request,"emp.html")


# to view

def viewemp(request):
    x=Employee.objects.all()
    return render(request,"viewemp.html",{"data":x})

# to dlete
def delete_emp(request,id):
    x=Employee.objects.get(id=id)
    x.delete()
    return HttpResponse("deleted successfully")

# to edit
def edit_emp(request,id):
    x=Employee.objects.get(id=id)
    return render (request,"editemp.html",{"data":x})