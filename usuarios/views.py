from django.shortcuts import render
from usuarios import forms


def entrar(request):

  login = forms.LoginForm()
  cadastro = forms.CadastroForm()
  
  return render(request, 'usuarios/entrar.html', {
    "cadastro": cadastro,
    "login": login,
  })
