# Sistema de Gerenciamento - Clínica Veterinária Unimar# Sistema de Gerenciamento - Clínica Veterinária Unimar



Sistema completo de gerenciamento para clínicas veterinárias com Flask e Bootstrap.Sistema completo de gerenciamento para clínicas veterinárias desenvolvido com Flask e Bootstrap.



## 📋 Funcionalidades##  Descrição



- 👤 **Donos**: Cadastro completo com dados de contatoEste sistema permite gerenciar:

- 🐾 **Pets**: Registro de animais (espécie, raça, idade, peso)-  **Donos de Pets**: Cadastro completo com dados de contato e endereço

- 👨‍⚕️ **Veterinários**: Gestão de profissionais (CRMV, especialidade)-  **Pets**: Registro de animais com informações detalhadas (espécie, raça, idade, peso)

- 📅 **Consultas**: Agendamento e controle de atendimentos-  **Veterinários**: Gestão de profissionais da clínica com CRMV e especialidade

-  **Agendamentos**: Marcação e controle de consultas

---

##  Requisitos

## 🚀 Como Iniciar

- Python 3.8 ou superior

### Método Simples (Recomendado)- pip (gerenciador de pacotes)

- Git (para clonar o repositório)

```

🖱️ Duplo clique em: INICIAR_SERVIDOR.bat##  Instalação e Execução

```

### ⭐ MÉTODO RECOMENDADO - Windows (Mais Fácil)

O navegador abrirá automaticamente em: http://127.0.0.1:5000

**Para usuário final (sem conhecimento técnico):**

### Método por Terminal

1. **Duplo clique no arquivo:** `INICIAR_SERVIDOR.bat`

```powershell2. Aguarde a mensagem: "Acesse: http://127.0.0.1:5000"

pip install -r requirements.txt3. O navegador abrirá automaticamente em: **http://127.0.0.1:5000**

python INICIAR.py

```**Vantagens:**

- ✅ Abre o navegador automaticamente

---- ✅ Reinício automático se o servidor cair

- ✅ Verifica e instala dependências automaticamente

## 📁 Estrutura- ✅ Interface amigável em português

- ✅ Mais estável (sem travamentos)

```- ✅ Não precisa usar terminal

RA13119972-23/

├── backend/           # API Flask**Problemas?** Consulte o arquivo `docs/SOLUCAO_PROBLEMAS.md`

├── frontend/          # Interface HTML/Bootstrap

├── database/          # SQLite---

├── docs/              # Documentação técnica

└── tests/             # Scripts de teste### Método Alternativo 1 - Windows (PowerShell)

```

**Para desenvolvedores:**

---

1. **Clone o repositório:**

## 🛠️ Tecnologias```powershell

git clone https://github.com/BearBR/ClinicaVeterinaria.git

- **Backend**: Flask 3.1.2, Flask-CORScd ClinicaVeterinaria

- **Frontend**: HTML5, Bootstrap 5.3.3, JavaScript```

- **Banco**: SQLite3

2. **Instale as dependências:**

---```powershell

pip install -r requirements.txt

## ⚠️ Problemas?```



**Servidor travando?** → Use `INICIAR_SERVIDOR.bat`3. **Execute o servidor estável:**

```powershell

**Mais ajuda?** → Veja `docs/SOLUCAO_PROBLEMAS.md`python backend/app_estavel.py

```

**Testes?** → Veja `docs/RELATORIO_DE_TESTES.md`

Acesse: http://127.0.0.1:5000

---

---

## 👨‍💻 Desenvolvimento

### Método Alternativo 2 - Com Ambiente Virtual (Windows)

**Desenvolvido por**: Marcio Santos  

**Instituição**: UNIMAR - 2025  1. **Clone o repositório:**

**Disciplina**: Projeto Integrador Extensionista 3```powershell

git clone https://github.com/BearBR/ClinicaVeterinaria.git

**Repositório**: https://github.com/BearBR/ClinicaVeterinariacd ClinicaVeterinaria

```

---

2. **Crie e ative o ambiente virtual:**

## 📖 Documentação Completa```powershell

python -m venv .venv

Para instruções detalhadas de instalação, configuração e resolução de problemas, consulte a pasta `docs/`..\.venv\Scripts\Activate.ps1

