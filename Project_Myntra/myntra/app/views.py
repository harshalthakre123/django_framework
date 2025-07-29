from django.shortcuts import render
from django.shortcuts import HttpResponse
from app.models import Users

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


def signup(req):
    if req.method=="POST":
        fn=req.POST.get("fname")
        ln=req.POST.get("lname")
        e=req.POST.get("email")
        c=req.POST.get("contact")
        p=req.POST.get("password")
        cp=req.POST.get("cpassword")
        # print(fn, ln, e, c, p, cp)
        data=Users.objects.filter(email=e)
        if data:
            msg="User Already Exist! Please Login."
            return render(req, "registration.html", {"msg": msg})
        elif p==cp:
            Users.objects.create(f_name=fn, l_name=ln, email=e, contact=c, password=p)
            msg="Registration Successful, Please Login to Continue."
            return render(req, "registration.html", {"login_form":"login_form","msg":msg})
        else:
            msg="Password and Confirm Password Not Matched! Please Try Again"
            return render(req, "registration.html", {"signup_form": "signup_form", "msg": msg})

    return render(req, "registration.html",{"signup_form": "signup_form",})

def login(req):
    if req.method=="POST":
        e=req.POST.get("email")
        p=req.POST.get("password")
        data=Users.objects.filter(email=e)
        if data:
            user_obj=Users.objects.get(email=e)
            password=user_obj.password
            if p==password:
                user_data={"f_name": user_obj.f_name, "l_name": user_obj.l_name ,"email": user_obj.email,"contact": user_obj.contact}
                msg="Login Successful!"
                return render(req, "homepg.html", {"msg":msg, "user_data":user_data})
            else:
                msg="Email and password not matched!"
                return render(req, "registration.html", {"signup_form": "signup_form","email":e} )
    return render(req, "registration.html", {"login_form": "login_form"})


def logout(req):
    pass
    # login.user_data={}
    # return render(req, "home.html",{"user_data ":user_data})







