from django.shortcuts import render
from os.path import join
from livraria.models import Autor, Livro

BASE_PATH = 'livraria/'

def inicio(request):
  
  livros = Livro.objects.all()[:6]
  autores = Autor.objects.all()[:4]
  
  return render(request, join(BASE_PATH, 'inicio.html'), {
    "livros": livros,
    "autores": autores
  })
