from django.shortcuts import render, redirect, get_object_or_404
from  django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages

from .forms import RegisterForm, LoginForm

User = get_user_model()

# Create your views here.
def register(request):
    context={}
    return render(request,'register.html',context)


def login(request):
    context={}
    return render(request,'login.html',context)


def logout(request):
    return redirect('/login')