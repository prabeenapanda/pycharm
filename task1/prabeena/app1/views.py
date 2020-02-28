from django.shortcuts import render
import json
from django.http import HttpResponse
from . models import student
from django.http import JsonResponse
def get(request):
    students = student.objects.all()
    return JsonResponse({"students":list(students.values())})
def add_student(request):
    data = json.loads(request.body)
    name = data['name']
    age = data['age']
    classes = data['classes']
    student.objects.create(name=name, age=age, classes=classes)
    return  JsonResponse({"status":200, "message":"Added Successfully"})