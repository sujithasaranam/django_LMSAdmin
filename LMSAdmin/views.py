import email
import imp
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .forms import BookForm
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required


# Create your views here.
from .models import *
from operator import itemgetter
from django.contrib import messages

def registerPage(request):
    global p
    if request.method=='POST':
        user=User()
        user.Username=request.POST['username']
        user.email=request.POST['email']
        user.password=request.POST['password']
        user.conformpassword=request.POST['confirm-password']
        p=1
        if user.Username=='' or user.email=='' or user.password=='' or user.conformpassword=='':
            p=0
            messages.add_message(request, messages.WARNING, 'Some fields are empty.Please fill all the fields and click on "Register Now"')
            return redirect('register')

        if user.password!=user.conformpassword:
            p=0
            messages.add_message(request, messages.WARNING, 'Password and confirm Password did not match. Please try again')
            return redirect('register')
        x=User.objects.all()
        for i in x:
            if i.email==user.email:
                messages.add_message(request, messages.WARNING, 'Email already exists.Please try again')
                p=0
        if(p==1):
            user.save()
    return render(request,'accounts/register.html')
			


def loginPage(request):
    global p2
    if request.method == 'POST':
        email = request.POST['email']
        password =request.POST['password']
        x=User.objects.all()
        for i in x:
            p2=0
            if i.email==email and i.password==password:
                p1=1
                return redirect('adminlogin')
        if(p2!=1):
            messages.error(request, "Bad Credentials!!")
            return redirect('login')
    
    return render(request, "accounts/login.html")

def addbook(request):
    global p1
    if request.method=='POST':
        b=Book()
        b.Bookname=request.POST['Bookname']
        b.Author=request.POST['Author']
        b.Noofbooks=request.POST['Noofbooks']
        b.Branch=request.POST['Branch']
        p1=1
        if b.Bookname=='' or b.Author=='' or b.Noofbooks=='' or b.Branch=='':
            p1=0
            messages.add_message(request, messages.WARNING, 'Some fields are empty.Please fill all the fields and click on "Register Now"')
            return redirect('addbook')
        if(p1==1):
            messages.add_message(request, messages.SUCCESS, 'Book added successfully!!')
            b.save()
    return render(request,'accounts/addbook.html')

def admin(request):
    books = Book.objects.all()
    return render(request, 'accounts/admin.html', {'books':books})


def home(request):
    books = Book.objects.all()
    return render(request, 'accounts/home.html', {'books':books})

def logoutUser(request):
	logout(request)
	return redirect('login')

def updatebook(request,pk):
    book = Book.objects.get(Id=pk)
    form = BookForm(instance=book)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('adminlogin')
    context = {'form':form}
    return render(request, 'accounts/update.html', context)

def deletebook(request,pk):
    book = Book.objects.get(Id=pk)
    if request.method == "POST":
        book.delete()
        return redirect('adminlogin')

    context = {'item':book}
    return render(request, 'accounts/delete.html', context)


