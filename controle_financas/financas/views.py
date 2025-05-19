from django.shortcuts import render, redirect
from .forms import TransacaoForm
from  django.http import HttpResponse

def pagina_inicial(request):
    return HttpResponse('Página Inicial do seu Controle Financeiro!')

def listar_transacoes(request):
    return HttpResponse("Lista de Transações")

def adicionar_transacao(request):
    if request.method == 'POST':
        form = TransacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_transacoes')
    else:
        form = TransacaoForm()
    return render(request, 'financas/adicionar_transacao.html',{'form': form})