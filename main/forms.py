import re

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# from .models import *


def senha_forte(password):
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')

    if not regex.match(password):
        raise ValidationError()


class formRegistro(forms.ModelForm):
    cidade = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Digite sua cidade'
        }),
    )
    estado = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Digite seu estado'
        }),
    )
    senha = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Digite sua senha'
        }),
    )
    confirmar = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirme sua senha'
        }),
        validators=[senha_forte]
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            # 'password',
        ]

        labels = {
            'username': 'Usuário',
            'first_name': 'Primeiro nome',
            'last_name': 'Último nome',
            'cidade': 'Cidade',
            'estado': 'Estado',
            'email': 'E-mail',
            'senha': 'Senha',
            'confirmarSenha': 'Confirmar senha',
        }

        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Digite seu usuário'
            }),
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Digite seu primeiro nome'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Digite seu último nome'
            }),
            'email': forms.TextInput(attrs={
                'placeholder': 'Digite seu e-mail'
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Digite sua senha'
            }),
        }

    # def clean(self):
    #     cleaned_data = super().clean()
    #     password = cleaned_data.get('password')
    #     password2 = cleaned_data.get('confirmar')

    #     if password != confirmar:
    #         raise ValidationError({
    #             'password': 'As senhas precisam ser iguais',
    #             'confirmar': 'As senhas precisam ser iguais',
    #         })
