from django.urls import path;
from usuarios import views

urlpatterns = [
  path('entrar', views.entrar, name='entrar')
]