from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
  path("", views.log, name="log"),
  path("home", views.home, name="home"),
  path("logout", views.logout_user, name="logout"),
  path("instrucciones", views.intrucciones, name="instrucciones"),
  path("niveles", views.niveles, name="niveles"),
  path("coms", views.coms, name="coms"),
  path("nivel_1", views.nivel_1, name="nivel_1"),
  path("nivel_2", views.nivel_2, name="nivel_2"),
  path("nivel_3", views.nivel_3, name="nivel_3"),
   
]