# Generated by Django 5.1.3 on 2024-11-21 17:27

import usuarios.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_remove_perfil_seguidores_perfil_seguindo'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='imagem_perfil',
            field=models.ImageField(blank=True, default='perfil_pictures/default.jpg', upload_to=usuarios.models.user_directory_path),
        ),
    ]