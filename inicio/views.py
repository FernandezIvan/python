from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from django.shortcuts import render

def inicio(request):
    return render(request,'inicio/inicio.html')



def registro(request):
    return HttpResponse('<h2>registrate<h2>')



def crear_usuario(request,nombre,apellido,mail,edad,genero):
    
    usuario= usuario(nombre=nombre, apellido=apellido, mail=mail, edad=edad,genero=genero )
    usuario.save()
    diccionario={
        'usuario':usuario,
    }
    return render (request,'inicio/crear_usuario.html',diccionario)
    
