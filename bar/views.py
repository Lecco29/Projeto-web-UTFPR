from django.shortcuts import render
from .models import CategoriaAlimento, CategoriaJogo, Jogo


def index(request):

    return render(request, 'bar/index.html')


def cardapio(request):
 
    categorias = CategoriaAlimento.objects.filter(
        itens__ativo=True
    ).distinct().prefetch_related('itens').order_by('ordem', 'nome')
    
    
    for categoria in categorias:
        categoria.itens_list = categoria.itens.filter(ativo=True)
    
    context = {
        'categorias': categorias,
    }
    return render(request, 'bar/cardapio.html', context)


def jogos(request):
  
    categorias = CategoriaJogo.objects.filter(
        jogos__ativo=True
    ).distinct().prefetch_related('jogos').order_by('ordem', 'nome')
    
  
    for categoria in categorias:
        jogos_list = []
        for jogo in categoria.jogos.filter(ativo=True):
            jogo.copias_disponiveis = jogo.get_copias_disponiveis()
            jogo.total_copias = jogo.get_total_copias()
            jogos_list.append(jogo)
        categoria.jogos_list = jogos_list
    
    context = {
        'categorias': categorias,
    }
    return render(request, 'bar/jogos.html', context)
