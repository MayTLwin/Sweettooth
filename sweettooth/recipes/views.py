

# Create your views here.
from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from .models import Recipe
from urllib.parse import quote_plus




def recipe_list(request:HttpRequest):
    
    recipes=[]
    if 'category' in request.GET:
      recipes = Recipe.objects.all().filter(label_id =request.GET['category'])
    else:
      recipes = Recipe.objects.all()


  
    return render(request,'recipes/recipes.html',{'recipes':recipes,})

def recipe_details(request,id : int):
    recipe = Recipe.objects.get(pk = id)
    share_string = quote_plus(recipe.name)
    context = {
  "recipe":recipe,
  "share_string":share_string,
    }

    
    return render (request,'recipes/detail.html',context)



