# Generated by Django 5.1.3 on 2024-11-20 22:21

import casos.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casos', '0002_casoclinico_curtidas_comentario'),
    ]

    operations = [
        migrations.AddField(
            model_name='casoclinico',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to=casos.models.upload_to),
        ),
        migrations.AddField(
            model_name='casoclinico',
            name='legenda_imagem',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]