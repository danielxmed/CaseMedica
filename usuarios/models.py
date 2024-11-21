from django.db import models
from django.contrib.auth.models import User
import os
from django.conf import settings

def user_directory_path(instance, filename):
# O arquivo será salvo em MEDIA_ROOT/perfil_pictures/user_<id>/<filename>
    return f'perfil_pictures/user_{instance.user.id}/{filename}'

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    formacao = models.CharField(max_length=200, blank=True)
    afiliacoes = models.CharField(max_length=200, blank=True)
    especialidades = models.CharField(max_length=200, blank=True)
    bio = models.TextField(blank=True)
    seguindo = models.ManyToManyField('self', symmetrical=False, related_name='seguidores', blank=True)
    imagem_perfil = models.ImageField(upload_to=user_directory_path, default='media/perfil_pictures/default.jpg', blank=True)

    def __str__(self):
        return f'Perfil de {self.user.username}'
    
    def total_seguidores(self):
        return self.seguidores.count()

    def total_seguindo(self):
        return self.seguindo.count()
    
    
