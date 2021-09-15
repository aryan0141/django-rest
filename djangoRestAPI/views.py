from re import S
from django.shortcuts import render
from django.utils.html import json_script
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

def student_detail(request, name):
    stu = Student.objects.get(name = name)
    stu_serialized = StudentSerializer(stu)
    json_object = JSONRenderer().render(stu_serialized.data)
    return HttpResponse(json_object, content_type="application/Json")

def student_list(request):
    stu = Student.objects.all()
    stu_serialized = StudentSerializer(stu, many=True)
    json_object = JSONRenderer().render(stu_serialized.data)
    return HttpResponse(json_object, content_type="application/Json")
# Create your views here.
