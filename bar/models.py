from django.db import models
from django.core.validators import MinValueValidator


class CategoriaAlimento(models.Model):
  
    nome = models.CharField(max_length=100, unique=True)
    ordem = models.IntegerField(default=0, help_text="Ordem de exibição")
    
    class Meta:
        verbose_name = "Categoria de Alimento"
        verbose_name_plural = "Categorias de Alimentos"
        ordering = ['ordem', 'nome']
    
    def __str__(self):
        return self.nome


class ItemAlimento(models.Model):
  
    categoria = models.ForeignKey(CategoriaAlimento, on_delete=models.CASCADE, related_name='itens')
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    ingredientes = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    imagem = models.ImageField(upload_to='images/', blank=True, null=True)
    imagem_url = models.CharField(max_length=500, blank=True, help_text="URL da imagem se não for upload")
    ativo = models.BooleanField(default=True, help_text="Se o item está disponível no cardápio")
    
    class Meta:
        verbose_name = "Item do Cardápio"
        verbose_name_plural = "Itens do Cardápio"
        ordering = ['categoria__ordem', 'categoria__nome', 'nome']
    
    def __str__(self):
        return f"{self.categoria.nome} - {self.nome}"
    
    def get_imagem_url(self):
      
        if self.imagem:
            return self.imagem.url
        elif self.imagem_url:
            return self.imagem_url
        return None
    
    def get_preco_formatado(self):
  
        return f"R$ {self.preco:.2f}".replace('.', ',')


class CategoriaJogo(models.Model):
  
    nome = models.CharField(max_length=100, unique=True)
    ordem = models.IntegerField(default=0, help_text="Ordem de exibição")
    
    class Meta:
        verbose_name = "Categoria de Jogo"
        verbose_name_plural = "Categorias de Jogos"
        ordering = ['ordem', 'nome']
    
    def __str__(self):
        return self.nome


class Jogo(models.Model):
  
    categoria = models.ForeignKey(CategoriaJogo, on_delete=models.CASCADE, related_name='jogos')
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    detalhes = models.TextField(blank=True, help_text="Detalhes adicionais sobre o jogo")
    tipo = models.CharField(max_length=100, help_text="Tipo de jogo (ex: Estratégia, RPG, etc.)")
    jogadores_min = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    jogadores_max = models.IntegerField(default=4, validators=[MinValueValidator(1)])
    tempo_medio = models.CharField(max_length=50, help_text="Tempo médio de partida (ex: 30-60 min)")
    imagem = models.ImageField(upload_to='images/', blank=True, null=True)
    imagem_url = models.CharField(max_length=500, blank=True, help_text="URL da imagem se não for upload")
    ativo = models.BooleanField(default=True, help_text="Se o jogo está disponível")
    
    class Meta:
        verbose_name = "Jogo"
        verbose_name_plural = "Jogos"
        ordering = ['categoria__ordem', 'categoria__nome', 'nome']
    
    def __str__(self):
        return f"{self.categoria.nome} - {self.nome}"
    
    def get_jogadores_display(self):
    
        if self.jogadores_min == self.jogadores_max:
            return str(self.jogadores_min)
        return f"{self.jogadores_min}-{self.jogadores_max}"
    
    def get_imagem_url(self):
       
        if self.imagem:
            return self.imagem.url
        elif self.imagem_url:
            return self.imagem_url
        return None
    
    def get_copias_disponiveis(self):
        """Retorna o número de cópias disponíveis"""
        return self.copias.filter(disponivel=True).count()
    
    def get_total_copias(self):
        """Retorna o total de cópias do jogo"""
        return self.copias.count()


class CopiaJogo(models.Model):
  
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE, related_name='copias')
    codigo = models.CharField(max_length=50, unique=True, help_text="Código único da cópia")
    disponivel = models.BooleanField(default=True, help_text="Se a cópia está disponível para uso")
    observacoes = models.TextField(blank=True, help_text="Observações sobre o estado da cópia")
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Cópia de Jogo"
        verbose_name_plural = "Cópias de Jogos"
        ordering = ['jogo__nome', 'codigo']
    
    def __str__(self):
        status = "Disponível" if self.disponivel else "Em uso"
        return f"{self.jogo.nome} - {self.codigo} ({status})"
