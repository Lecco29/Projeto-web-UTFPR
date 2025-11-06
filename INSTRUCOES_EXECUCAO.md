# Instruções de Execução - Josiel Bar

## Pré-requisitos

Certifique-se de ter Python 3.8 ou superior instalado no seu sistema.

## Passo a Passo para Executar a Aplicação

### 1. Instalar Dependências

Abra o terminal/PowerShell na pasta do projeto e execute:

```bash
pip install -r requirements.txt
```

Ou, se estiver usando Python 3 especificamente:

```bash
python -m pip install -r requirements.txt
```

No Windows, se o comando `python` não funcionar, tente:

```bash
py -m pip install -r requirements.txt
```

### 2. Criar e Aplicar Migrações do Banco de Dados

```bash
python manage.py makemigrations
python manage.py migrate
```

Ou no Windows:

```bash
py manage.py makemigrations
py manage.py migrate
```

### 3. Criar Superusuário (Admin)

Execute o comando para criar um usuário administrador:

```bash
python manage.py createsuperuser
```

Você será solicitado a informar:
- Nome de usuário: (ex: admin)
- Email: (opcional, pode deixar em branco)
- Senha: (ex: admin123)
- Confirmar senha: (digite a mesma senha)

**Credenciais sugeridas:**
- Usuário: `admin`
- Senha: `admin123`

### 4. (Opcional) Migrar Dados dos Arquivos JSON

Se quiser carregar os dados iniciais dos arquivos JSON:

```bash
python manage.py migrate_json
```

Este comando irá:
- Ler os arquivos `json/alimentos_bebidas.json` e `json/jogos.json`
- Criar as categorias e itens no banco de dados
- Preservar dados já existentes (não duplica)

### 5. Iniciar o Servidor

```bash
python manage.py runserver
```

Ou no Windows:

```bash
py manage.py runserver
```

O servidor será iniciado em `http://127.0.0.1:8000/`

### 6. Acessar a Aplicação

- **Site principal**: http://127.0.0.1:8000/
- **Django Admin**: http://127.0.0.1:8000/admin/

## Acesso ao Django Admin

Use as credenciais criadas no passo 3:
- URL: http://127.0.0.1:8000/admin/
- Usuário: admin (ou o que você criou)
- Senha: admin123 (ou a senha que você definiu)

## Funcionalidades Principais

### No Site Público:
- Visualizar cardápio de comidas e bebidas
- Visualizar biblioteca de jogos
- Ver disponibilidade de cópias de jogos

### No Django Admin:
- Gerenciar categorias e itens do cardápio
- Gerenciar categorias e jogos
- **Registrar cópias de jogos** (funcionalidade principal)
- Controlar disponibilidade de cópias (disponível/em uso)
- Ver estatísticas de disponibilidade em tempo real

## Como Registrar Cópias de Jogos

1. Acesse o Django Admin
2. Vá em "Jogos" → selecione um jogo
3. Na parte inferior da página, você verá a seção "Cópias de jogos"
4. Clique em "Adicionar outra Cópia de jogo" ou edite existentes
5. Preencha:
   - **Código**: Código único da cópia (ex: "XAD001", "CAT001")
   - **Disponível**: Marque se está disponível, desmarque se está em uso
   - **Observações**: (opcional) Informações sobre o estado da cópia
6. Salve

A disponibilidade será exibida automaticamente no site público.

## Estrutura de Pastas

```
Codigo/
├── bar/                    # Aplicação Django
│   ├── models.py          # Modelos de dados
│   ├── admin.py           # Configuração do Admin
│   ├── views.py           # Views do site
│   └── ...
├── josielbar/             # Configurações do projeto
├── templates/             # Templates HTML
├── static/                # Arquivos estáticos (CSS, imagens)
│   ├── styles.css
│   └── images/
├── media/                 # Uploads (criado automaticamente)
├── json/                  # Dados originais em JSON
├── db.sqlite3            # Banco de dados (criado automaticamente)
├── manage.py             # Script de gerenciamento Django
└── requirements.txt      # Dependências do projeto
```

## Solução de Problemas

### Erro: "No module named 'django'"
- Instale as dependências: `pip install -r requirements.txt`

### Erro: "Command 'python' not found"
- Use `py` no Windows: `py manage.py runserver`
- Ou use `python3` no Linux/Mac

### Imagens não aparecem
- Certifique-se de que as imagens estão na pasta `static/images/`
- Verifique se o servidor está rodando em modo DEBUG (settings.py)

### Erro ao migrar dados JSON
- Verifique se os arquivos `json/alimentos_bebidas.json` e `json/jogos.json` existem
- Verifique se as migrações foram aplicadas: `python manage.py migrate`

## Desenvolvimento

Para desenvolvimento, o Django está configurado com:
- `DEBUG = True` (modo desenvolvimento)
- Banco SQLite (não precisa de servidor de banco separado)
- Servidor de desenvolvimento integrado

## Produção

Para produção, considere:
- Alterar `DEBUG = False` em `settings.py`
- Configurar um servidor de banco de dados (PostgreSQL, MySQL)
- Configurar um servidor web (Apache, Nginx)
- Usar `collectstatic` para arquivos estáticos

