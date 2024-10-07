from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('pessoas/', views.lista_pessoas, name='core_lista_pessoas'),
    path('pessoas-novo/', views.pessoa_novo, name='core_pessoas_novo'),
    path('pessoas-update/<int:id>', views.pessoa_update, name='core_pessoas_update'),
    path('pessoas-delete/<int:id>', views.pessoa_delete, name='core_pessoas_delete'),

    path('veiculos/', views.lista_veiculos, name='core_lista_veiculos'),
    path('veiculos-novo/', views.veiculo_novo, name='core_veiculo_novo'),
    path('veiculos-update/<int:id>', views.veiculo_update, name='core_veiculo_update'),
    path('veiculos-delete/<int:id>', views.veiculo_delete, name='core_veiculo_delete'),

    path('mov-rot/', views.lista_movrotativo, name='core_lista_movrotativos'),
    path('mov-rot-novo/', views.lista_movrotativo_novo, name='core_movrotativo_novo'),
    path('mov-rot-update/<int:id>', views.lista_movrotativo_update, name='core_movrotativo_update'),
    path('mov-rot-delete/<int:id>', views.lista_movrotativo_delete, name='core_movrotativo_delete'),

    path('mensalistas/', views.lista_mensalista, name='core_lista_mensalistas'),
    path('mensalistas-novo/', views.lista_mensalista_novo, name='core_lista_mensalista_novo'),
    path('mensalistas-update/<int:id>', views.lista_mensalista_update, name='core_lista_mensalista_update'),
    path('mensalistas-delete/<int:id>', views.lista_mensalista_delete, name='core_lista_mensalista_delete'),

    path('mov-mensal/', views.lista_movmensalista, name='core_lista_movmensalistas'),
    path('mov-mensal-novo/', views.lista_movrotativo_novo, name='core_lista_mov_mensal_novo'),
    path('mov-mensal-update/<int:id>', views.lista_mov_mensal_update, name='core_lista_mov_mensal_update'),
    path('mov-mensal-delete/<int:id>', views.lista_mov_mensal_delete, name='core_lista_mov_mensal_delete'),
]