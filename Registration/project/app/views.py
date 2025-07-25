from django.shortcuts import render
from .models import Students as st
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, "home.html")

def register(request):
    return render(request, "home.html",{'register': 'register'})

def login(request):
    return render(request, "home.html", {'login':'login'})

def registerdata(request):
    print("Registration data")
    # print("Method used:-\n", request.method, "\n")
    print("Post data:-\n",request.POST, "\n")
    print("Files data:-\n", request.FILES, "\n")
    # print("Cookies data:-\n", request.COOKIES, "\n")
    # print("META data:-\n", request.META, "\n")
    
    if request.method =="POST":
        n= request.POST.get('name')
        e= request.POST.get('email')
        c= request.POST.get('contact')
        i= request.FILES.get('image')
        d= request.FILES.get('document')
        p= request.POST.get('password')
        cp=request.POST.get('cpassword')
        data=st.objects.filter(email=e)
        if data:
            msg="Email Already Exist!"
            return render(request, "home.html", {"msg": msg, 'register': 'register'})
        elif p==cp:
            st.objects.create(first_name=n, email=e, contact=c, image=i, document=d, password=p)
            msg="Registration Successful!"
            return render(request, "home.html", {'login':'login'})
        else:
            msg="Password and confirm Password not Matched!"
            return render(request, "home.html", {"msg": msg, "register": "register"}) 
            





def logindata(request):
    print("Login data")
    # print("Method used:-\n", request.method, "\n")
    # print("Post data:-\n",request.POST, "\n")
    # print("Cookies data:-\n", request.COOKIES, "\n")
    # print("META data:-\n", request.META, "\n")
    if request.method =="POST":
        e=request.POST.get('email')
        p=request.POST.get('password')
        data=st.objects.filter(email=e)
        if data:
            user=st.objects.get(email=e)
            password=user.password
            if p==password:
                stu_data={"name":user.first_name, "email":user.email , "contact": user.contact, "image":user.image, "document":user.document}
                msg="Login Successful"
                return render(request, "userdash.html", {"msg":msg, "stu_data":stu_data})
            else:
                msg="Email and Password Not Matched!"
                return render(request, "home.html", {"msg":msg})
        else:
            msg="email not registered, Please Sign-up"
            return render(request, "home.html", {"msg":msg, "register":register})
