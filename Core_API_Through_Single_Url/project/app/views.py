from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from app.models import *
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
import json
# Create your views here.

@csrf_exempt
def stu_detail(req):
    data=req.body
    if req.body== b'':
        all_data=Students.objects.all()
        py_data=list(all_data.values())
        j_data=json.dumps(py_data)
        return HttpResponse(j_data ,content_type="application/json")

    p_data=json.loads(data)
    if "id" in p_data:
        pk=p_data["id"]
        stu_data=Students.objects.get(id=pk)
        if req.method=="DELETE":
            stu_data.delete()
            return JsonResponse({"msg": "Data Deleted Successfully"})
        
        elif req.method=="PUT":
            stu_data.name=p_data["name"]
            stu_data.email=p_data["email"]
            stu_data.contact=p_data["contact"]
            stu_data.save()
            return JsonResponse({"msg":"Object Updated"})

        elif req.method=="PATCH":
            if "name" in p_data:
                stu_data.name=p_data["name"]
            if "email" in p_data:
                stu_data.email=p_data["email"]
            if "contact" in p_data:
                stu_data.contact=p_data["contact"]    
            stu_data.save()
            return JsonResponse({"msg":"Data Updated"})
        
        elif req.method=="GET":
            py_data=model_to_dict(stu_data)
            data=json.dumps(py_data)
            return HttpResponse(data, {"msg":"Data Fetched"})
    
    else:
        Students.objects.create(name=p_data["name"], email=p_data["email"], contact=p_data["contact"])
        return JsonResponse({"msg": "Data Added"})
        # if req.method=="POST":
        #     Students.objects.create(name=p_data["name"], email=p_data["email"], contact=p_data["contact"])
        #     return JsonResponse({"msg": "Data Added"})
        # else:
        #     all_data=Students.objects.all()
        #     py_data=list(all_data.values())
        #     j_data=json.dumps(py_data)
        #     return HttpResponse(j_data ,content_type="application/json")