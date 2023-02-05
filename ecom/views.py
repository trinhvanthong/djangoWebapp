from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework import viewsets
from .serializers import *


import re 
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
def checkmail(email):   
    if(re.search(regex,email)):   
        return False
    else:   
        return True
       
# Create your views here.
def index(request):
    return HttpResponse("hello")

def home(request):
    return render(request, "home.html")
# 
# 
# test
def addPaintings(request):
    user = Author.objects.get(id=1)
    user.createPainting("JQK",150,"24x24")
    return render(request, 'home.html')
# 
# 
# user register page
def register(request):
    return render(request,"user_register.html")
# 
# 
# 
def index(request):
    return HttpResponse("hello")

def home(request):
    return render(request, "home.html")
# 
# 
# test
def addPaintings(request):
    user = Author.objects.get(id=1)
    user.createPainting("JQK",150,"24x24")
    return render(request, 'home.html')
# 
# 
# user register page
def register(request):
    if request.method =='POST':
        username1=request.POST.get('username')
        password=request.POST.get('password')
        repassword=request.POST.get('repassword')
        email=request.POST.get('email')
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        try:
            user = User.objects.get(username=username1)
            messages.error(request, 'Your username had been existed')  
        except:
            if password!=repassword:
                messages.error(request, 'Your password does not match')  
            elif checkmail(email):
                messages.error(request, 'Your email is invalid')  
            elif firstname=="" or lastname=="":
                messages.error(request, 'your information cannot be null ')     
            else:
                newUser=User()
                newUser.email=email    
                newUser.set_password(password)  
                newUser.username=username1    
                newUser.first_name=firstname    
                newUser.last_name=lastname    
                newUser.save()
                return redirect('login')
    return render(request,"user_register.html")
# 
# 
#  login/logout
def loginPage(request):
    if request.method== 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user= authenticate(request, username=username, password=password) 
        if user is not None:
            login(request, user) 
            return redirect('home')
        else:
            messages.error(request, 'Your username or password is not correct')  
    context= {}    
    return render(request, 'login.html',context)
def logoutPage(request):
    logout(request)
    return redirect('home')
# 
# 
# show all artist
def artist(request):
    artist_list=Author.objects.all()
    paginator = Paginator(artist_list, 5)
    pageNumber = request.GET.get('page')
    try:
        artists = paginator.page(pageNumber)
    except PageNotAnInteger:
        artists = paginator.page(1)
    except EmptyPage:
        artists = paginator.page(paginator.num_pages)
    return render(request,'artist.html',{'artists': artists})
# 
# 
# show paintings 
def painting(request,key=0):
    if key==0:
        painting_list=Paintings.objects.all()
    else:
        painting_list=Paintings.objects.all().filter(Author_id=key) 
    paginator = Paginator(painting_list, 5)
    pageNumber = request.GET.get('page')
    try:
        paintings = paginator.page(pageNumber)
    except PageNotAnInteger:
        paintings = paginator.page(1)
    except EmptyPage:
        paintings = paginator.page(paginator.num_pages)
    try:    
        artist= Author.objects.get(id=key) 
    except:
        artist= "all"    
    return render(request,'paintings.html',{'paintings': paintings, "artist":artist})
# 
# 
# API
class PaintingViewSet(viewsets.ModelViewSet):
    queryset= Paintings.objects.all()
    serializer_class= PaintingSerializer