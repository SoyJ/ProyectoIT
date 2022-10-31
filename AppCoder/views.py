from difflib import restore
from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso

# Create your views here.
def curso(self):
    curso = Curso(nombre = 'Python', camada = 37360)
    curso.save()
    texto= f"Curso creado : {curso.nombre} {curso.camada}"
    return HttpResponse (texto)
