from django.shortcuts import render
from app.models import Student as st
from django.shortcuts import redirect
from urllib.parse import urlencode
from django.urls import reverse
from app.models import Query

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
                # data= urlencode({'id':data.id})
                # return redirect(f'{url}?{data}')
                req.session['id']=data.id
                return redirect(f'{url}')
            else:
                pmsg="Email and Password not matched"
                return render(req, "login.html", {"pmsg":pmsg, "email":e})
            
        else:
            return redirect("register")
    return render(req, "login.html")


def dashboard(req):
    data= req.session.get('id', None)
    # pk= req.GET.get('id')
    # print("dashboard.....")
    if data:
        pk=req.session['id']
        user= st.objects.get(id=pk)
        data={"name":user.name, "email":user.email, "contact":user.contact, "image":user.image, "document":user.document, "password":user.password}
        return render(req, "dashboard.html", {"data":data})
    else:
        return redirect('login')

def logout(req):
    req.session.flush()
    return redirect('home')


def query(req):
    data= req.session.get('id', None)
    # pk= req.GET.get('id')
    # print("dashboard.....")
    if data:
        pk=req.session['id']
        user= st.objects.get(id=pk)
        data={"name":user.name, "email":user.email, "contact":user.contact, "image":user.image, "document":user.document, "password":user.password}
        return render(req, "dashboard.html", {"data":data, "query":"query"})
    else:
        return redirect("login")
    
def querydata(req):
    if req.method=="POST":
        print("QUERY DATA....................")
        n=req.POST.get("name")
        e=req.POST.get("email")
        q=req.POST.get("query")
        print(n, e, q)
        Query.objects.create(name=n, email=e, query=q)
        pk=req.session["id"]
        user=st.objects.get(id=pk)
        data={"name":user.name, "email":user.email, "contact":user.contact, "image":user.image, "document":user.document, "password":user.password}
        return render(req, "dashboard.html", {"data":data})

def showquery(req):
    pk=req.session["id"]
    user=st.objects.get(id=pk)
    data={"name":user.name, "email":user.email, "contact":user.contact, "image":user.image, "document":user.document, "password":user.password}
    e=user.email
    allquery=Query.objects.filter(email=e)
    return render(req, "dashboard.html", {"data":data, "allquery":allquery})
    
