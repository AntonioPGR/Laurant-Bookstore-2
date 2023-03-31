from django.shortcuts import render, redirect
from app.usuarios import forms
from app.usuarios.utils import cadastrar_usuario, logar_usuario, sair_usuario

def cadastrar(request):

  if request.user.is_authenticated:
    return redirect('inicio')
  
  if request.method == 'POST' and request.POST:
    cadastro_form = forms.CadastroForm(request.POST)
    if cadastro_form.is_valid():
      return cadastrar_usuario(request, cadastro_form)
  else:
    cadastro_form = forms.CadastroForm()
  
  return render(request, 'usuarios/cadastrar.html', {
    "cadastro": cadastro_form,
  })


def entrar(request):
  
  if request.user.is_authenticated:
    return redirect('inicio')

  if request.method == 'POST' and request.POST:
    login_form = forms.LoginForm(request.POST)
    if login_form.is_valid():
      return logar_usuario(request, login_form)
  else:
    login_form = forms.LoginForm()
    
  return render(request, 'usuarios/entrar.html', {
    "login": login_form,
  })


def sair(request):
  if not request.user.is_authenticated:
    return redirect('inicio')
  
  return sair_usuario(request)