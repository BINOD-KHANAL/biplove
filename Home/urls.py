from django.contrib import admin
from django.urls import path,include
from Home import views


urlpatterns = [
    
 path("",  views.index,name='Index'), 
 path("index",views.index,name='Home'),
    
 path("about", views.about, name='about'), 
 path("contact",views.contact,name='contact')
  
]