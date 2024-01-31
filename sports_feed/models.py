from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    titulo = models.CharField(max_length=80)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo

    