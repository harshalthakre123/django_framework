from django.shortcuts import render

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
        print("NAME:-", '\n' ,request.POST.get('name'))
        print("E-MAIL:-", '\n' ,request.POST.get('email'))
        print("CONTACT NO.:-", '\n' ,request.POST.get('contact'))
        print("IMAGE:-", '\n' ,request.FILES.get('image'))
        print("DOCUMENT:-", '\n' ,request.FILES.get('document'))
        print("PASSWORD:-", '\n' ,request.POST.get('password'))
    


def logindata(request):
    print("Login data")
    # print("Method used:-\n", request.method, "\n")
    print("Post data:-\n",request.POST, "\n")
    # print("Cookies data:-\n", request.COOKIES, "\n")
    # print("META data:-\n", request.META, "\n")
    if request.method =="POST":
        print("E-MAIL:-", '\n' ,request.POST.get('l_email'))
        print("PASSWORD:-", '\n' ,request.POST.get('l_password'))