from django.urls import path
from . import views

urlpatterns = [
    path('label/',views.get_labels,name ="label"),
]