from django.urls import path
from . import views


urlpatterns = [
    #path('',views.index,name = 'index'),
    path('',views.home,name ='home'),
    path('about/',views.about__us),
    path('contact/',views.contact__form),
]