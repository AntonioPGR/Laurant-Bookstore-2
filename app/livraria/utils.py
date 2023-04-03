from app.livraria.models import Autor, Livro, GeneroLiterario
from app.livraria.forms import LivroForm, AutorForm, GeneroLiterarioForm


# def filtrar_resultados(data, get_params):
#   pass


def definir_item(item_label):
  if item_label == 'livro':
    form = LivroForm
    classe_pertencente = Livro
  elif item_label == 'autor':
    form = AutorForm
    classe_pertencente = Autor
  elif item_label == 'genero':
    form = GeneroLiterarioForm
    classe_pertencente = GeneroLiterario
  else:
    return None
  
  return {
    'classe_pertencente': classe_pertencente,
    'form': form
  }


def encontrar_item(classe_pertencente, id):
  item = classe_pertencente.objects.get(id=id)
  return item