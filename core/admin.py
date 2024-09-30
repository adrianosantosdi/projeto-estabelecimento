from django.contrib import admin
from .models import Pessoa, Marca, Veiculo


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'endereco')


@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nome',)


@admin.register(Veiculo)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('marca', 'placa', 'cor', 'observacoes')    