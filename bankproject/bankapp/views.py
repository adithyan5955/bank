from django.shortcuts import get_object_or_404, render, redirect
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.db import connection
def HomePage(request):
    return render(request,"index.html")
def LoginPage(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('bankapp:submit_application')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("bankapp:loginpage")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})

def logout(request):
    auth.logout(request)
    return redirect('/')
  
def submit_application(request):
    if request.method == 'POST':
        form = AccountApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html', {'message': 'Application accepted'})
        else:
            # Form is not valid, display validation errors
            return render(request, 'form1.html', {'form': form})
    else:
        form = AccountApplicationForm()
    return render(request, 'form1.html', {'form': form})

def form_details(request, form_id):
    # Retrieve the form data by form ID
    form_data = get_object_or_404(AccountApplication, pk=form_id)

    return render(request, 'form_details.html', {'form_data': form_data})