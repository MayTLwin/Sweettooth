from django.urls import path
from . import views

urlpatterns = [
    path('',views.recipe_list,name = "recipe"),
    path('detail/<int:id>',views.recipe_details,name = "recipe_details"),]