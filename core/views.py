from django.shortcuts import render, redirect
from .models import Pessoa, Veiculo, MovRotativo, Mensalista, MovMensalista
from .forms import PessoaForm, VeiculoForm, MovRotativoForm, MensalistaForm, MovMensalistaForm


def home(request):
    return render(request, 'core/index.html')


def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    return render(request, 'core/lista_pessoas.html', context= {
        'pessoas': pessoas,
        'form': PessoaForm
    })


def pessoa_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoas')   


def pessoa_update(request, id):
    data = {}
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    data['pessoa'] = pessoa
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/update_pessoas.html', data)
    

def pessoa_delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('core_lista_pessoas')  
    else:
        return render(request, 'core/delete_confirm.html', context={
            'obj': pessoa
        })  
    

def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    form = VeiculoForm()
    return render(request, 'core/lista_veiculos.html', context={
        'veiculos': veiculos,
        'form': VeiculoForm
    })


def veiculo_novo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_veiculos')  


def veiculo_update(request, id):
    data = {}
    veiculo = Veiculo.objects.get(id=id)
    form = VeiculoForm(request.POST or None, instance=veiculo)
    data['veiculo'] = veiculo
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/update_veiculos.html', data)
    

def veiculo_delete(request, id):
    veiculo = Veiculo.objects.get(id=id)
    if request.method == 'POST':
        veiculo.delete()
        return redirect('core_lista_veiculos')  
    else:
        return render(request, 'core/delete_confirm.html', context={
            'obj': veiculo
        })  


def lista_movrotativo(request):
    mov_root = MovRotativo.objects.all()
    form = MovRotativoForm()
    return render(request, 'core/lista_movrotativos.html', context={
       'mov_root': mov_root,
       'form': MovRotativoForm
    })


def lista_movrotativo_novo(request):
    form = MovRotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movrotativos')  


def lista_movrotativo_update(request, id):
    data = {}
    mov_rotativo = MovRotativo.objects.get(id=id)
    form = MovRotativoForm(request.POST or None, instance=mov_rotativo)
    data['mov_rotativo'] = mov_rotativo
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movrotativos')
    else:
        return render(request, 'core/update_movrotativo.html', data)
    

def lista_movrotativo_delete(request, id):
    mov_rotativo =MovRotativo.objects.get(id=id)
    if request.method == 'POST':
        mov_rotativo.delete()
        return redirect('core_lista_movrotativos')  
    else:
        return render(request, 'core/delete_confirm.html', context={
            'obj': mov_rotativo
        })      


def lista_mensalista(request):
    mensalistas = Mensalista.objects.all()
    form = MensalistaForm()
    return render(request, 'core/lista_mensalistas.html', context={
       'mensalistas': mensalistas,
       'form': MensalistaForm
    })


def lista_mensalista_update(request, id):
    data = {}
    mensalista = Mensalista.objects.get(id=id)
    form = MensalistaForm(request.POST or None, instance=mensalista)
    data['mensalista'] = mensalista
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_mensalistas')
    else:
        return render(request, 'core/update_mensalistas.html', data)
    

def lista_mensalista_novo(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_mensalistas')  


def lista_mensalista_delete(request, id):
    mensalista = Mensalista.objects.get(id=id)
    if request.method == 'POST':
        mensalista.delete()
        return redirect('core_lista_mensalistas')  
    else:
        return render(request, 'core/delete_confirm.html', context={
            'obj': mensalista
        })  


def lista_movmensalista(request):
    mov_mensalista = MovMensalista.objects.all()
    form: MovMensalistaForm
    return render(request, 'core/lista_movmensalistas.html', context={
       'mov_mensalista': mov_mensalista,
       'form': MovMensalistaForm
    })


def lista_mov_mensal_novo(request):
    form = MovMensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movmensalistas')   


def lista_mov_mensal_update(request, id):
    data = {}
    mov_mensalista = MovMensalista.objects.get(id=id)
    form = MovMensalistaForm(request.POST or None, instance=mov_mensalista)
    data['mov_mensalista'] = mov_mensalista
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movmensalistas')
    else:
        return render(request, 'core/update_movmensalistas.html', data)
    

def lista_mov_mensal_delete(request, id):
    mov_mensalista = MovMensalista.objects.get(id=id)
    if request.method == 'POST':
        mov_mensalista.delete()
        return redirect('core_lista_movmensalistas')  
    else:
        return render(request, 'core/delete_confirm.html', context={
            'obj': mov_mensalista
        })  