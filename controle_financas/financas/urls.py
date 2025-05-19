from django.urls import path
from . import views


urlpatterns =[
    path("", views.pagina_inicial, name = "pagina inicial"),
    path('transacoes/', views.listar_transacoes, name="listar_transacoes"),
    path('nova_transacao/', views.adicionar_transacao, name='adicionar_transacao')
]