from django.shortcuts import render
from .models import Pessoa

def home(request):
    context = {'mensagem': 'aqui uma msg'}
    return render(request, 'estacionamento/index.html', context)


def lista_pessoa(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'estacionamento/lista_pessoas.html', {'pessoas':pessoas})