from django.shortcuts import render
from os.path import join

BASE_PATH = 'livraria/'

def inicio(request):
  return render(request, join(BASE_PATH, 'inicio.html'))
