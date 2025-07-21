from django.shortcuts import render
from app.models import Students as st
from app.models import Aadhar as aa
from django.shortcuts import HttpResponse
from app.models import Department as dp
from app.models import Students1 as stu

# Create your views here.

#forward access=========]

def ForwardAccess(req):
    
    ##one-to-one===============================================================
    
    # data=st.objects.get(id=1)
    # name=data.name
    # email=data.email
    # city=data.city
    # aad_obj=data.a_no
    # aadhar=data.a_no.a_no
    # gen_date=data.a_no.gen_date
    # return HttpResponse({name:name, email:email, city:city, aad_obj:aad_obj, aadhar:aadhar, gen_date:gen_date})
    
    # data=st.objects.all()
    # return render(req, "home.html" , {'x': data})

    ##one to many=====================================================================

    # data1=stu.objects.get(id=1)
    # name=data1.name
    # email=data1.email
    # contact=data1.contact
    # depart_obj=data1.depart
    # department= data1.depart.d_name
    # return HttpResponse({name: name, email: email, contact: contact, depart_obj: depart_obj  ,department: department})

    data1=stu.objects.all()
    return render (req, 'home.html', {"a": data1})
    


def ReverseAccess(req):
    
    ##one-to-one

    # data=aa.objects.get(id=1)
    # aadhar_no=data.a_no
    # gen_date=data.gen_date
    # stu_data=data.stu_info
    # name=stu_data.name
    # email=stu_data.email
    # city=stu_data.city
    # return HttpResponse({aadhar_no:aadhar_no, gen_date:gen_date , name:name, email:email, city:city})

    # data=aa.objects.all()
    # return render(req, "home.html", {'y': data})


    ##one to many=============================================================


    data1=dp.objects.get(id=1)
    depart=data1.d_name
    print(depart)
    x=data1.student_info.all()
    for i in x:
        print(i.name)


    return HttpResponse({depart: depart, name: name, email: email , contact: contact})


    # data1=dp.objects.all()
    # return render(req, "home.html", {"b": data1})
