from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from app.models import *
import json 
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict  #for single obj to py data
# Create your views here.

@csrf_exempt
def stu_list(req):
    if req.method=="POST":
        data=req.body
        print(data)
        print(type(data))
        p_data=json.loads(data)
        print(p_data)
        print(type(data))
        Student.objects.create(name= p_data['name'], email=p_data['email'], contact=p_data['contact'])
        return JsonResponse({"msg": "saved Successfully"})

    all_data=Student.objects.all()
    # print(all_data)
    # print(type(all_data))
    # print(all_data.values())
    # print(type(all_data.values()))
    # print(all_data.values_list())
    py_data=list(all_data.values())
    # print(type(py_data))
    # print(py_data)
    j_data=json.dumps(py_data)
    # print(j_data)
    # print(type(j_data))
    return HttpResponse(j_data, content_type='application/json')

@csrf_exempt
def stu_detail(req, pk):
    if req.method=="PATCH":
        old_data=Student.objects.get(id=pk)
        raw_data=req.body
        new_data=json.loads(raw_data)
        if "name" in new_data:
            old_data.name=new_data["name"]
        if "email" in new_data:
            old_data.email=new_data["email"]
        if "contact" in new_data:            
            old_data.contact=new_data["contact"]
        old_data.save()
        updated_data=Student.objects.get(id=pk)
        updated_data = model_to_dict(updated_data)
        return JsonResponse({"msg":"data updated successfully" ,"updated_data":updated_data})
    elif req.method=="PUT":
        old_data=Student.objects.get(id=pk)
        raw_data=req.body
        new_data=json.loads(raw_data)
        old_data.name=new_data["name"]
        old_data.email=new_data["email"]
        old_data.contact=new_data["contact"]
        old_data.save()
        updated_data=Student.objects.get(id=pk)
        updated_data = model_to_dict(updated_data)
        return JsonResponse({"msg":"data updated successfully" ,"updated_data":updated_data})
    elif req.method=="DELETE":
        stu_data=Student.objects.get(id=pk)
        stu_data.delete()
        return JsonResponse({"msg": "Object Deleted"})    
    else:
        stu_data=Student.objects.get(id=pk)
        p_data= model_to_dict(stu_data)
        j_data= json.dumps(p_data)
        return HttpResponse(j_data, content_type="application/json")