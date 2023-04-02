from django.urls import path
from app.livraria import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('livro/<int:livro_id>', views.livro, name='livro'),
    path('autor/<int:autor_id>', views.autor, name='autor'),
    path('buscar/<str:type>', views.buscar, name='buscar'),
    path('novo/<str:item>', views.novo_item, name='novo-item')
]
