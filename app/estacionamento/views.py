from django.shortcuts import render, redirect
from .models import Pessoa, Veiculo, MovRotativo
from .form import PessoaForm


def home(request):
    context = {'mensagem': 'aqui uma msg'}
    return render(request, 'estacionamento/index.html', context)


def lista_pessoa(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    data = {'pessoas': pessoas, 'form': form}
    return render(request, 'estacionamento/lista_pessoas.html', data)


def pessoa_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('lista_pessoa')


def lista_veiculo(request):
    veiculo = Veiculo.objects.all()
    return render(request, 'estacionamento/lista_veiculo.html', {'veiculo': veiculo})


def lista_movimento(request):
    lista_movimento = MovRotativo.objects.all()
    return render(request, 'estacionamento/lista_movimento.html', {'lista_movimento': lista_movimento})