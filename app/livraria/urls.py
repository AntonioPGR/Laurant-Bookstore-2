from django.urls import path
from app.livraria import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('livro/<int:livro_id>', views.livro, name='livro'),
    path('autor/<int:autor_id>', views.autor, name='autor'),
    path('buscar/livro', views.buscar_livros, name='buscar-livros'),
    path('novo/<str:item_label>', views.novo_item, name='novo-item'),
    path('editar/<str:item_label>/<int:item_id>', views.editar_item, name='editar-item'),
    path('deletar/<str:item_label>/<int:item_id>', views.deletar_item, name='deletar-item')
]
