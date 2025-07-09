from django.shortcuts import render
from .models import Students
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
        # p= request.POST.get('password'))

        # Queries
    Students.objects.create(first_name=n, email=e, contact=c, image=i, document=d)
    return HttpResponse("Registration Successful")
    





def logindata(request):
    print("Login data")
#     # print("Method used:-\n", request.method, "\n")
#     print("Post data:-\n",request.POST, "\n")
#     # print("Cookies data:-\n", request.COOKIES, "\n")
#     # print("META data:-\n", request.META, "\n")
#     if request.method =="POST":
#         print("E-MAIL:-", '\n' ,request.POST.get('l_email'))
#         print("PASSWORD:-", '\n' ,request.POST.get('l_password'))