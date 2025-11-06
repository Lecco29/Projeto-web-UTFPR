# Josiel Bar - Sistema de Gerenciamento de Bar de Jogos

Sistema web desenvolvido em Django para gerenciamento de um bar de jogos, incluindo cardápio de comidas/bebidas e biblioteca de jogos com controle de disponibilidade.

## Requisitos

- Python 3.8 ou superior
- Django 5.2.8 ou superior
- Pillow (para upload de imagens)

## Instalação

1. Clone ou baixe o repositório

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute as migrações do banco de dados:
```bash
python manage.py makemigrations
python manage.py migrate
```

4. Crie um superusuário para acessar o Django Admin:
```bash
python manage.py createsuperuser
```
Siga as instruções para criar o usuário administrador.

5. (Opcional) Migre os dados dos arquivos JSON para o banco:
```bash
python manage.py migrate_json
```

## Executando a Aplicação

Para iniciar o servidor de desenvolvimento:

```bash
python manage.py runserver
```

Acesse:
- Site principal: http://127.0.0.1:8000/
- Django Admin: http://127.0.0.1:8000/admin/

## Credenciais do Django Admin

**Usuário:** admin  
**Senha:** admin123

*Nota: Altere a senha após o primeiro acesso por questões de segurança.*

## Dados Pré-Cadastrados

O banco de dados já vem com dados populados:

### Alimentos:
- **Entradas**: Batata Frita, Calabresa Acebolada, Torresmo
- **Pratos Principais**: X-Salada, Hambúrguer Artesanal, Bauru, Frango a Passarinho, Porção de Carne
- **Bebidas**: Cerveja, Caipirinha, Refrigerante, Suco
- **Sobremesas**: Pudim, Sorvete

### Jogos (com cópias):
- **Clássicos**: Xadrez (3 cópias), Damas (2), Monopoly (2)
- **Modernos**: Catan (2), Ticket to Ride (1), Wingspan (1)
- **Partida Rápida**: Sushi Go! (3), Love Letter (2), Splendor (2)
- **Cooperativos**: Pandemic (1), Forbidden Island (1)
- **RPG**: Dungeons & Dragons (1), Call of Cthulhu (1)

## Estrutura do Projeto

- `bar/` - Aplicação principal
  - `models.py` - Modelos de dados (CategoriaAlimento, ItemAlimento, CategoriaJogo, Jogo, CopiaJogo)
  - `admin.py` - Configurações do Django Admin
  - `views.py` - Views do site
  - `urls.py` - URLs da aplicação
- `josielbar/` - Configurações do projeto Django
- `templates/` - Templates HTML
- `static/` - Arquivos estáticos (CSS, imagens)
- `media/` - Arquivos de upload (imagens de itens e jogos)
- `json/` - Arquivos JSON originais com dados

## Funcionalidades

### Para Clientes (Site Público)
- Visualização do cardápio de comidas e bebidas
- Visualização da biblioteca de jogos
- Consulta de disponibilidade de cópias de jogos

### Para Funcionários (Django Admin)
- Gerenciamento de categorias e itens do cardápio
- Gerenciamento de categorias e jogos
- **Registro e controle de cópias de jogos** (disponíveis/em uso)
- Visualização de disponibilidade em tempo real
- Upload de imagens ou uso de URLs externas

## Modelos de Dados

### CategoriaAlimento
- Categorias do cardápio (Entradas, Pratos Principais, Bebidas, Sobremesas)

### ItemAlimento
- Itens do cardápio com preço, descrição, ingredientes e imagem

### CategoriaJogo
- Categorias de jogos (Clássicos, Modernos, RPG, etc.)

### Jogo
- Informações dos jogos (nome, tipo, número de jogadores, tempo médio)

### CopiaJogo
- Cópias físicas dos jogos para controle de disponibilidade
- Permite registrar quantas cópias estão disponíveis ou em uso

## Personalizações do Django Admin

- Listas personalizadas com informações úteis (total de itens, disponibilidade)
- Formulários inline para gerenciar cópias de jogos diretamente na página do jogo
- Visualização de imagens em miniatura
- Filtros e busca por vários campos
- Edição rápida de campos comuns (ativo, disponível)

## Comandos Úteis

```bash
# Criar migrações
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Popular banco com dados genéricos
python manage.py popular_dados

# Migrar dados do JSON
python manage.py migrate_json

# Criar superusuário (se necessário)
python manage.py createsuperuser

# Coletar arquivos estáticos (produção)
python manage.py collectstatic
```

