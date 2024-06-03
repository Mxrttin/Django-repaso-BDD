from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index , name="index"),
    path('listadosSQL',views.listadosSQL ,name="listadoSQL")
]