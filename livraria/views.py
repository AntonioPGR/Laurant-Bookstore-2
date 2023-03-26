from django.shortcuts import render, get_object_or_404
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
  
  
def livro(request, livro_id):
  livro = get_object_or_404(Livro, pk=livro_id)
  return render(request, join(BASE_PATH, 'livro.html'), {
    "livro": livro
  })


def autor(request, autor_id):
  autor = get_object_or_404(Autor, pk=autor_id)
  return render(request, join(BASE_PATH, 'autor.html'), {
    "autor": autor
  })
  
def buscar(request):
  livros = Livro.objects.order_by("genero_literario")
  search_query = ''
  if 'search_query' in request.GET:
    search_query = request.GET["search_query"]
    if search_query:
      livros = livros.filter(titulo__icontains=search_query)
  return render(request, join(BASE_PATH, 'pesquisa.html'), {"livros":livros, "searchQuery":search_query})