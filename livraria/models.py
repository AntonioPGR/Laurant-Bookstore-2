from django.db import models


class GeneroLiterario(models.Model):
  nome = models.CharField(max_length=20)
  
  def __str__(self) -> str:
    return self.nome


class Autor(models.Model):
  
  nome = models.CharField(max_length=30, blank=False, null=False)
  foto = models.ImageField(upload_to="autores/%d-%b")
  biografia = models.TextField(max_length=1000, blank=False, null=False)
  nascimento = models.DateField(verbose_name="Data de nascimento", blank=False, null=False)
  morte = models.DateField(verbose_name="Data de morte", blank=True, null=True, help_text="Caso ainda vivo, deixar em branco")
  genero_literario = models.ForeignKey(GeneroLiterario, on_delete=models.SET_NULL, null=True, blank=True)
  frase_destaque = models.TextField(verbose_name="Frase exibida no perfil", max_length=200, blank=True, null=True)

  def __str__(self) -> str:
    return self.nome


class Livro(models.Model):
  
  titulo = models.CharField(max_length=100, blank=False, null=False)
  autor = models.ForeignKey(Autor, on_delete=models.SET_NULL, null=True, blank=False)
  preco = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
  desconto = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
  sinopse = models.TextField(max_length=1000, blank=False, null=False)
  genero_literario = models.ForeignKey(GeneroLiterario, on_delete=models.SET_NULL, null=True, blank=True)
  
  def __str__(self) -> str:
    return self.titulo