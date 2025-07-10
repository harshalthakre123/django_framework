from django.shortcuts import render

# Create your views here.

def homepg(request):
    return render(request, "homepg.html")

def men(request):
    return render(request, "men.html")

def women(request):
    return render(request, "women.html")

def kids(request):
    return render(request, "kids.html")

def home(request):
    return render(request, "home.html")

def beauty(request):
    return render(request, "beauty.html")

def genz(request):
    return render(request, "genz.html")

def studio(request):
    return render(request, "studio.html")

def wishlist(request):
    return render(request, "wishlist.html")

def bag(request):
    return render(request, "bag.html")















