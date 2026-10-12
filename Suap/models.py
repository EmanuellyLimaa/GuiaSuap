from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    nome_completo = models.CharField(
        max_length=150,
        verbose_name='Nome completo'
    )

    def __str__(self):
        return self.email or self.username

