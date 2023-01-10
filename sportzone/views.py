from collections import UserDict
from django.shortcuts import render,redirect
from django import *
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login
from pyexpat.errors import messages
from django.contrib.auth.models import User




def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            print(username,password)
            if user is not None:
                login(request, user)
                # uid = request.user.id
                print("login sucessfull")
                return redirect('adminDash')
                
            else:
                print("User none")
    else:
        form = LoginForm()
    return render(request, 'customer/login.html', {'form': form})

def customerRegister(request):
    if request.POST:
        username = request.POST['username']
        password1 = request.POST['password']
        password2 = request.POST['password2']
        user = User.objects.create_user(username=username, password=password1)
        user.save()
        forms=CustomerRegisterForm(request.POST)
        if forms.is_valid():
            forms.save()
    return render(request,"customer/register.html",{'form':CustomerRegisterForm})

def adminDashboard(request):
    return render(request,'adminDashboard.html')

def productsList(request):
    return render(request,'productsList.html')

def addproducts(request):
    
    return render(request,'addproducts.html')

def orderdetail(request):
    
    return render(request,'orderdetail.html')

def store(request):
    return render(request,'customer/store.html')


def cart(request):
    
    return render(request,'cart.html')

def orderdetail(request):
    
    return render(request,'orderdetail.html')

def checkout(request):
    
    return render(request,'customer/customerdash.html')

