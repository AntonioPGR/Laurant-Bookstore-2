from django.contrib import admin
from livraria.models import GeneroLiterario, Autor, Livro


class ListarGenero(admin.ModelAdmin): 
  search_fields = ("nome", )
  empty_value_display = "-vazio-"
  actions_on_bottom = True
  list_display_links = ("id", "nome")
  list_display = ("id", "nome")
  list_per_page=20
  
admin.site.register(GeneroLiterario, ListarGenero)


class ListarAutores(admin.ModelAdmin):
  search_fields = ("nome", )
  empty_value_display = "-empty-"
  actions_on_bottom = True
  list_display = ("id", "nome", "nascimento", "genero_literario")
  list_per_page = 20
  list_display_links = ("id", "nome", "genero_literario")
  list_filter = ("genero_literario", )
  
admin.site.register(Autor, ListarAutores)


class ListarLivros(admin.ModelAdmin):
  search_fields = ("nome", "autor")
  empty_value_display = "-empty-"
  actions_on_bottom = True
  list_display = ("id", "titulo", "autor", "preco", "desconto", "genero_literario")
  list_per_page = 20
  list_display_links = ("id", "titulo", "autor")
  list_filter = ("autor", "desconto")
  list_editable = ("desconto", )
  
admin.site.register(Livro, ListarLivros)
