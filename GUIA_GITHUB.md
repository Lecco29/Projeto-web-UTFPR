# Guia para Subir o Projeto no GitHub

## Passo a Passo Completo

### 1. Criar Repositório no GitHub

1. Acesse [github.com](https://github.com)
2. Clique em "New repository" (ou "Novo repositório")
3. Nome: `josiel-bar-django` (ou outro nome)
4. Descrição: "Sistema de gerenciamento de bar de jogos desenvolvido em Django"
5. **NÃO** marque "Initialize with README" (já temos README)
6. Clique em "Create repository"

### 2. Inicializar Git no Projeto

Abra o terminal na pasta do projeto e execute:

```bash
# Inicializar repositório Git
git init

# Adicionar todos os arquivos
git add .

# Fazer o primeiro commit
git commit -m "Initial commit: Sistema Django para bar de jogos"

# Adicionar o repositório remoto (substitua SEU_USUARIO pelo seu usuário do GitHub)
git remote add origin https://github.com/SEU_USUARIO/josiel-bar-django.git

# Enviar para o GitHub
git branch -M main
git push -u origin main
```

### 3. O que está sendo enviado

✅ **Arquivos incluídos:**
- Todo o código fonte (`bar/`, `josielbar/`)
- Templates HTML (`templates/`)
- Arquivos estáticos (`static/` - CSS e imagens)
- Banco de dados (`db.sqlite3`) - **COM TODOS OS DADOS**
- Uploads (`media/`) - **COM TODAS AS IMAGENS**
- Migrações (`bar/migrations/`)
- Configurações (`manage.py`, `requirements.txt`)
- Documentação (`README.md`, `INSTRUCOES_EXECUCAO.md`, etc.)

### 4. Credenciais do Admin

**IMPORTANTE:** As credenciais do Django Admin estão no banco de dados:
- Usuário: `admin`
- Senha: `admin123`

**⚠️ ATENÇÃO:** Se for usar em produção, altere a senha!

### 5. Clonar o Repositório (para outra pessoa)

Quando alguém clonar o repositório:

```bash
# Clonar o repositório
git clone https://github.com/SEU_USUARIO/josiel-bar-django.git

# Entrar na pasta
cd josiel-bar-django

# Instalar dependências
pip install -r requirements.txt

# Rodar o servidor (o banco já está pronto!)
python manage.py runserver
```

**Pronto!** O banco de dados já vem com todos os dados, então não precisa rodar migrações ou criar superusuário.

## Estrutura do Repositório

```
josiel-bar-django/
├── bar/                    # Aplicação Django
│   ├── migrations/        # Migrações do banco
│   ├── models.py          # Modelos de dados
│   ├── admin.py           # Configuração do Admin
│   ├── views.py           # Views
│   └── ...
├── josielbar/             # Configurações do projeto
├── templates/             # Templates HTML
├── static/                # Arquivos estáticos (CSS, imagens)
├── media/                 # Uploads (imagens enviadas)
├── json/                  # Dados JSON originais
├── db.sqlite3            # Banco de dados (com todos os dados!)
├── manage.py             # Script principal
├── requirements.txt      # Dependências
└── README.md            # Documentação
```

## Dados que Já Estão no Banco

### Alimentos:
- **Entradas**: Batata Frita, Calabresa Acebolada, Torresmo
- **Pratos Principais**: X-Salada, Hambúrguer Artesanal, Bauru, Frango a Passarinho, Porção de Carne
- **Bebidas**: Cerveja, Caipirinha, Refrigerante, Suco
- **Sobremesas**: Pudim, Sorvete

### Jogos:
- **Clássicos**: Xadrez (3 cópias), Damas (2), Monopoly (2)
- **Modernos**: Catan (2), Ticket to Ride (1), Wingspan (1)
- **Partida Rápida**: Sushi Go! (3), Love Letter (2), Splendor (2)
- **Cooperativos**: Pandemic (1), Forbidden Island (1)
- **RPG**: Dungeons & Dragons (1), Call of Cthulhu (1)

## Comandos Úteis

### Popular dados novamente (se necessário):
```bash
python manage.py popular_dados
```

### Migrar dados do JSON:
```bash
python manage.py migrate_json
```

### Criar superusuário (se necessário):
```bash
python manage.py createsuperuser
```

## .gitignore

O arquivo `.gitignore` está configurado para incluir:
- ✅ `db.sqlite3` (banco de dados)
- ✅ `media/` (uploads)
- ❌ `__pycache__/` (cache do Python)
- ❌ `*.pyc` (arquivos compilados)
- ❌ `venv/` (ambiente virtual)

## Próximos Passos

1. ✅ Projeto está pronto para GitHub
2. ✅ Dados já estão populados
3. ✅ Imagens já estão incluídas
4. ✅ Documentação completa

**Agora é só fazer o push para o GitHub!**

