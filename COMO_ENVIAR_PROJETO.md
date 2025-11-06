# Como Enviar o Projeto para um Amigo

## O que é salvo e o que não é

### ✅ O que FICA SALVO (deve enviar):
- **Todo o código**: `bar/`, `josielbar/`, `templates/`, `static/`
- **Migrações**: `bar/migrations/` (importante! Permite recriar o banco)
- **Configurações**: `manage.py`, `requirements.txt`
- **Arquivos estáticos**: `static/images/`, `static/styles.css`
- **Dados JSON originais**: `json/` (para migração)

### ❌ O que NÃO fica salvo (será recriado):
- **Banco de dados**: `db.sqlite3` (será recriado quando rodar `migrate`)
- **Superusuário**: Precisa criar novamente com `createsuperuser`
- **Uploads de imagens**: `media/` (imagens enviadas pelo admin)

## Como Enviar o Projeto

### Opção 1: ZIP (Mais Simples)

1. **Criar arquivo ZIP** com tudo, EXCETO:
   - `db.sqlite3` (não precisa)
   - `media/` (não precisa, a menos que tenha imagens importantes)
   - `__pycache__/` (não precisa)

2. **Ou melhor ainda**: Use o `.gitignore` que já está criado e envie apenas os arquivos necessários

### Opção 2: Git (Recomendado)

Se vocês usam Git:
```bash
git init
git add .
git commit -m "Projeto Django Josiel Bar"
```

## O que seu amigo precisa fazer

### 1. Instalar dependências
```bash
pip install -r requirements.txt
```

### 2. Criar banco de dados
```bash
python manage.py migrate
```

### 3. Criar superusuário
```bash
python manage.py createsuperuser
```
- Usuário: `admin`
- Senha: `admin123` (ou outra)

### 4. (Opcional) Migrar dados do JSON
```bash
python manage.py migrate_json
```

### 5. Rodar o servidor
```bash
python manage.py runserver
```

## Importante sobre os Dados

### Se você quer que seu amigo tenha os MESMOS dados:

**Opção A**: Envie o `db.sqlite3` junto
- Vantagem: Ele terá exatamente tudo que você tem
- Desvantagem: Arquivo pode ser grande

**Opção B**: Use o comando `migrate_json`
- Vantagem: Ele terá os dados iniciais do JSON
- Desvantagem: Não terá os dados que você adicionou manualmente

**Opção C**: Exporte os dados pelo Django Admin
- Vá em Django Admin → Export → JSON
- Mais trabalho, mas mais controle

## Checklist Antes de Enviar

- [ ] Código está funcionando
- [ ] `requirements.txt` está atualizado
- [ ] `README.md` tem instruções
- [ ] `INSTRUCOES_EXECUCAO.md` está completo
- [ ] Decidiu se envia `db.sqlite3` ou não
- [ ] Decidiu se envia `media/` ou não

## Estrutura Mínima para Enviar

```
Codigo/
├── bar/                    ✅ ESSENCIAL
├── josielbar/              ✅ ESSENCIAL
├── templates/              ✅ ESSENCIAL
├── static/                 ✅ ESSENCIAL
├── json/                   ✅ Para migração inicial
├── manage.py               ✅ ESSENCIAL
├── requirements.txt        ✅ ESSENCIAL
├── README.md               ✅ Útil
├── INSTRUCOES_EXECUCAO.md  ✅ Útil
└── .gitignore             ✅ Útil
```

## O que NÃO precisa enviar

- `db.sqlite3` - Pode recriar com `migrate`
- `media/` - Imagens enviadas (a menos que sejam importantes)
- `__pycache__/` - Cache do Python (recriado automaticamente)

