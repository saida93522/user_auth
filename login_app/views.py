from django.shortcuts import render, redirect, get_object_or_404
from  django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages

from .forms import RegisterForm, LoginForm

User = get_user_model()

def home(request):
    return render(request,'home.html')

def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password1']
        password2 = form.cleaned_data['password2']

    context={"form":form}
    return render(request,'register.html',context)

def login_user(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.clean_username['username']
        password = form.clean_password['password']
        user = authenticate(request, username=username,password=password)
        if user !=None:
            login(request,user)
            return redirect('homepage')
        else:
            request.session['invalid_user'] = 1
            
    context={"form":form}
    return render(request,'login.html',context)

def logout_user(request):
    logout(request)
    return redirect('/login')