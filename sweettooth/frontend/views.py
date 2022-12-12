

# Create your views here.
from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from django.views.generic import TemplateView

# Create your views here.
"""def index(request:HttpRequest):
    name = ''

    if "name" in request.GET:
        name=request.GET["name"]

    return HttpResponse(f"<h2>Sweet Tooth{name}</h2>")"""


def home(request:HttpRequest):
    return render(request,'frontend/home.html');

def about__us(request:HttpRequest):

    return render(request,'frontend/aboutus.html');

def contact__form(request:HttpRequest):

    return render(request,'frontend/contact.html');
