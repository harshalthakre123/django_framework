from django.shortcuts import render
from .forms import RegisterForm 
# Create your views here.

def home(req):
    return render(req, "home.html")

def register(req):
    if req.method=="POST":
        form=RegisterForm(req.POST, req.FILES)
        print(form)
        if form.is_valid():
            n=form.cleaned_data["name"]
            e=form.cleaned_data["email"]
            c=form.cleaned_data["contact"]
            i=form.cleaned_data["image"]
            f=form.cleaned_data["file"]
            print(n, e, c, i, f, sep=",")
    else:
        fm=RegisterForm()
        return render(req, "home.html", {"register":"register","x": fm})