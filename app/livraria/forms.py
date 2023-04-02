from django import forms
from app.livraria.models import Livro, Autor

class LivroForm(forms.ModelForm):
  class Meta:
    model = Livro
    exclude = []
    labels={
      'titulo': 'Título',
      'genero_literario': 'Gênero Literário',
      'preco': 'Preço'
    }
    widgets = {
      'titulo': forms.TextInput(attrs={'class': 'forms__input'}),
      'autor': forms.Select(attrs={'class': 'forms__input'}),
      'capa': forms.FileInput(attrs={'class': 'forms__input'}),
      'genero_literario': forms.Select(attrs={'class': 'forms__input'}),
      'sinopse': forms.Textarea(attrs={'class': 'forms__input'}),
      'preco': forms.NumberInput(attrs={'class': 'forms__input'}),
      'desconto': forms.NumberInput(attrs={'class': 'forms__input'}),
    }
    
    
class AutorForm(forms.ModelForm):
  class Meta:
    model = Autor
    exclude = []
    labels = {
      'genero_literio': 'Gênero Literário',
      'frase_destaque': 'Frase em destaque no perfil'
    }
    widgets = {
      'nome': forms.TextInput(attrs={'class': 'forms__input'}),
      'foto': forms.FileInput(attrs={'class': 'forms__input'}),
      'nascimento': forms.DateInput(
        format = '%d/%m/%Y',
        attrs={
          'type': 'date',
          'class': 'forms__input'
        }
      ), 
      'morte': forms.DateInput(
        format = '%d/%m/%Y',
        attrs={
          'type': 'date',
          'class': 'forms__input'
        }
      ),
      'biografia': forms.Textarea(attrs={'class': 'forms__input'}),
      'genero_literario': forms.Select(attrs={'class': 'forms__input'}),
      'frase_destaque': forms.TextInput(attrs={'class': 'forms__input'})
    }
  