```

3. **Instale as dependências:**
```powershell
pip install -r requirements.txt
```

4. **Execute o sistema:**
```powershell
python INICIAR.py
```

O navegador abrirá automaticamente em http://127.0.0.1:5000

### Linux/Mac

1. **Clone o repositório:**
```bash
git clone https://github.com/BearBR/ClinicaVeterinaria.git
cd ClinicaVeterinaria
```

2. **Crie e ative o ambiente virtual:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

4. **Execute o sistema:**
```bash
python INICIAR.py
```

##  Estrutura do Projeto

```
RA13119972-23/
├── backend/
│   ├── app.py              # API Flask com todas as rotas
│   └── app_estavel.py      # ⭐ Versão melhorada e estável
├── database/
│   ├── schema.sql          # Estrutura do banco de dados
│   └── clinica.db          # Banco SQLite (criado automaticamente)
├── frontend/
│   ├── index.html          # Página inicial
│   ├── donos.html          # Gestão de donos
│   ├── pets.html           # Gestão de pets
│   ├── veterinarios.html   # Gestão de veterinários
│   └── consultas.html      # Agendamento de consultas
├── docs/                   # 📖 Documentação
│   ├── RELATORIO_DE_TESTES.md
│   └── SOLUCAO_PROBLEMAS.md
├── tests/                  # 🧪 Scripts de teste
│   └── testar_api.py
├── INICIAR_SERVIDOR.bat    # ⭐ RECOMENDADO - Duplo clique
├── INICIAR.py              # Script Python de inicialização
├── inserir_dados.py        # Popula banco com dados de exemplo
├── gerar_documentacao.py   # Gerador de documentação
├── requirements.txt        # Dependências Python
└── README.md               # Este arquivo
```

##  Funcionalidades

### Módulos Implementados

1. **Donos de Pets**
   - Cadastro completo (nome, telefone, email, endereço, CEP)
   - Listagem com busca e filtros
   - Edição e exclusão de registros
   - Máscaras de entrada para telefone e CEP

2. **Pets**
   - Registro com vinculação ao dono
   - Dados: nome, espécie, raça, idade, peso
   - Visualização de informações completas
   - Gestão de histórico

3. **Veterinários**
   - Cadastro com CRMV único
   - Especialidades
   - Dados de contato
   - Validação de duplicidade

4. **Agendamento de Consultas**
   - Marcação de consultas
   - Seleção de pet e veterinário
   - Tipos de atendimento (consulta, vacina, cirurgia, exame)
   - Controle de status

##  Banco de Dados

O sistema utiliza SQLite. O banco é criado automaticamente na primeira execução.

Para reinicializar o banco de dados, acesse:
```
http://127.0.0.1:5000/api/init-db
```

##  Tecnologias Utilizadas

- **Backend**: Flask 3.1.2, Flask-CORS
- **Frontend**: HTML5, Bootstrap 5.3.3, JavaScript
- **Banco de Dados**: SQLite3
- **Componentes**: DataTables (para tabelas interativas)

##  Notas Importantes

- O banco de dados (database/clinica.db) é criado automaticamente
- Arquivos .venv, __pycache__ e logs são ignorados pelo Git
- O servidor Flask roda em modo de desenvolvimento
- Para produção, considere usar um servidor WSGI como Gunicorn

##  Como Usar o Sistema

### 1️⃣ Iniciar o Sistema
```
Duplo clique em: INICIAR_SERVIDOR.bat
```

### 2️⃣ Acessar a Aplicação
O navegador abrirá automaticamente em: `http://127.0.0.1:5000`

### 3️⃣ Parar o Sistema
- Feche a janela do terminal, OU
- Pressione `Ctrl+C` na janela

### 4️⃣ Inserir Dados de Exemplo (Opcional)
```powershell
python inserir_dados.py
```

---

## ⚠️ Solução de Problemas

### Servidor travando ou caindo?

**SOLUÇÃO:** Use o arquivo `INICIAR_SERVIDOR.bat` (duplo clique)

Este arquivo:
- ✅ Abre o navegador automaticamente
- ✅ Reinicia automaticamente se o servidor cair
- ✅ Verifica dependências
- ✅ Mais estável que o método original

**Documentação completa:** `docs/SOLUCAO_PROBLEMAS.md`
**Relatório de testes:** `docs/RELATORIO_DE_TESTES.md`

### Problemas comuns:

1. **"Python não encontrado"**
   - Instale Python 3.x: https://www.python.org/downloads/
   - Marque "Add Python to PATH" durante instalação

2. **"Porta 5000 já está em uso"**
   - Feche outros servidores rodando
   - Ou mude a porta em `backend/app_estavel.py`

3. **"Banco de dados travado"**
   - Feche todos os terminais
   - Delete `database/clinica.db`
   - Reinicie o servidor (cria novo banco)

##  Desenvolvimento

**Desenvolvido por**: Marcio Santos  
**Instituição**: UNIMAR  
**Ano**: 2025  
**Disciplina**: Projeto Integrador Extensionista 3

##  Licença

Este projeto foi desenvolvido para fins acadêmicos.

---
**Repositório**: https://github.com/BearBR/ClinicaVeterinaria

