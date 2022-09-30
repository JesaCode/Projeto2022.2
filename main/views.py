from django.shortcuts import render

# Create your views here.


def registro_cadastro(request):
    return render(request, 'cadastro/pages/registro_cadastro.html')
