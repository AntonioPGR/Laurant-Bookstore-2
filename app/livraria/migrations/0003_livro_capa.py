# Generated by Django 4.1.7 on 2023-03-25 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livraria', '0002_alter_autor_biografia_alter_livro_sinopse'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='capa',
            field=models.ImageField(default='', upload_to='livros/%d-%b'),
            preserve_default=False,
        ),
    ]
