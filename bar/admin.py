from django.contrib import admin
from django.utils.html import format_html
from .models import CategoriaAlimento, ItemAlimento, CategoriaJogo, Jogo, CopiaJogo


@admin.register(CategoriaAlimento)
class CategoriaAlimentoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'ordem', 'total_itens', 'total_itens_ativos']
    list_editable = ['ordem']
    search_fields = ['nome']
    ordering = ['ordem', 'nome']
    
    def total_itens(self, obj):
        return obj.itens.count()
    total_itens.short_description = "Total de Itens"
    
    def total_itens_ativos(self, obj):
        return obj.itens.filter(ativo=True).count()
    total_itens_ativos.short_description = "Itens Ativos"


class ItemAlimentoInline(admin.TabularInline):
    model = ItemAlimento
    extra = 1
    fields = ['nome', 'preco', 'ativo', 'imagem', 'imagem_url']
    show_change_link = True


@admin.register(ItemAlimento)
class ItemAlimentoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'categoria', 'preco_formatado', 'ativo', 'preview_imagem']
    list_filter = ['categoria', 'ativo']
    search_fields = ['nome', 'descricao', 'ingredientes']
    list_editable = ['ativo']
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('categoria', 'nome', 'descricao', 'ingredientes', 'preco', 'ativo')
        }),
        ('Imagem', {
            'fields': ('imagem', 'imagem_url'),
            'description': 'Faça upload de uma imagem ou forneça uma URL'
        }),
    )
    
    def preco_formatado(self, obj):
        return f"R$ {obj.preco:.2f}".replace('.', ',')
    preco_formatado.short_description = "Preço"
    
    def preview_imagem(self, obj):
        img_url = obj.get_imagem_url()
        if img_url:
            return format_html('<img src="{}" style="max-width: 100px; max-height: 100px;" />', img_url)
        return "Sem imagem"
    preview_imagem.short_description = "Imagem"


@admin.register(CategoriaJogo)
class CategoriaJogoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'ordem', 'total_jogos', 'total_jogos_ativos']
    list_editable = ['ordem']
    search_fields = ['nome']
    ordering = ['ordem', 'nome']
    
    def total_jogos(self, obj):
        return obj.jogos.count()
    total_jogos.short_description = "Total de Jogos"
    
    def total_jogos_ativos(self, obj):
        return obj.jogos.filter(ativo=True).count()
    total_jogos_ativos.short_description = "Jogos Ativos"


class CopiaJogoInline(admin.TabularInline):
    model = CopiaJogo
    extra = 1
    fields = ['codigo', 'disponivel', 'observacoes']
    show_change_link = True


@admin.register(Jogo)
class JogoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'categoria', 'tipo', 'jogadores_display', 'tempo_medio', 
                    'copias_disponiveis', 'total_copias', 'ativo', 'preview_imagem']
    list_filter = ['categoria', 'tipo', 'ativo']
    search_fields = ['nome', 'descricao', 'tipo']
    list_editable = ['ativo']
    inlines = [CopiaJogoInline]
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('categoria', 'nome', 'descricao', 'detalhes', 'tipo', 'ativo')
        }),
        ('Especificações', {
            'fields': ('jogadores_min', 'jogadores_max', 'tempo_medio')
        }),
        ('Imagem', {
            'fields': ('imagem', 'imagem_url'),
            'description': 'Faça upload de uma imagem ou forneça uma URL'
        }),
    )
    
    def jogadores_display(self, obj):
        return obj.get_jogadores_display()
    jogadores_display.short_description = "Jogadores"
    
    def copias_disponiveis(self, obj):
        disponiveis = obj.get_copias_disponiveis()
        total = obj.get_total_copias()
        if total == 0:
            return format_html('<span style="color: orange;">Nenhuma cópia cadastrada</span>')
        cor = 'green' if disponiveis > 0 else 'red'
        return format_html('<span style="color: {};">{}/{}</span>', cor, disponiveis, total)
    copias_disponiveis.short_description = "Cópias Disponíveis"
    
    def total_copias(self, obj):
        return obj.get_total_copias()
    total_copias.short_description = "Total de Cópias"
    
    def preview_imagem(self, obj):
        img_url = obj.get_imagem_url()
        if img_url:
            return format_html('<img src="{}" style="max-width: 100px; max-height: 100px;" />', img_url)
        return "Sem imagem"
    preview_imagem.short_description = "Imagem"


@admin.register(CopiaJogo)
class CopiaJogoAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'jogo', 'disponivel', 'status_disponibilidade', 'data_atualizacao']
    list_filter = ['disponivel', 'jogo__categoria', 'data_atualizacao']
    search_fields = ['codigo', 'jogo__nome', 'observacoes']
    list_editable = ['disponivel']
    date_hierarchy = 'data_atualizacao'
    fieldsets = (
        ('Informações da Cópia', {
            'fields': ('jogo', 'codigo', 'disponivel')
        }),
        ('Observações', {
            'fields': ('observacoes',)
        }),
        ('Datas', {
            'fields': ('data_criacao', 'data_atualizacao'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ['data_criacao', 'data_atualizacao']
    
    def status_disponibilidade(self, obj):
        if obj.disponivel:
            return format_html('<span style="color: green; font-weight: bold;">✓ Disponível</span>')
        else:
            return format_html('<span style="color: red; font-weight: bold;">✗ Em uso</span>')
    status_disponibilidade.short_description = "Status"


# Personalização do Admin Site
admin.site.site_header = "Administração - Josiel Bar"
admin.site.site_title = "Josiel Bar Admin"
admin.site.index_title = "Painel de Controle"
