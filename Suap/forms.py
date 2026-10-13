from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class CadastroForm(UserCreationForm):
    nome_completo = forms.CharField(
        label='Nome completo',
        max_length=150
    )

    email = forms.EmailField(label='E-mail')

    foto_perfil = forms.ImageField(
        label='Foto de perfil',
        required=False
)

    class Meta:
        model = Usuario
        fields = [
            'nome_completo',
            'email',
            'foto_perfil',
            'password1',
            'password2'
        ]

def clean_email(self):
        email = self.cleaned_data['email'].lower().strip()

        if Usuario.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(
                'Este e-mail já está cadastrado.'
            )

        return email

def save(self, commit=True):
    usuario = super().save(commit=False)

    email = self.cleaned_data['email'].lower().strip()

    usuario.username = email
    usuario.email = email
    usuario.nome_completo = self.cleaned_data['nome_completo']
    usuario.foto_perfil = self.cleaned_data.get('foto_perfil')

    if commit:
        usuario.save()

    return usuario
