from usuarios.forms import CadastroForm, LoginForm
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def cadastrar_usuario(request, respostas_form:CadastroForm):
  if not respostas_form.is_valid():
    messages.error(request, " Formulário invalido!!")
    return redirect('cadastrar')

  if respostas_form['senha'].value() != respostas_form['senha2'].value():
    messages.error(request, " As senhas devem ser iguais!!")
    return redirect('cadastrar')
  
  nome = respostas_form['nome_de_usuario'].value()
  email = respostas_form['email'].value()
  # nascimento = respostas_form['nascimento'].value()
  senha = respostas_form['senha'].value()
  
  if User.objects.filter(email=email).exists():
    messages.error(request, " Já existe um usuário cadastrado com esse email!!")
    return redirect('cadastrar')
  
  if User.objects.filter(username=nome).exists():
    messages.error(request, " Já existe um usuário cadastrado com esse nome!!")
    return redirect('cadastrar')
  
  usuario = User.objects.create_user(password=senha, username=nome, email=email)
  usuario.save()
  
  messages.success(request, f"Olá {nome}, seu cadastro foi efetuado com sucesso!")
  return redirect('entrar')


def logar_usuario(request, respostas_form:LoginForm):
  if not respostas_form.is_valid():
    messages.error(request, " Formulário invalido!!")
    return redirect("entrar")
    
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