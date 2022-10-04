from django.http import Http404
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import formRegistro


def index(request):
    return render(request, 'index.html')


def registro_cadastro(request):
    registro_form_data = request.session.get('registro_form_data', None)
    form = formRegistro(registro_form_data)
    return render(request, 'cadastro/pages/registro_cadastro.html', {
        'form': form,
    })


def registro_criado(request):
    if not request.POST:
        raise Http404

    POST = request.POST
    request.session['registro_form_data'] = POST
    form = formRegistro(POST)

    if form.is_valid():
        form.save()
        messages.success('Seu usuario foi criado')

        del(request.session['registro_form_data'])

    return redirect('main:registro')
