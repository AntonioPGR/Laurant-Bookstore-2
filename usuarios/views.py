from django.shortcuts import render, redirect
from usuarios import forms
from usuarios.utils import cadastrar_usuario, logar_usuario, sair_usuario

def cadastrar(request):

  if request.user.is_authenticated:
    return redirect('inicio')
  
  cadastro_form = forms.CadastroForm()
  
  if request.method == 'POST' and request.POST:
    respostas_form = forms.CadastroForm(request.POST)
    cadastro_result = cadastrar_usuario(request, respostas_form)
    if cadastro_result: return cadastro_result
  
  return render(request, 'usuarios/cadastrar.html', {
    "cadastro": cadastro_form,
  })


def entrar(request):
  
  if request.user.is_authenticated:
    return redirect('inicio')

  login_form = forms.LoginForm()
  if request.method == 'POST' and request.POST:
    respostas_form = forms.LoginForm(request.POST)
    return logar_usuario(request, respostas_form)
    
  
  return render(request, 'usuarios/entrar.html', {
    "login": login_form,
  })


def sair(request):
  if not request.user.is_authenticated:
    return redirect('inicio')
  
  return sair_usuario(request)