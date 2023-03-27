from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import UserRegistration
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def register_view(request):
    form=UserRegistration()
    if request.method =='POST':
        form=UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "account created successfully")
            return redirect ("home")

    context={
        'form':form
    }
    return render(request, 'usersapp/register.html', context)

def my_login_view(request):
    if request.method == 'POST':
        form=AuthenticationForm(request.POST)
        if form.is_valid():
            pass
