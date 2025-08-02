from django.shortcuts import render
from app.models import Student as st
from django.shortcuts import redirect

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
        # print(n, e, c, i, d, p, cp)
        user=st.objects.filter(email=e)
        if user:
            msg="user already exist!"
            return render(req, 'register.html', {"msg":msg})
        else:
            if p==cp:
                data={"name":n, "email":e, "contact":c, "image":i, "document":d, "password":p}
                st.objects.create(name=n, email=e, contact=c, image=i, document=d, password=p)
                return redirect("login")
            else:
                pmsg="password and confirm password not matched"
                return render(req, "register.html",{"pmsg", pmsg})
    return render(req, "register.html")


from urllib.parse import urlencode
from django.urls import reverse
def login(req):
    if req.method=="POST":
        e=req.POST.get("email")
        p=req.POST.get("password")
        # print(e, p, sep=",")
        user=st.objects.filter(email=e)
        if user:
            data=st.objects.get(email=e)
            upass=data.password
            print(upass)
            if upass==p:
                url= reverse('dashboard')
                data= urlencode({'id':data.id})
                return redirect(f'{url}?{data}')
            else:
                pmsg="Email and Password not matched"
                return render(req, "login.html", {"pmsg":pmsg, "email":e})
            
        else:
            return redirect("register")
    return render(req, "login.html")


def dashboard(req):
    pk= req.GET.get('id')
    user= st.objects.get(id=pk)
    data={"name":user.name, "email":user.email, "contact":user.contact, "image":user.image, "document":user.document, "password":user.password}
    return render(req, "dashboard.html", {"data":data})