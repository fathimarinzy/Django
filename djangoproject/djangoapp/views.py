from django.shortcuts import render,HttpResponse,redirect

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