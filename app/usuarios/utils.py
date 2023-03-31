from app.usuarios.forms import CadastroForm, LoginForm
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def cadastrar_usuario(request, respostas_form:CadastroForm):
    nome = respostas_form['nome_de_usuario'].value()
    email = respostas_form['email'].value()
    # nascimento = respostas_form['nascimento'].value()
    senha = respostas_form['senha'].value()
    
    usuario = User.objects.create_user(password=senha, username=nome, email=email)
    usuario.save()
    
    messages.success(request, f"Olá {nome}, seu cadastro foi efetuado com sucesso!")
    return redirect('entrar')


def logar_usuario(request, respostas_form:LoginForm):
  username = respostas_form['username'].value()
  senha = respostas_form['senha'].value()
  usuario = authenticate(
    request,
    username=username,
    password=senha
  )
  
  if usuario is None:
    messages.error(request, " Informações incorretas! verifique seu email e/ou senha e tente novamente")
    return redirect('entrar')
  
  login(
    request,
    usuario
  )
  messages.success(request, f"Olá novamente {username}, seu login foi efetuado com sucesso!")
  return redirect('inicio')
  
  
def sair_usuario(request):
  messages.success(request, "Logout efetuado com sucesso!")
  logout(request)
  return redirect('entrar')