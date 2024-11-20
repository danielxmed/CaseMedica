from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    formacao = models.CharField(max_length=200)
    afiliacoes = models.CharField(max_length=200)
    especialidades = models.CharField(max_length=200)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f'Perfil de {self.user.username}'