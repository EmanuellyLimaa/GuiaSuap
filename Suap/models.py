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
<<<<<<< HEAD
        return self.email or self.username
=======
        return self.email or self.username

class tutorias(models.Model):
    titulo = models.CharField(max_length=200, verbose_name='Título')
    descricao = models.TextField(verbose_name='Descrição')
    video_url = models.URLField( blank=True, verbose_name='Link do vídeo')

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizando_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['titulo']
        verbose_name = 'Tutorial'
        verbose_name_plural = 'Tutoriais'
>>>>>>> a61d7a1eff0296df0e8344581b60a3e8d21d1fe5
