from django import forms
from django.contrib.auth.forms import User, UserCreationForm
#  from django.core.exceptions import ValidationError
from django.db import transaction

from .models import Usuario

# class formRegistro(forms.ModelForm):
#     cidade = forms.CharField(
#         required=True,
#         widget=forms.TextInput(attrs={
#             'placeholder': 'Digite sua cidade'
#         }),
#     )
#     estado = forms.CharField(
#         required=True,
#         widget=forms.TextInput(attrs={
#             'placeholder': 'Digite seu estado'
#         }),
#     )
#     senha = forms.CharField(
#         required=True,
#         widget=forms.PasswordInput(attrs={
#             'placeholder': 'Digite sua senha'
#         }),
#     )
#     confirmar = forms.CharField(
#         required=True,
#         widget=forms.PasswordInput(attrs={
#             'placeholder': 'Confirme sua senha'
#         }),
#         validators=[senha_forte]
#     )

#     class Meta:
#         model = User
#         fields = [
#             'first_name',
#             'last_name',
#             'username',
#             'email',
#             # 'password',
#         ]

#         labels = {
#             'username': 'Usuário',
#             'first_name': 'Primeiro nome',
#             'last_name': 'Último nome',
#             'cidade': 'Cidade',
#             'estado': 'Estado',
#             'email': 'E-mail',
#             'senha': 'Senha',
#             'confirmarSenha': 'Confirmar senha',
#         }

#         widgets = {
#             'username': forms.TextInput(attrs={
#                 'placeholder': 'Digite seu usuário'
#             }),
#             'first_name': forms.TextInput(attrs={
#                 'placeholder': 'Digite seu primeiro nome'
#             }),
#             'last_name': forms.TextInput(attrs={
#                 'placeholder': 'Digite seu último nome'
#             }),
#             'email': forms.TextInput(attrs={
#                 'placeholder': 'Digite seu e-mail'
#             }),
#             'password': forms.PasswordInput(attrs={
#                 'placeholder': 'Digite sua senha'
#             }),
#         }

# def clean(self):
#     cleaned_data = super().clean()
#     password = cleaned_data.get('password')
#     password2 = cleaned_data.get('confirmar')

#     if password != confirmar:
#         raise ValidationError({
#             'password': 'As senhas precisam ser iguais',
#             'confirmar': 'As senhas precisam ser iguais',
#         })


class formRegistro(UserCreationForm):
    email = forms.EmailField(label='Email', required=True)
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirmar senha', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def conferir_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Senhas diferentes")
        return password2

    @transaction.atomic
    def salvar(self):
        usuario = super().save(commit=False)
        usuario.email = self.cleaned_data['email']
        usuario.set_password(self.cleaned_data["password1"])
        usuario.is_Usuario = True
        usuario.save()
        usuario = Usuario.objects.create(usuario=usuario)
        return usuario
