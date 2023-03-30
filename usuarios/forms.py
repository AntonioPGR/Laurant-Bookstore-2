from django import forms

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
  
  
  def clean_senha2(self):
    senha = self.cleaned_data.get('senha')
    senha2 = self.cleaned_data.get('senha2')

    if senha and senha2:
        if senha != senha2:
            raise forms.ValidationError('Senhas não são iguais')
        else:
            return senha2