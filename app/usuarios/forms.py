from django import forms
from re import search
from django.contrib.auth.models import User

class LoginForm(forms.Form):
  username = forms.CharField(
    max_length=100,
    required=True,
    label='Nome de usuário',
    widget=forms.TextInput({
      "class": 'forms__input',
    })
  )
  senha = forms.CharField(
    max_length=70,
    required=True,
    label="Senha",
    widget=forms.PasswordInput({
      "class": 'forms__input',
    })
  )
  
  def clean_senha(self):
    senha = self.cleaned_data.get("senha")
    nome = self.cleaned_data.get("username")
    if senha:
      if not User.objects.filter(username=nome, password=senha):
        raise forms.ValidationError('Senha e/ou usuario incorretos')
      return senha
    
    raise forms.ValidationError('O campo "senha" não pode ficar vazio')
  
  def clean_username(self):
    nome = self.cleaned_data.get("username")
    if nome:
      if not User.objects.filter(username=nome).exists():
        raise forms.ValidationError('Não foi encontrado nenhum usuário com esse nome')
      return nome
    
    raise forms.ValidationError('O campo "nome" não pode ficar vazio')
  
  
class CadastroForm(forms.Form):
  email = forms.EmailField(
    max_length=100,
    required=True,
    label='Email',
    widget=forms.TextInput({
      "class": 'forms__input',
      "placeholder": "exemplo@gmail.com",
    })
  )
  nome_de_usuario = forms.CharField(
    max_length=100,
    required=True,
    label="Nome de usuário",
    widget=forms.TextInput({
      "class": 'forms__input',
      "placeholder": "Ex.: Jóse Dávila",
    })
  )
  senha = forms.CharField(
    max_length=70,
    required=True,
    label="Senha",
    widget=forms.PasswordInput({
      "id": "userPasswordInput",
      "class": 'forms__input',
      "placeholder": "Exemplo1234+",
    })
  )
  senha2 = forms.CharField(
    max_length=70,
    required=True,
    label="Confirme sua senha",
    widget=forms.PasswordInput({
      "id": "userPasswordInput",
      "class": 'forms__input',
      "placeholder": "Exemplo1234+",
    })
  )
  
  def clean_email(self):
    email = self.cleaned_data.get('email')
    if email:
      if "@" not in email:
        raise forms.ValidationError('Insira um email valido')
      if User.objects.filter(email=email).exists():
        raise forms.ValidationError('Este email já está cadastrado em nossso site')
      return email
      
    raise forms.ValidationError('O campo "email" não pode ficar vazio')
  
  def clean_nome_de_usuario(self):
    nome = self.cleaned_data.get('nome_de_usuario')
    if nome:
      if " " in nome:
        raise forms.ValidationError('Não são permitidos espaços no nome')
      if search(r'[^\w\s]', nome):
        raise forms.ValidationError('Não são permitidos caracteres especiais no nome')
      if User.objects.filter(username=nome).exists():
        raise forms.ValidationError('Esse nome de usuário já está sendo utilizado')
      return nome
    
    raise forms.ValidationError('O campo "nome" não pode ficar vazio')
  
  def clean_senha(self):
    senha = self.cleaned_data.get('senha')
    
    if senha: 
      if len(senha) < 8:
        raise forms.ValidationError("A senha deve conter no minimo 8 caracteres")
      if not search(r'[a-z]', senha):  
        raise forms.ValidationError("A senha deve conter ao minimo 1 letra minúscula")
      if not search(r'[A-Z]', senha):
        raise forms.ValidationError("A senha deve conter ao minimo 1 letra maiúscula")
      if not search(r'[\d]', senha):
        raise forms.ValidationError("A senha deve conter ao minimo 1 número")
      if not search(r'[^\w\s]', senha):
        raise forms.ValidationError("A senha deve conter ao minimo 1 caracter especial (+-*&$%=_?...)")
      return senha
      
    raise forms.ValidationError('O campo "senha" não pode ficar vazio')
  
  def clean_senha2(self):
    senha = self.cleaned_data.get('senha')
    senha2 = self.cleaned_data.get('senha2')

    if senha2:
      if senha != senha2:
        raise forms.ValidationError('As senhas não são iguais')
      else:
        return senha2
      
    raise forms.ValidationError('O campo "confirme sua senha" não pode ficar vazio ')