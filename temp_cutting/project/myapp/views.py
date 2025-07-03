from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def cart(request):
    return render(request, "cart.html")

def orders(request):
    return render(request, "orders.html")

def profile(request):
    return render(request, "profile.html")

def register(request):
    return render(request, "register.html")

def login(request):
    return render(request, "login.html")