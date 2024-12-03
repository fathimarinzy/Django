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