from .import views
from django.urls import path

urlpatterns = [
    path('firedect',views.firedect,name="home"),
]
