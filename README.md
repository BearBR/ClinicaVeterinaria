# Sistema de Gerenciamento - Clínica Veterinária PetCare

Sistema completo de gerenciamento para clínicas veterinárias desenvolvido com Flask e Bootstrap.

##  Descrição

Este sistema permite gerenciar:
-  **Donos de Pets**: Cadastro completo com dados de contato e endereço
-  **Pets**: Registro de animais com informações detalhadas (espécie, raça, idade, peso)
-  **Veterinários**: Gestão de profissionais da clínica com CRMV e especialidade
-  **Agendamentos**: Marcação e controle de consultas

##  Requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes)
- Git (para clonar o repositório)

##  Instalação e Execução

### Windows (PowerShell)

1. **Clone o repositório:**
```powershell
git clone https://github.com/BearBR/ClinicaVeterinaria.git
cd ClinicaVeterinaria
```

2. **Crie e ative o ambiente virtual:**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. **Instale as dependências:**
```powershell
pip install -r requirements.txt
```

4. **Execute o sistema:**
```powershell
python run.py
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
python run.py
```

##  Estrutura do Projeto

```
ClinicaVeterinaria/
 backend/
    app.py              # API Flask com todas as rotas
 database/
    schema.sql          # Estrutura do banco de dados
 frontend/
    index.html          # Página inicial
    donos.html          # Gestão de donos
    pets.html           # Gestão de pets
    veterinarios.html   # Gestão de veterinários
    consultas.html      # Agendamento de consultas
 scripts/                # Scripts auxiliares
 requirements.txt        # Dependências Python
 run.py                  # Script de inicialização
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

##  Desenvolvimento

**Autor**: Projeto Integrador - UNIMAR  
**Ano**: 2025  
**Disciplina**: Projeto Integrador Extensionista 3

##  Licença

Este projeto foi desenvolvido para fins acadêmicos.

---
**Repositório**: https://github.com/BearBR/ClinicaVeterinaria
