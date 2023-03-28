from django.shortcuts import render
from usuarios import forms
from usuarios.utils import cadastrar_usuario, logar_usuario, sair_usuario

def cadastrar(request):

  cadastro_form = forms.CadastroForm()
  
  if request.method == 'POST' and request.POST:
    respostas_form = forms.CadastroForm(request.POST)
    return cadastrar_usuario(request, respostas_form)
  
  return render(request, 'usuarios/cadastrar.html', {
    "cadastro": cadastro_form,
  })


def entrar(request):

  login_form = forms.LoginForm()
  if request.method == 'POST' and request.POST:
    respostas_form = forms.LoginForm(request.POST)
    return logar_usuario(request, respostas_form)
    
  
  return render(request, 'usuarios/entrar.html', {
    "login": login_form,
  })


def sair(request):
  return sair_usuario(request)