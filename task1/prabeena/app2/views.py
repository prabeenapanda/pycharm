from django.shortcuts import render
from django.http import JsonResponse
import json
from django.http import HttpResponse
from . models import rack
def gett(request):
    racks=rack.objects.all()
    return JsonResponse({"racks":list(racks.values())})
def addd(request):
    data = json.loads(request.body)
    name = data['name']
    size=data['size']
    rack.objects.create(name=name,size=size)
    return  JsonResponse({"status":200, "message":"Added Successfully"})