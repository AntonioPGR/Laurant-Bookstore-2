from django.shortcuts import render, get_object_or_404, redirect
from os.path import join
from app.livraria.models import Autor, Livro
from app.livraria.forms import LivroForm
from django.contrib import messages
from app.livraria.utils import definir_item, encontrar_item, filtrar_resultados

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
  
  
def buscar_livros(request):
  
  resultado_completo = Livro.objects
  resultado_filtrado = resultado_completo
  
  search_query = request.GET['search_query']
  if search_query:
    resultado_filtrado = resultado_filtrado.filter(titulo__contains=search_query)
    if len(resultado_filtrado) == 0:
      resultado_filtrado = resultado_filtrado.filter(autor__nome__contains=search_query)
    
  # genero_literario = request.GET['genero_literario']
  # if request.GET['genero_literario']:
  #   resultado_filtrado = resultado_filtrado.filter(genero_literario__id=genero_literario.id)
      
  return render(request, join(BASE_PATH, 'pesquisa.html'), {
    "livros": resultado_filtrado,
    "pesquisa": search_query,
    # "genero_literario": genero_literario
  })


def novo_item(request, item_label):
  if not request.user.is_authenticated:
    messages.error(request, f"Faça login para poder adicionar {item_label} a plataforma")
    return redirect('inicio')
  
  response = definir_item(item_label)
  
  if not response:
    messages.error(request, f"Essa página de cadastro não existe! {item_label}")
    return redirect('inicio')
  
  form = response['form']
  
  if request.method == 'POST' and request.POST:
    form = response.form(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      messages.success(request, f"Seu novo {item_label} foi cadastrado com sucesso!")
      return redirect('inicio')
  
  return render(request, join(BASE_PATH, 'novo_item.html'), {
    "form": form,
    "item": item_label
  })  
  
  
def editar_item(request, item_label, item_id):
  # verificar autenticação
  if not request.user.is_authenticated:
    messages.error(request, f"Faça login para poder deletar {item_label} a plataforma")
    return redirect('inicio')
  
  # definir o tipo do item e a qual classe pertence
  response = definir_item(item_label)
  if not response:
    messages.error(request, f"Essa página de cadastro não existe! {item_label}")
    return redirect('inicio')
  
  # definir o item especificamente
  item = encontrar_item(response['classe_pertencente'], item_id)
  
  #define o formulário
  form = response['form'](instance=item)
  
  # verificar respostar
  if request.method == 'POST' and request.POST:
    form = form(request.POST, request.FILES, instance=item)
    if form.is_valid():
      form.save()
      messages.success(request, f"Seu novo {item_label} foi editado com sucesso!")
      return redirect('inicio')
  
  return render(request, join(BASE_PATH, 'editar_item.html'), {
    'form': form,
    'item_id': item_id,
    'label': item_label
  })
  

def deletar_item(request, item_label, item_id):
  # verificar autenticação
  if not request.user.is_authenticated:
    messages.error(request, f"Faça login para poder deletar {item_label} a plataforma")
    return redirect('inicio')
  
  # definir o tipo do item e a qual classe pertence
  response = definir_item(item_label)
  if not response:
    messages.error(request, f"Essa página de cadastro não existe! {item_label}")
    return redirect('inicio')
  
  # definir o item especificamente
  item = encontrar_item(response['classe_pertencente'], item_id)
  item.delete()
  messages.success(request, f"Sua {item_label} foi deletado com sucesso")
  return redirect('inicio')