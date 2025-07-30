from django.shortcuts import render

# Create your views here.

def home(req):
    return render(req, "home.html")

def register(req):
    if req.method=="POST":
        n=req.POST.get("name")
        e=req.POST.get("email")
        c=req.POST.get("contact")
        i=req.FILES.get("image")
        d=req.FILES.get("document")
        p=req.POST.get("password")
        cp=req.POST.get("cpassword")
        print(n, e, c, i, d, p, cp)
    return render(req, "register.html")