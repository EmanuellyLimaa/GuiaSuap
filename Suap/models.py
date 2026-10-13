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

