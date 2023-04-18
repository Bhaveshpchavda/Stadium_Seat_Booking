from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout

# Create your views here.
def home_view(request,*args, **kwargs):
    print(args,kwargs)
    print(request.user)
    return render(request,"index.html",{})

def booking_view(request,*args, **kwargs):
    print(args,kwargs)
    print(request.user)
    return render(request,"booking.html",{})

def dashboard_view(request,*args, **kwargs):
    print(args,kwargs)
    print(request.user)
    return render(request,"dashboard.html",{})

def contact_view(request,*args, **kwargs):
    print(args,kwargs)
    print(request.user)
    my_context={
        "text":"contact",
        "number":123,
        "list":[123,456,789]
        
    }
    return render(request,"contact.html",my_context)
    
def login_view(request,*args, **kwargs):
    print(args,kwargs)
    print(request.user)
    return render(request,"login.html",{})

def signup_view(request,*args, **kwargs):
    print(args,kwargs)
    print(request.user)
    return render(request,"signup.html",{})


def signup(request):
    if request.method == "POST":
        Name=request.POST['name']
        email=request.POST['email']
        password=request.POST['pswd']

        if User.objects.filter(username=Name):
            messages.error(request,"Username already exists",extra_tags="validation")
            return redirect('/signup')

        if User.objects.filter(email=email):
            messages.error(request,"Email already exists",extra_tags="validation")
            return redirect('/signup')

        
        myuser=User.objects.create_user(Name, email, password)
        myuser.first_name=Name
        myuser.email=email
        myuser.is_active = True
        myuser.save()
        messages.success(request,"Account has been successfully created", extra_tags="valid")

        
        return redirect('/')

    return render(request,"login.html")

def signin(request):
    if(request.method=="POST"):
        Name=request.POST['name']
        password=request.POST['passwd']
        print(Name,password)
        user=authenticate(request,username=Name,password=password)
        if user is not None:
            login(request,user)
            return redirect('/home/')
            
        else:
            messages.error(request,"Invalid Credentials",extra_tags="invalid")
            return redirect('/')
    return render(request,"login.html")

def signout(request):
    logout(request)
    return redirect('/')

