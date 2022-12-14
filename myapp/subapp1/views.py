from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature

# Create your views here.
def index(request): 
    features = Feature.objects.all()
    return render(request, 'index.html', {"features": features})

def counter(request):
    if request.method == "POST": 
        text=request.POST["words"]
        noOfWords = len(text.split(" "))
        return render(request, 'counter.html', {"noOfWords": noOfWords})
    posts = ['hello', 'world', 'wow']
    return render(request, 'counter.html', {"posts": posts})

def register(request):
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        if password1 == password2:
            if User.objects.filter(email=email).exists(): 
                messages.info(request, 'User Already Exists')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'UserName Already Exists')
                return redirect('register')
            else: 
                user=User.objects.create_user(email=email, username=username, password=password1)
                user.save()
                return redirect('login')
        else: 
            messages.info(request, 'Passwords dont match')
            return redirect('register')
    else: 
        return render(request, 'register.html')

def login(request): 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        if user is not None: 
            auth.login(request, user)
            return redirect('/')
        else: 
            messages.info(request, 'User not found')
            return redirect('login')
    else: 
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def post(request,pk): 
    return render(request, 'post.html',{'pk':pk})