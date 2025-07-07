from django.shortcuts import render

# Create your views here.

# def home(request):
#     return render(request, "home.html")

def register(request):
    return render(request, ("register.html",{register: register}))

def login(request):
    return render(request, "login.html")

def registerdata(request):
    print("registration")