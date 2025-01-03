from django.shortcuts import render,HttpResponse,redirect
from .forms import Author,Loginform,Collegeform,Home
from .models import Login,College,Employee,Author,Book,Testing,Authors,Books,Students,Marks,Teachers,Department,Loginpage,Trainer
from django.views.generic import CreateView,DetailView,ListView,DeleteView,UpdateView

from django.core.mail import send_mail
from djangoproject import settings




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

#to update
def update_emp(request,id):
    if request.method=="POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        age=request.POST['age']
        place=request.POST['place']
        x=Employee.objects.get(id=id)
        x.firstname=firstname
        x.lastname=lastname
        x.age=age
        x.place=place
        x.save()
        return HttpResponse("worked")

#    to connect two table using fk

def authorfm(request):
    if request.method=="POST":
        n=request.POST['name']
        p=request.POST['phone']
        e=request.POST['email']
        x=Author.objects.create(name=n,phone=p,email=e)
        x.save()
        return HttpResponse("worked")
    else:
        return render(request,"authorfm.html")

def author(request):
    x=Author.objects.all()
    return render(request,"author.html",{"data":x})


def price(request):
    if request.method=="POST":
        Aut=request.POST['Aut_id']
        price=request.POST['price']
        z=Author.objects.get(id=Aut)
        x=Book.objects.create(Author_id=z,price=price)
        x.save()
        return HttpResponse("worked")
    else:
        x=Author.objects.all()
        return render(request,"author.html",{"data":x})

def price_view(request):
    x=Book.objects.all()
    return render (request,"priceview.html",{"data":x})


def pricedelete(request,id):
    x=Book.objects.get(id=id)
    x.delete()
    return HttpResponse("worked")

def priceedit(request,id):
    x=Book.objects.get(id=id)
    return render(request,"priceedit.html",{"data":x})

def updateprice(request,id):
    if request.method=="POST":
        price=request.POST['price']
        x=Book.objects.get(id=id)
        x.price=price
        x.save()
        return redirect("priceview")
    

 #image case

def testing(request):
    x=Testing.objects.all()
    return render (request,"img.html",{"data":x})

def for_images(request):
    if request.method=="POST":
        x=request.FILES['images']
        y=request.POST['phone']
        s=Testing.objects.create(image_lawn=x,phone=y)
        s.save()
        return HttpResponse("worked")
    else:
        return render(request,'img.html')
    
def view_image(request):
    x=Testing.objects.all()
    return render(request,"viewimg.html",{"view":x})


def editimg(request,id):
    x=Testing.objects.get(id=id)
    return render(request,"editimg.html",{"view":x})

def updimg(request,id):
    if request.method=="POST":
        phone=request.POST['phone']
        x=Testing.objects.get(id=id)
        if "images" in request.FILES:
            x.image_lawn=request.FILES['images']
        x.phone=phone
        x.save()
        return redirect("test2")


 

# session cookie
def setcookie(request):
    r=HttpResponse("cookie is set")
    r.set_cookie("django","Its a framework")
    return r

def getcookie(request):
    r=request.COOKIES['django']
    return HttpResponse(r)

def setsession(request):
    request.session['name']='ammu'
    return HttpResponse("session set")     

def getsession(request):
    x=request.session['name']
    return HttpResponse(x)

def deletesession(request):
    del request.session['name']
    return HttpResponse('session deleted')


# hw
def authdetail(request):
  if request.method=="POST":
      a=request.POST['author_name']
      l=request.POST['language']
      p=request.POST['published_year']
      x=Authors.objects.create(author_name=a,language=l,published_year=p)
      x.save()
      return HttpResponse("worked")
  else:
      return render(request,'authdetail.html')
  
def authors(request):
    x=Authors.objects.all()
    return render(request,"authors.html",{"data":x})

def book_name(request):
    if request.method=="POST":
        aut=request.POST['Auth_id']
        book_name=request.POST['book_name']
        z=Authors.objects.get(id=aut)
        x=Books.objects.create(auth_id=z,book_name=book_name)
        x.save()
        return HttpResponse("worked")
    else:
        x=Authors.objects.all()
        return render(request,'authors.html',{"data":x})

def detailview(request):
    x=Books.objects.all()
    return render(request,'detailview.html',{"data":x})

def bookdelete(request,id):
    x=Books.objects.get(id=id)
    x.delete()
    return HttpResponse("worked")

def bookedit(request,id):
    x=Books.objects.get(id=id)
    return render(request,"detailedit.html",{"data":x})

def bookupdate(request,id):
    if request.method=="POST":
        book_name=request.POST['book_name']
        x=Books.objects.get(id=id)
        x.book_name=book_name
        x.save()
        return redirect("detailview")
    
