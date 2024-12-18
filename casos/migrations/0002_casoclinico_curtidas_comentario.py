# Generated by Django 5.1.3 on 2024-11-20 20:44

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='casoclinico',
            name='curtidas',
            field=models.ManyToManyField(blank=True, related_name='casos_curtidos', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conteudo', models.TextField()),
                ('data_publicacao', models.DateTimeField(default=django.utils.timezone.now)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('caso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='casos.casoclinico')),
            ],
        ),
    ]
