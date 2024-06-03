from django.shortcuts import render

from .models import Genero,ALumno

# Create your views here.

def index (request):
    alumnos=ALumno.objects.all()
    context={"alumnos":alumnos}
    return render (request,"alumnos/index.html",context)


def listadoSQL(request):
    alumnos=ALumno.objects.raw('SELECT')