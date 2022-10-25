# from django.contrib import messages
# from django.contrib.auth import authenticate
import re

from django.http import HttpResponse
from django.shortcuts import render

from .models import Usuario

# from .models import Usuario


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        return render(request, 'index.html')

    return render(request, 'login.html')


def registro_cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro/cadastro.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        cidade = request.POST.get('cidade')
        estado = request.POST.get('estado')
        senha = request.POST.get('senha')
        confirmarSenha = request.POST.get('confirmarSenha')

        usuario = Usuario.objects.filter(email=email)

        if usuario.exists():
            return render(request, 'cadastro/cadastro.html', {
                'nome': nome,
                'cidade': cidade, 'estado': estado,
                'senha': senha, 'confirmarSenha': confirmarSenha
            })

        if not re.fullmatch(re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'), email):
            return render(request, 'cadastro/cadastro.html', {
                'nome': nome,
                'cidade': cidade, 'estado': estado,
                'senha': senha, 'confirmarSenha': confirmarSenha
            })

        usuario = Usuario(
            nome=nome,
            email=email,
            cidade=cidade,
            estado=estado,
            senha=senha,
            confirmarSenha=confirmarSenha
        )

        usuario.save()

        return HttpResponse('teste')

        # def registro_criado(request):
        #     if request.method == "POST":
        #         # nomeCompleto = request.POST.get('nomeCompleto')
        #         # user = request.POST.get('user')
        #         # email = request.POST.get('email')
        #         # cidade = request.POST.get('cidade')
        #         # estado = request.POST.get('estado')
        #         # senha = request.POST.get('senha')
        #         # confirmarSenha = request.POST.get('confirmarSenha')

        #         # usuario = Usuario(nomeCompleto=nomeCompleto, user=user,
        #         #                   email=email, cidade=cidade,
        #         #                   estado=estado, senha=senha,
        #         #                   confirmarSenha=confirmarSenha)

        #         # usuario.save()
        #         # POST = request.POST
        #         # request.session['registro_form_data'] = POST
        #         # form = formRegistro(POST)

        #         # if form.is_valid():
        #         #     form.save()
        #         #     messages.success('Seu usuario foi criado')

        #         #     del (request.session['registro_form_data'])
        #         return HttpResponse('Dados coletados')

        #     elif request.method == "GET":
        #         return render(request, 'cadastro/cadastro.html')
        #         # context = {'form': form}
        #         # return redirect(request, 'main:registro')
        #         # return HttpResponse('Estou aqui')
