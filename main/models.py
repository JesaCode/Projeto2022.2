from django.contrib.auth.models import User
from django.db import models


class Troca(models.Model):
    autor = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )
    darFigurinhas = models.CharField(max_length=50)
    recebeFigurinhas = models.CharField(max_length=10)
    valor = models.FloatField(max_length=10)
    descricao = models.CharField(max_length=165)
    ativa = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Figurinha(models.Model):
    codigo = models.CharField(max_length=6)
    nomeFigurinha = models.CharField(max_length=50)
    tipoFigurinha = models.CharField(max_length=10)
    trocasFigurinha = models.ForeignKey(
        Troca, on_delete=models.SET_NULL, null=True
    )

# class UUser(models.Model):
#    nome = models.CharField(max_length=6)
#    email = models.EmailField(max_length=50)
#    senha = models.CharField(max_length=10)
#    figurinhas = models.ForeignKey(
#        Figurinha, on_delete=models.SET_NULL, null=True
#    )
#    Trocas = models.ForeignKey(
#        Troca, on_delete=models.SET_NULL, null=True
#    )
#    created_at = models.DateTimeField(auto_now_add=True)


class Usuario(models.Model):
    usuarioSistema = models.CharField(max_length=30)
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    cidade = models.CharField(max_length=30)
    estado = models.CharField(max_length=30)
    # figurinhas = models.CharField(max_length=3)
    senha = models.CharField(max_length=30)
    confirmarSenha = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.nome
