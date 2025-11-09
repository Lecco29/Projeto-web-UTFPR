# Josiel Bar - Sistema de Gerenciamento de Bar de Jogos

Sistema web desenvolvido em Django para gerenciamento de um bar de jogos, incluindo cardápio de comidas/bebidas e biblioteca de jogos com controle de disponibilidade.


## Instalação

1. Clone ou baixe o repositório

2. Instale as dependências:
```bash
pip install -r requirements.txt
```
## Executando a Aplicação

3.Para iniciar o servidor de desenvolvimento:

```bash
python manage.py runserver
```

Acesse:
- Site principal: http://127.0.0.1:8000/
- Django Admin: http://127.0.0.1:8000/admin/

## Credenciais do Django Admin

**Usuário:** admin  
**Senha:** admin123

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

