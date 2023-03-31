from django.shortcuts import render, get_object_or_404, redirect
from os.path import join
from app.livraria.models import Autor, Livro

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
  
  livros = Livro.objects.filter(genero_literario=livro.genero_literario).exclude(pk=livro.id)
  
  return render(request, join(BASE_PATH, 'livro.html'), {
    "livro": livro,
    "livros": livros
  })


def autor(request, autor_id):
  autor = get_object_or_404(Autor, pk=autor_id)
  livros = Livro.objects.filter(autor=autor.pk)
  return render(request, join(BASE_PATH, 'autor.html'), {
    "autor": autor,
    "livros": livros
  })
  
  
def buscar(request, type):
  autores = ''
  livros = ''
  
  if type == 'autores':
    autores = Autor.objects.order_by("genero_literario")
  elif type == 'livros':
    livros = Livro.objects.order_by("genero_literario")
  else:
    return redirect('buscar', type='livros')
    
  search_query = ''
  if 'search_query' in request.GET:
    search_query = request.GET["search_query"]
    if search_query and livros:
      livros = livros.filter(titulo__icontains=search_query)
      
  return render(request, join(BASE_PATH, 'pesquisa.html'), {"autores":autores, "livros":livros, "searchQuery":search_query})