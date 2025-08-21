from django.shortcuts import render
from .forms import RegisterForm 
# Create your views here.

def home(req):
    return render(req, "home.html")

def register(req):
    fm=RegisterForm()
    return render(req, "home.html", {"register":"register","x": fm})