"""
Comando Django para migrar dados dos arquivos JSON para o banco de dados
"""
import json
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from bar.models import CategoriaAlimento, ItemAlimento, CategoriaJogo, Jogo


class Command(BaseCommand):
    help = 'Migra dados dos arquivos JSON para o banco de dados'

    def handle(self, *args, **options):
        base_dir = settings.BASE_DIR
        json_dir = os.path.join(base_dir, 'json')
        
        # Migrar alimentos e bebidas
        alimentos_file = os.path.join(json_dir, 'alimentos_bebidas.json')
        if os.path.exists(alimentos_file):
            self.stdout.write('Migrando alimentos e bebidas...')
            self.migrate_alimentos(alimentos_file)
        else:
            self.stdout.write(self.style.WARNING(f'Arquivo não encontrado: {alimentos_file}'))
        
        # Migrar jogos
        jogos_file = os.path.join(json_dir, 'jogos.json')
        if os.path.exists(jogos_file):
            self.stdout.write('Migrando jogos...')
            self.migrate_jogos(jogos_file)
        else:
            self.stdout.write(self.style.WARNING(f'Arquivo não encontrado: {jogos_file}'))
        
        self.stdout.write(self.style.SUCCESS('Migração concluída!'))

    def migrate_alimentos(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        ordem = 0
        for cat_data in data.get('categorias', []):
            ordem += 1
            categoria, created = CategoriaAlimento.objects.get_or_create(
                nome=cat_data['nome'],
                defaults={'ordem': ordem}
            )
            if not created:
                categoria.ordem = ordem
                categoria.save()
            
            self.stdout.write(f'  Categoria: {categoria.nome}')
            
            for item_data in cat_data.get('itens', []):
                # Extrair preço do formato "R$ XX,XX"
                preco_str = item_data.get('preco', '0').replace('R$', '').replace(' ', '').replace(',', '.')
                try:
                    preco = float(preco_str)
                except ValueError:
                    preco = 0.0
                
                # Normalizar caminho da imagem
                imagem_path = item_data.get('imagem', '')
                if imagem_path and not imagem_path.startswith('http'):
                    # Se for caminho relativo, usar como imagem_url
                    imagem_url = imagem_path
                else:
                    imagem_url = ''
                
                item, created = ItemAlimento.objects.get_or_create(
                    categoria=categoria,
                    nome=item_data['nome'],
                    defaults={
                        'descricao': item_data.get('descricao', ''),
                        'ingredientes': item_data.get('ingredientes', ''),
                        'preco': preco,
                        'imagem_url': imagem_url,
                        'ativo': True,
                    }
                )
                if not created:
                    # Atualizar dados existentes
                    item.descricao = item_data.get('descricao', '')
                    item.ingredientes = item_data.get('ingredientes', '')
                    item.preco = preco
                    if imagem_url:
                        item.imagem_url = imagem_url
                    item.save()
                
                self.stdout.write(f'    - {item.nome}')

    def migrate_jogos(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        ordem = 0
        for cat_data in data.get('categorias', []):
            ordem += 1
            categoria, created = CategoriaJogo.objects.get_or_create(
                nome=cat_data['nome'],
                defaults={'ordem': ordem}
            )
            if not created:
                categoria.ordem = ordem
                categoria.save()
            
            self.stdout.write(f'  Categoria: {categoria.nome}')
            
            for jogo_data in cat_data.get('jogos', []):
                # Parse jogadores (ex: "2-4" ou "2")
                jogadores_str = jogo_data.get('jogadores', '1-4')
                if '-' in jogadores_str:
                    try:
                        jogadores_min, jogadores_max = map(int, jogadores_str.split('-'))
                    except ValueError:
                        jogadores_min, jogadores_max = 1, 4
                else:
                    try:
                        jogadores_min = jogadores_max = int(jogadores_str)
                    except ValueError:
                        jogadores_min, jogadores_max = 1, 4
                
                # Normalizar caminho da imagem
                imagem_path = jogo_data.get('imagem', '')
                if imagem_path and not imagem_path.startswith('http'):
                    imagem_url = imagem_path
                else:
                    imagem_url = ''
                
                jogo, created = Jogo.objects.get_or_create(
                    categoria=categoria,
                    nome=jogo_data['nome'],
                    defaults={
                        'descricao': jogo_data.get('descricao', ''),
                        'detalhes': jogo_data.get('detalhes', ''),
                        'tipo': jogo_data.get('tipo', ''),
                        'jogadores_min': jogadores_min,
                        'jogadores_max': jogadores_max,
                        'tempo_medio': jogo_data.get('tempo', ''),
                        'imagem_url': imagem_url,
                        'ativo': True,
                    }
                )
                if not created:
                    # Atualizar dados existentes
                    jogo.descricao = jogo_data.get('descricao', '')
                    jogo.detalhes = jogo_data.get('detalhes', '')
                    jogo.tipo = jogo_data.get('tipo', '')
                    jogo.jogadores_min = jogadores_min
                    jogo.jogadores_max = jogadores_max
                    jogo.tempo_medio = jogo_data.get('tempo', '')
                    if imagem_url:
                        jogo.imagem_url = imagem_url
                    jogo.save()
                
                self.stdout.write(f'    - {jogo.nome}')

