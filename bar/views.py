from django.shortcuts import render
from .models import CategoriaAlimento, CategoriaJogo, Jogo


def index(request):
    """Página inicial do site"""
    return render(request, 'bar/index.html')


def cardapio(request):
    """Página do cardápio de comidas e bebidas"""
    categorias = CategoriaAlimento.objects.filter(
        itens__ativo=True
    ).distinct().prefetch_related('itens').order_by('ordem', 'nome')
    
    # Garantir que apenas itens ativos sejam exibidos
    for categoria in categorias:
        categoria.itens_list = categoria.itens.filter(ativo=True)
    
    context = {
        'categorias': categorias,
    }
    return render(request, 'bar/cardapio.html', context)


def jogos(request):
    """Página da biblioteca de jogos"""
    categorias = CategoriaJogo.objects.filter(
        jogos__ativo=True
    ).distinct().prefetch_related('jogos').order_by('ordem', 'nome')
    
    # Garantir que apenas jogos ativos sejam exibidos e adicionar info de disponibilidade
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
