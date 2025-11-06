"""
Comando para popular o banco de dados com dados genéricos baseados nas imagens disponíveis
"""
from django.core.management.base import BaseCommand
from bar.models import CategoriaAlimento, ItemAlimento, CategoriaJogo, Jogo, CopiaJogo
import os
from django.conf import settings


class Command(BaseCommand):
    help = 'Popula o banco de dados com dados genéricos baseados nas imagens disponíveis'

    def handle(self, *args, **options):
        self.stdout.write('Populando banco de dados com dados genéricos...')
        
        # Popular alimentos
        self.popular_alimentos()
        
        # Popular jogos
        self.popular_jogos()
        
        self.stdout.write(self.style.SUCCESS('Banco de dados populado com sucesso!'))

    def popular_alimentos(self):
        """Popula alimentos baseado nas imagens disponíveis"""
        self.stdout.write('\n=== Populando Alimentos ===')
        
        # Categorias
        categorias_data = {
            'Entradas': {
                'ordem': 1,
                'itens': [
                    {
                        'nome': 'Batata Frita',
                        'descricao': 'Porção de batata frita crocante e dourada, perfeita para compartilhar',
                        'ingredientes': 'Batata, óleo, sal, temperos especiais',
                        'preco': 15.90,
                        'imagem': 'images/batatafrita.jpg'
                    },
                    {
                        'nome': 'Calabresa Acebolada',
                        'descricao': 'Linguiça calabresa fatiada com cebola refogada, um clássico do bar',
                        'ingredientes': 'Linguiça calabresa, cebola, azeite, pimenta',
                        'preco': 19.90,
                        'imagem': 'images/Calabresa Acebolada.jpg'
                    },
                    {
                        'nome': 'Torresmo',
                        'descricao': 'Torresmo crocante e dourado, irresistível para acompanhar uma cerveja',
                        'ingredientes': 'Pele de porco, sal, temperos naturais',
                        'preco': 17.90,
                        'imagem': 'images/torresmo.jpg'
                    }
                ]
            },
            'Pratos Principais': {
                'ordem': 2,
                'itens': [
                    {
                        'nome': 'X-Salada',
                        'descricao': 'Hambúrguer suculento com queijo, alface, tomate e maionese',
                        'ingredientes': 'Pão de hambúrguer, carne bovina 150g, queijo, alface, tomate, maionese',
                        'preco': 22.90,
                        'imagem': 'images/X-salada.jpg'
                    },
                    {
                        'nome': 'Hambúrguer Artesanal',
                        'descricao': 'Hambúrguer artesanal com ingredientes selecionados',
                        'ingredientes': 'Pão brioche, carne artesanal 180g, queijo cheddar, bacon, alface, tomate',
                        'preco': 28.90,
                        'imagem': 'images/hamburguer.jpg'
                    },
                    {
                        'nome': 'Bauru',
                        'descricao': 'Sanduíche clássico brasileiro com presunto, queijo, tomate e maionese',
                        'ingredientes': 'Pão francês, presunto, queijo muçarela, tomate, maionese',
                        'preco': 19.90,
                        'imagem': 'images/Bauru.jpg'
                    },
                    {
                        'nome': 'Frango a Passarinho',
                        'descricao': 'Frango frito em pedaços com alho e temperos especiais',
                        'ingredientes': 'Frango, alho, óleo, temperos, pimenta',
                        'preco': 26.90,
                        'imagem': 'images/frango-passarinho.jpg'
                    },
                    {
                        'nome': 'Porção de Carne com Fritas',
                        'descricao': 'Tiras de carne acebolada acompanhadas de batata frita',
                        'ingredientes': 'Carne bovina, cebola, batata, óleo, temperos',
                        'preco': 32.90,
                        'imagem': 'images/carne-frita.jpg'
                    }
                ]
            },
            'Bebidas': {
                'ordem': 3,
                'itens': [
                    {
                        'nome': 'Cerveja Long Neck',
                        'descricao': 'Cerveja gelada, variedade de marcas disponíveis',
                        'ingredientes': 'Água, malte, lúpulo, levedura',
                        'preco': 9.90,
                        'imagem': 'images/cerveja.jpg'
                    },
                    {
                        'nome': 'Caipirinha',
                        'descricao': 'Caipirinha de limão com cachaça artesanal',
                        'ingredientes': 'Cachaça, limão, açúcar, gelo',
                        'preco': 14.90,
                        'imagem': 'images/caipirinha.jpg'
                    },
                    {
                        'nome': 'Refrigerante Lata',
                        'descricao': 'Refrigerante gelado em lata, diversos sabores',
                        'ingredientes': 'Água gaseificada, açúcar, essências naturais',
                        'preco': 7.00,
                        'imagem': 'images/refrigerante.jpg'
                    },
                    {
                        'nome': 'Suco Natural',
                        'descricao': 'Suco fresco da fruta da estação, 100% natural',
                        'ingredientes': 'Frutas frescas, água, açúcar (opcional)',
                        'preco': 8.90,
                        'imagem': 'images/suco.jpg'
                    }
                ]
            },
            'Sobremesas': {
                'ordem': 4,
                'itens': [
                    {
                        'nome': 'Pudim de Leite',
                        'descricao': 'Clássico pudim caseiro com calda de caramelo',
                        'ingredientes': 'Leite condensado, leite, ovos, açúcar',
                        'preco': 9.90,
                        'imagem': 'images/pudim.jpg'
                    },
                    {
                        'nome': 'Sorvete de Creme',
                        'descricao': 'Bola de sorvete de creme com calda opcional',
                        'ingredientes': 'Leite, creme de leite, açúcar, baunilha',
                        'preco': 8.50,
                        'imagem': 'images/sorvete.jpg'
                    }
                ]
            }
        }
        
        for cat_nome, cat_data in categorias_data.items():
            categoria, created = CategoriaAlimento.objects.get_or_create(
                nome=cat_nome,
                defaults={'ordem': cat_data['ordem']}
            )
            if not created:
                categoria.ordem = cat_data['ordem']
                categoria.save()
            
            self.stdout.write(f'  Categoria: {categoria.nome}')
            
            for item_data in cat_data['itens']:
                item, created = ItemAlimento.objects.get_or_create(
                    categoria=categoria,
                    nome=item_data['nome'],
                    defaults={
                        'descricao': item_data['descricao'],
                        'ingredientes': item_data['ingredientes'],
                        'preco': item_data['preco'],
                        'imagem_url': item_data['imagem'],
                        'ativo': True,
                    }
                )
                if not created:
                    item.descricao = item_data['descricao']
                    item.ingredientes = item_data['ingredientes']
                    item.preco = item_data['preco']
                    item.imagem_url = item_data['imagem']
                    item.ativo = True
                    item.save()
                
                self.stdout.write(f'    - {item.nome}')

    def popular_jogos(self):
        """Popula jogos baseado nas imagens disponíveis"""
        self.stdout.write('\n=== Populando Jogos ===')
        
        categorias_data = {
            'Jogos Clássicos': {
                'ordem': 1,
                'jogos': [
                    {
                        'nome': 'Xadrez',
                        'descricao': 'O clássico jogo de estratégia que desafia a mente',
                        'detalhes': 'Jogo milenar de estratégia pura. Cada peça tem movimentos únicos e o objetivo é dar xeque-mate no rei adversário.',
                        'tipo': 'Estratégia Abstrata',
                        'jogadores_min': 2,
                        'jogadores_max': 2,
                        'tempo': '30-60 min',
                        'imagem': 'images/tab.jpg',
                        'copias': 3
                    },
                    {
                        'nome': 'Damas',
                        'descricao': 'Jogo tradicional de captura e movimento',
                        'detalhes': 'Jogo clássico onde o objetivo é capturar todas as peças do adversário ou bloqueá-las.',
                        'tipo': 'Estratégia Abstrata',
                        'jogadores_min': 2,
                        'jogadores_max': 2,
                        'tempo': '15-30 min',
                        'imagem': 'images/tab.jpg',
                        'copias': 2
                    },
                    {
                        'nome': 'Monopoly',
                        'descricao': 'O clássico jogo de compra e venda de propriedades',
                        'detalhes': 'Jogue dados, compre propriedades, construa casas e hotéis. O objetivo é fazer os outros jogadores falirem.',
                        'tipo': 'Estratégia/Economia',
                        'jogadores_min': 2,
                        'jogadores_max': 8,
                        'tempo': '60-180 min',
                        'imagem': 'images/tab.jpg',
                        'copias': 2
                    }
                ]
            },
            'Jogos Modernos': {
                'ordem': 2,
                'jogos': [
                    {
                        'nome': 'Catan',
                        'descricao': 'Construa sua civilização na ilha de Catan',
                        'detalhes': 'Colete recursos, construa estradas e cidades. Negocie com outros jogadores para conseguir os recursos que precisa.',
                        'tipo': 'Estratégia/Construção',
                        'jogadores_min': 3,
                        'jogadores_max': 4,
                        'tempo': '60-90 min',
                        'imagem': 'images/tab.jpg',
                        'copias': 2
                    },
                    {
                        'nome': 'Ticket to Ride',
                        'descricao': 'Construa rotas ferroviárias pelos Estados Unidos',
                        'detalhes': 'Colete cartas de trem e construa rotas conectando cidades. Complete seus bilhetes de destino para ganhar pontos.',
                        'tipo': 'Estratégia/Construção',
                        'jogadores_min': 2,
                        'jogadores_max': 5,
                        'tempo': '30-60 min',
                        'imagem': 'images/tab.jpg',
                        'copias': 1
                    },
                    {
                        'nome': 'Wingspan',
                        'descricao': 'Crie o habitat perfeito para pássaros',
                        'detalhes': 'Jogo de engine building onde você atrai pássaros para seu habitat, cada um com habilidades únicas.',
                        'tipo': 'Estratégia/Temático',
                        'jogadores_min': 1,
                        'jogadores_max': 5,
                        'tempo': '40-70 min',
                        'imagem': 'images/tab.jpg',
                        'copias': 1
                    }
                ]
            },
            'Jogos de Partida Rápida': {
                'ordem': 3,
                'jogos': [
                    {
                        'nome': 'Sushi Go!',
                        'descricao': 'Colete a melhor combinação de sushi',
                        'detalhes': 'Jogo rápido de cartas onde você escolhe cartas para fazer a melhor combinação de sushi.',
                        'tipo': 'Drafting',
                        'jogadores_min': 2,
                        'jogadores_max': 5,
                        'tempo': '15 min',
                        'imagem': 'images/tab.jpg',
                        'copias': 3
                    },
                    {
                        'nome': 'Love Letter',
                        'descricao': 'Ganhe o coração da princesa',
                        'detalhes': 'Jogo de cartas simples onde você tenta entregar sua carta de amor à princesa antes dos outros.',
                        'tipo': 'Dedução',
                        'jogadores_min': 2,
                        'jogadores_max': 4,
                        'tempo': '20 min',
                        'imagem': 'images/tab.jpg',
                        'copias': 2
                    },
                    {
                        'nome': 'Splendor',
                        'descricao': 'Construa seu império de joias',
                        'detalhes': 'Colete gemas para comprar desenvolvimentos e atrair nobres. O primeiro a 15 pontos vence.',
                        'tipo': 'Estratégia/Economia',
                        'jogadores_min': 2,
                        'jogadores_max': 4,
                        'tempo': '30 min',
                        'imagem': 'images/tab.jpg',
                        'copias': 2
                    }
                ]
            },
            'Jogos Cooperativos': {
                'ordem': 4,
                'jogos': [
                    {
                        'nome': 'Pandemic',
                        'descricao': 'Salve o mundo de doenças mortais',
                        'detalhes': 'Trabalhe em equipe para curar doenças e salvar a humanidade. Todos ganham ou todos perdem.',
                        'tipo': 'Cooperativo',
                        'jogadores_min': 2,
                        'jogadores_max': 4,
                        'tempo': '45 min',
                        'imagem': 'images/tab.jpg',
                        'copias': 1
                    },
                    {
                        'nome': 'Forbidden Island',
                        'descricao': 'Escape da ilha antes que ela afunde',
                        'detalhes': 'Jogue como aventureiros tentando coletar tesouros e escapar de uma ilha que está afundando.',
                        'tipo': 'Cooperativo/Aventura',
                        'jogadores_min': 2,
                        'jogadores_max': 4,
                        'tempo': '30 min',
                        'imagem': 'images/tab.jpg',
                        'copias': 1
                    }
                ]
            },
            'Jogos de RPG': {
                'ordem': 5,
                'jogos': [
                    {
                        'nome': 'Dungeons & Dragons',
                        'descricao': 'A aventura épica de fantasia',
                        'detalhes': 'Crie personagens únicos e embarque em aventuras épicas em um mundo de fantasia. O Mestre narra a história.',
                        'tipo': 'RPG',
                        'jogadores_min': 3,
                        'jogadores_max': 6,
                        'tempo': '120+ min',
                        'imagem': 'images/tab.jpg',
                        'copias': 1
                    },
                    {
                        'nome': 'Call of Cthulhu',
                        'descricao': 'Investigue mistérios sobrenaturais',
                        'detalhes': 'Jogue como investigadores tentando desvendar mistérios sobrenaturais e sobreviver à loucura.',
                        'tipo': 'RPG/Horror',
                        'jogadores_min': 2,
                        'jogadores_max': 6,
                        'tempo': '120+ min',
                        'imagem': 'images/tab.jpg',
                        'copias': 1
                    }
                ]
            }
        }
        
        for cat_nome, cat_data in categorias_data.items():
            categoria, created = CategoriaJogo.objects.get_or_create(
                nome=cat_nome,
                defaults={'ordem': cat_data['ordem']}
            )
            if not created:
                categoria.ordem = cat_data['ordem']
                categoria.save()
            
            self.stdout.write(f'  Categoria: {categoria.nome}')
            
            for jogo_data in cat_data['jogos']:
                jogo, created = Jogo.objects.get_or_create(
                    categoria=categoria,
                    nome=jogo_data['nome'],
                    defaults={
                        'descricao': jogo_data['descricao'],
                        'detalhes': jogo_data['detalhes'],
                        'tipo': jogo_data['tipo'],
                        'jogadores_min': jogo_data['jogadores_min'],
                        'jogadores_max': jogo_data['jogadores_max'],
                        'tempo_medio': jogo_data['tempo'],
                        'imagem_url': jogo_data['imagem'],
                        'ativo': True,
                    }
                )
                if not created:
                    jogo.descricao = jogo_data['descricao']
                    jogo.detalhes = jogo_data['detalhes']
                    jogo.tipo = jogo_data['tipo']
                    jogo.jogadores_min = jogo_data['jogadores_min']
                    jogo.jogadores_max = jogo_data['jogadores_max']
                    jogo.tempo_medio = jogo_data['tempo']
                    jogo.imagem_url = jogo_data['imagem']
                    jogo.ativo = True
                    jogo.save()
                
                # Criar cópias do jogo
                num_copias = jogo_data.get('copias', 1)
                for i in range(1, num_copias + 1):
                    codigo = f"{jogo.nome.upper()[:3]}{i:03d}"
                    CopiaJogo.objects.get_or_create(
                        jogo=jogo,
                        codigo=codigo,
                        defaults={
                            'disponivel': True,
                            'observacoes': ''
                        }
                    )
                
                self.stdout.write(f'    - {jogo.nome} ({num_copias} copias)')

