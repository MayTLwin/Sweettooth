

# Create your views here.
from django.shortcuts import render
from recipes.models import Label
# Create your views here.
from django.core import serializers
from django.http import HttpRequest,HttpResponse
import json
def get_labels(request:HttpRequest): 
    labels = Label.objects.all().order_by("name")
 

    json_data = serializers.serialize('json',labels) 
    """label_list = list(labels.values('name','pk'))"""
    return HttpResponse(json_data,content_type='application/json')