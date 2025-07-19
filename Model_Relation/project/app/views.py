from django.shortcuts import render
from app.models import Students as st
from app.models import Aadhar as aa
from django.shortcuts import HttpResponse

# Create your views here.

#forward access=========]

def ForwardAccess(req):
    
    ##one-to-one
    
    data=st.objects.all()
    # data=st.objects.get(id=1)
    # name=data.name
    # email=data.email
    # city=data.city
    # aad_obj=data.a_no
    # aadhar=data.a_no.a_no
    # gen_date=data.a_no.gen_date
    # return HttpResponse({name:name, email:email, city:city, aad_obj:aad_obj, aadhar:aadhar, gen_date:gen_date})

    return render(req, "home.html" , {'x': data})

def ReverseAccess(req):
    
    ##one-to-one

    data=aa.objects.all()
    # data=aa.objects.get(id=1)
    # aadhar_no=data.a_no
    # gen_date=data.gen_date
    # stu_data=data.stu_info
    # name=stu_data.name
    # email=stu_data.email
    # city=stu_data.city
    # return HttpResponse({aadhar_no:aadhar_no, gen_date:gen_date , name:name, email:email, city:city})
    return render(req, "home.html", {'y': data})