from django.shortcuts import render
from .forms import RegisterForm 
from .models import User
# Create your views here.

def home(req):
    return render(req, "home.html")

def register(req):
    if req.method=="POST":
        form=RegisterForm(req.POST, req.FILES)
        print(form)
        if form.is_valid():
            print("------------------------------------")
            # n=form.cleaned_data["name"]
            # e=form.cleaned_data["email"]
            # c=form.cleaned_data["contact"]
            # i=form.cleaned_data["image"]
            # f=form.cleaned_data["file"]
            # print(n, e, c, i, f, sep=",")
            # User.objects.create(name=n, email=e, contact=c, image=i, file=f)
            form.save()
            return render(req, "home.html")  
        else:
            return render(req, "home.html", {"x": form} )      
    else:
        fm=RegisterForm()
        return render(req, "home.html", {"x": fm})
    
def showuser(req):
    data=User.objects.all()
    return render(req, "home.html", {"data": data})

def hidedata(req):
    data=User.objects.all()
    return render(req, "home.html")