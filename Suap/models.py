
from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    nome_completo = models.CharField(
        max_length=150,
        verbose_name='Nome completo'
    )

    foto_perfil = models.ImageField(
        upload_to='fotos_perfil/',
        blank=True,
        null=True,
        verbose_name='Foto de perfil'
    )

    def __str__(self):
        return self.email or self.username


class Tutorial(models.Model):
    titulo = models.CharField(
        max_length=200,
        verbose_name='Título'
    )
    descricao = models.TextField(
        verbose_name='Descrição'
    )
    video_arquivo = models.FileField(
        upload_to='tutoriais/',
        blank=True,
        null=True,
        verbose_name='Arquivo do vídeo'
    )
    publicado = models.BooleanField(
        default=True,
        verbose_name='Disponível para os alunos'
    )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['titulo']
        verbose_name = 'Tutorial'
        verbose_name_plural = 'Tutoriais'

    def __str__(self):
        return self.titulo