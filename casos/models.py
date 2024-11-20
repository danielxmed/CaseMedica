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

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['-data_publicacao']