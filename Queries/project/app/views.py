from django.shortcuts import render
from .models import Students
from django.shortcuts import HttpResponse
# Create your views here.

def alldata(req):
    data= Students.objects.all()
    print(data)
    # return HttpResponse(data)
    return render(req, 'home.html', {'x': data}) 

def myfilter(req):
    data= Students.objects.filter(name="Nikhil")
    print(data)
    # return HttpResponse(data)
    return render(req, 'home.html', {'x': data})

def myorder(req):
    data= Students.objects.order_by('-name')
    # data= Students.objects.order_by('city')
    print(data)
    # return HttpResponse(data)
    return render(req, 'home.html', {'x': data})

def myreverse(req):
    data= Students.objects.order_by('-name')
    data1= Students.objects.order_by('name').reverse()
    print(data)
    # return HttpResponse(data)
    return render(req, 'home.html', {'x': data, 'y':data1})

def myvalue(req):
    data= Students.objects.values()
    print(data)
    # return HttpResponse(data)
    return render(req, 'home.html', {'x': data})

def myvaluelist(req):
    data= Students.objects.values_list()
    print(data)
    # return HttpResponse(data)
    return render(req, 'home.html', {'x': data})

def myslice(req):
    print("first_five from top\n")
    data= Students.objects.all()[:5]
    print(data)
#     print("first_five from top by order\n")
#     data1= Students.objects.order_by("name")[:5]
#     print(data1)
#     print("last_five\n")
#     data2= Students.objects.all()[::-1][:5][::-1]
#     print(data2)
#     print("last object\n")
#     data3= Students.objects.all()[::-1][0:1]
#     print(data3)
#     print("even no. objects\n")
#     data4= Students.objects.all()[::2]
#     print(data4)
#     print("even no. objects\n")
#     data5= Students.objects.all()[1::2]
#     print(data5)
#     return HttpResponse(data5)


# Query that return single object:
def singledata(req):
    # data=Students.objects.get(name="Harshal Thakre")
    # data=Students.objects.get(name="Harshal")
    # print(data)
    # data= Students.objects.first()
    # data= Students.objects.last()
    # data= Students.objects.latest("id")
    # data= Students.objects.latest("name")
    # data= Students.objects.latest("email")
    # data= Students.objects.latest("city")
    # data= Students.objects.earliest("id")
    # data= Students.objects.earliest("name")
    # data= Students.objects.earliest("email")
    data= Students.objects.earliest("city")
    return HttpResponse(data)
