from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    formacao = models.CharField(max_length=200, blank=True)
    afiliacoes = models.CharField(max_length=200, blank=True)
    especialidades = models.CharField(max_length=200, blank=True)
    bio = models.TextField(blank=True)
    seguindo = models.ManyToManyField('self', symmetrical=False, related_name='seguidores', blank=True)

    def __str__(self):
        return f'Perfil de {self.user.username}'
    
    def total_seguidores(self):
        return self.seguidores.count()

    def total_seguindo(self):
        return self.seguindo.count()