def stddetail(request):
    if request.method=="POST":
        s=request.POST['std_name']
        c=request.POST['course']
        p=request.POST['place']
        a=request.POST['age']
        ph=request.POST['phone']
        e=request.POST['email']
        x=Students.objects.create(std_name=s,course=c,place=p,age=a,phone=ph,email=e)
        x.save()
        return HttpResponse("worked")
    else:
        return render(request,'stdform.html')
    
def std(request):
    x=Students.objects.all()
    return render(request,'std.html',{"data":x}) 
        
def mark(request):
    if request.method=="POST":
        stu=request.POST['st_id']
        mark=request.POST['mark']
        z=Students.objects.get(id=stu)
        x=Marks.objects.create(std_id=z,mark=mark)
        x.save()
        return HttpResponse("worked")
    else:
        x=Students.objects.all()
        return render(request,'std.html',{"data":x})

def stdview(request):
    x=Marks.objects.all()
    return render(request,'stdview.html',{"data":x})

def stddelete(request,id):
    x=Marks.objects.get(id=id)
    x.delete()
    return HttpResponse("worked")

def stdedit(request,id):
    x=Marks.objects.get(id=id)
    return render(request,"stdedit.html",{"data":x})

def stdupdate(request,id):
    if request.method=="POST":
        mark=request.POST['mark']
        x=Marks.objects.get(id=id)
        x.mark=mark
        x.save()
        return redirect("stdview")  


def tchrdetail(request):
    if request.method=="POST":
        n=request.POST['name']
        s=request.POST['sub']
        x=Teachers.objects.create(name=n,sub=s)
        x.save()
        return HttpResponse("worked")
    else:
        return render(request,'tchrform.html')
    
def tchr(request):
    x=Teachers.objects.all()
    return render(request,'tchr.html',{"data":x}) 
        
def dept_name(request):
    if request.method=="POST":
        tch=request.POST['tch_id']
        dept_name=request.POST['dept_name']
        z=Teachers.objects.get(id=tch)
        x=Department.objects.create(tchr_id=z,dept_name=dept_name)
        x.save()
        return HttpResponse("worked")
    else:
        x=Teachers.objects.all()
        return render(request,'tchr.html',{"data":x})

def deptview(request):
    x=Department.objects.all()
    return render(request,'deptview.html',{"data":x})

def deptdelete(request,id):
    x=Department.objects.get(id=id)
    x.delete()
    return HttpResponse("worked")

def deptedit(request,id):
    x=Department.objects.get(id=id)
    return render(request,"deptedit.html",{"data":x})

def deptupdate(request,id):
    if request.method=="POST":
        dept_name=request.POST['dept_name']
        x=Department.objects.get(id=id)
        x.dept_name=dept_name
        x.save()
        return redirect("deptview")  
    

# task
def home(request):
        return render(request,'home.html')
   

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username and password:  
            request.session["username"] = username
            return redirect("edit")
        return HttpResponse("Invalid login credentials.")
    return render(request, 'loginpage.html')
      
      
def edit(request):
    x=request.session.get("username")
    if x:  
        return render(request, 'editpage.html', {"data": x})
    else:
        return HttpResponse("Please log in first.")

def logout(request):
    if request.session.get("username"):
        request.session.flush() 
        return redirect("login")
    else:
        return HttpResponse("You are not logged in.")


# Generic views
class Trainercreate(CreateView):
    model=Trainer
    template_name='create.html'
    fields=['firstname','lastname','age','email','subject']
    success_url='list'

class Trainerlist(ListView):
    model=Trainer
    template_name='list.html'
    context_object_name='data'

class Trainerdetail(DetailView):
    model=Trainer
    template_name='detail.html'
    context_object_name='data'

class Traineredit(UpdateView):
    model=Trainer
    template_name='create.html'
    fields=['firstname','lastname','age','email','subject']
    success_url='/list'

class Trainerdelete(DeleteView):
    model=Trainer
    template_name="delete.html"
    success_url="/list"

#djangoform

def house(request):
    if request.method=="POST":
        x=Home(request.POST)
        if x.is_valid():
            print(x.cleaned_data)
    else:
        x=Home()
    return render(request,"house.html",{"data":x})


#loader method
from django.template import loader

def loa(request):
    x=loader.get_template("third.html")
    z='hai'
    return HttpResponse(x.render({"data":z}))


#mail 
def new_mail(request):
    subject='this is a mail with django'
    msg='this is a djngo mail'
    to='akshayp9396@gmail.com'
    r=send_mail(subject,msg,settings.EMAIL_HOST_USER,[to])
    if r==1:
        a="success"
    else:
        a="failed"
    return HttpResponse(a)