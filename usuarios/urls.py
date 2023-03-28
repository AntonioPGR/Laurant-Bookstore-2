from django.urls import path;
from usuarios import views

urlpatterns = [
  path('entrar', views.entrar, name='entrar'),
  path('cadastrar', views.cadastrar, name="cadastrar"),
  path('sair', views.sair, name="sair")
]