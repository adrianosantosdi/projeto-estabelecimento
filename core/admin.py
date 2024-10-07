from django.contrib import admin
from .models import Pessoa, Marca, Veiculo, Parametro, MovRotativo, Mensalista, MovMensalista


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'endereco')


@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nome',)


@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'placa', 'cor', 'observacoes')    


@admin.register(Parametro)
class ParametroAdmin(admin.ModelAdmin):
    list_display = ('valor_hora', 'valor_mes') 


@admin.register(MovRotativo)
class MovRotativoAdmin(admin.ModelAdmin):
    list_display = ('checkin', 'checkout', 'valor_hora', 'veiculo', 'pago', 'total', 'horas_totais', 'veiculo')     


@admin.register(Mensalista)
class MensalistaAdmin(admin.ModelAdmin):
    list_display = ('veiculo', 'inicio', 'valor_mes')  


@admin.register(MovMensalista)
class MovMensalistaAdmin(admin.ModelAdmin):
    list_display = ('mensalista', 'dt_pgto', 'total')             