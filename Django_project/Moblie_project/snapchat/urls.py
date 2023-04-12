from django.contrib import admin 
from django.urls import path
from . import views

urlpatterns = [
    path('snapchat/',views.snapchat,name='snapchat'),
   # path('<str=name>',views.greet,name='greet'),
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('s1',views.s1 ,name='s1'),
    path('date',views.date, name='date'),
]
