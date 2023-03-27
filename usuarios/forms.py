from django import forms

class LoginForm(forms.Form):
  email = forms.EmailField(
    max_length=100,
    required=True,
    label='Email',
    widget=forms.TextInput({
      "class": 'forms__input',
      "placeholder": "exemplo@gmail.com"
    })
  )
  senha = forms.CharField(
    max_length=70,
    required=True,
    label="Senha",
    widget=forms.PasswordInput({
      "class": 'forms__input'
    })
  )
  
class CadastroForm(forms.Form):
  email = forms.EmailField(
    max_length=100,
    required=True,
    label='Email',
    widget=forms.TextInput({
      "class": 'forms__input',
      "placeholder": "exemplo@gmail.com"
    })
  )
  nome_de_usuario = forms.CharField(
    max_length=100,
    required=True,
    label="Nome de usuário",
    widget=forms.TextInput({
      "class": 'forms__input',
      "placeholder": "Ex.: Jóse Dávila"
    })
  )
  nascimento = forms.DateField(
    required=True,
    label="Data de nascimento",
    widget=forms.DateInput({
      "class": 'forms__input',
      "placeholder": "dd/mm/yyyy",
      "type": "date",
    })
  )
  senha = forms.CharField(
    max_length=70,
    required=True,
    label="Senha",
    widget=forms.PasswordInput({
      "id": "userPasswordInput",
      "class": 'forms__input',
      "placeholder": "Exemplo1234+"
    })
  )
  senha2 = forms.CharField(
    max_length=70,
    required=True,
    label="Confirme sua senha",
    widget=forms.PasswordInput({
      "id": "userPasswordInput",
      "class": 'forms__input',
      "placeholder": "Exemplo1234+"
    })
  )
  