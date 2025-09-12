from django.shortcuts import render
from app.models import Students
from app.serializers import StudentSerializer
from django.http import HttpResponse, JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def stu_list(req):
    if req.method=="POST":
        data=req.body
        stream = io.BytesIO(data)
        p_data = JSONParser().parse(stream)
        serializer=StudentSerializer(data=p_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"msg":"Data Created"})
        return JsonResponse({"error": serializer.errors} )
    all_stu=Students.objects.all()
    serializer=StudentSerializer(all_stu, many=True)
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def stu_detail(req, pk):
    data=Students.objects.filter(id=pk)
    if data:
        data=Students.objects.get(id=pk)
        if req.method=="GET":
            serializer=StudentSerializer(data)
            return JsonResponse(serializer.data)
        if req.method=="DELETE":
            data.delete()
            return JsonResponse({"msg":"Data Deleted"})