from django.shortcuts import render, redirect
from .models import Pessoa, Veiculo, MovRotativo
from .form import PessoaForm, VeiculoForm


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


def pessoa_update(request, id):
    data = {}
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    data['pessoa'] = pessoa
    data['form'] = form
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('lista_pessoa')
    else:
        return render(request, 'estacionamento/update_pessoa.html', data)


def pessoa_delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('lista_pessoa')
    else:
        return render(request, 'estacionamento/delete_confirm.html', {'pessoa': pessoa})


def lista_veiculo(request):
    veiculo = Veiculo.objects.all()
    return render(request, 'estacionamento/lista_veiculo.html', {'veiculo': veiculo})


def veiculo_update(request, id):
    data = {}
    veiculo = Veiculo.objects.get(id=id)
    form = VeiculoForm(request.POST or None, instance=veiculo)
    data['veiculo'] = veiculo
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('lista_veiculo')
    else:
        return render(request, 'estacionamento/update-veiculo.html', data)

def lista_movimento(request):
    lista_movimento = MovRotativo.objects.all()
    return render(request, 'estacionamento/lista_movimento.html', {'lista_movimento': lista_movimento})