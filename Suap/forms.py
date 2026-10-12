from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class CadastroForm(UserCreationForm):
    nome_completo = forms.CharField(
        label='Nome completo',
        max_length=150
    )

    email = forms.EmailField(label='E-mail')

    class Meta:
        model = Usuario
        fields = [
            'nome_completo',
            'email',
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
        usuario.username = self.cleaned_data['email'].lower().strip()
        usuario.email = self.cleaned_data['email'].lower().strip()
        usuario.nome_completo = self.cleaned_data['nome_completo']
        if commit:
            usuario.save()
        return usuario
