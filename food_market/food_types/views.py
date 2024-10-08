from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Register

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def register(request):
  template=loader.get_template("register.html")
  if request.method=="POST":
    fname=request.POST["fname"]
    lname=request.POST["lname"]
    email=request.POST["email"]
    password=request.POST["password"]
    user=Register(fname=fname,lname=lname,email=email,password=password)
    user.save()
  return render(request,"register.html")

def loginpage(request):
  
  return render(request,"login.html")

def login(request):
  
  if request.method=="POST":
    email=request.POST["email"]
    password=request.POST["password"]
    # user=Register.objects.get(email=email)
    try:
        user=Register.objects.get(email=email)
    except Register.DoesNotExist:
        user=None
    if user:
       if user.password==password:
         request.session['lname']=user.lname
         return render(request,"main.html")
       else:
         message="password not match"
         return render(request,"login.html",{'msg':message})
    else:
      message="user does not exit.create account"
      return render(request,"register.html",{'msg':message})
  else:
    return render(request,"login.html")


