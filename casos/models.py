from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class CasoClinico(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    data_publicacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField()
    diagnostico = models.TextField(blank=True, null=True)
    tratamento = models.TextField(blank=True, null=True)
    conclusao = models.TextField(blank=True, null=True)
    publicado = models.BooleanField(default=True)
    curtidas = models.ManyToManyField(User, related_name='casos_curtidos', blank=True)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['-data_publicacao']

    def total_curtidas(self):
        return self.curtidas.count()

class Comentario(models.Model):
    caso = models.ForeignKey(CasoClinico, related_name='comentarios', on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Comentário de {self.autor.username} no caso {self.caso.titulo}'

