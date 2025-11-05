from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from datetime import datetime

# Criar documento
doc = Document()

# ============================================================================
# CAPA
# ============================================================================
# Título principal
titulo = doc.add_heading('Sistema de Gerenciamento', 0)
titulo.alignment = WD_ALIGN_PARAGRAPH.CENTER
titulo_run = titulo.runs[0]
titulo_run.font.size = Pt(28)
titulo_run.font.color.rgb = RGBColor(0, 51, 102)

# Subtítulo
subtitulo = doc.add_heading('Clínica Veterinária Unimar', 1)
subtitulo.alignment = WD_ALIGN_PARAGRAPH.CENTER
subtitulo_run = subtitulo.runs[0]
subtitulo_run.font.size = Pt(22)
subtitulo_run.font.color.rgb = RGBColor(102, 51, 153)

doc.add_paragraph('\n' * 3)

# Informações do projeto
info = doc.add_paragraph()
info.alignment = WD_ALIGN_PARAGRAPH.CENTER
info_run = info.add_run('Projeto Integrador Extensionista 3\n')
info_run.font.size = Pt(14)
info_run = info.add_run('Universidade de Marília - UNIMAR\n\n')
info_run.font.size = Pt(14)
info_run = info.add_run('Desenvolvido por: Marcio Santos\n')
info_run.font.size = Pt(14)
info_run.bold = True
info_run = info.add_run(f'RA: 13119972\n\n')
info_run.font.size = Pt(14)
info_run.bold = True
info_run = info.add_run(f'{datetime.now().strftime("%B de %Y")}\n')
info_run.font.size = Pt(12)

doc.add_page_break()

# ============================================================================
# SUMÁRIO (Manual)
# ============================================================================
doc.add_heading('Sumário', 1)
sumario_items = [
    '1. Descrição do Sistema',
    '2. Tecnologias Utilizadas',
    '3. Funcionalidades Implementadas',
    '4. Instalação e Execução',
    '5. Manual de Uso',
    '6. Estrutura do Projeto',
    '7. Prints das Telas',
]
for item in sumario_items:
    p = doc.add_paragraph(item)
    p.style = 'List Number'

doc.add_page_break()

# ============================================================================
# 1. DESCRIÇÃO DO SISTEMA
# ============================================================================
doc.add_heading('1. Descrição do Sistema', 1)
doc.add_paragraph(
    'O Sistema de Gerenciamento da Clínica Veterinária Unimar é uma aplicação web completa '
    'desenvolvida para facilitar a administração de clínicas veterinárias. O sistema permite '
    'o gerenciamento integrado de donos de pets, animais de estimação, veterinários e '
    'agendamento de consultas.'
)
doc.add_paragraph(
    'A solução foi desenvolvida com foco em usabilidade, permitindo que qualquer usuário, '
    'mesmo sem conhecimentos técnicos avançados, possa realizar cadastros, consultas, '
    'atualizações e exclusões de registros de forma intuitiva.'
)

# Objetivos
doc.add_heading('Objetivos do Sistema:', 2)
objetivos = [
    'Centralizar informações de donos, pets e veterinários',
    'Facilitar o agendamento e controle de consultas',
    'Proporcionar interface amigável e responsiva',
    'Garantir integridade e persistência dos dados',
    'Otimizar o fluxo de trabalho da clínica veterinária'
]
for obj in objetivos:
    doc.add_paragraph(obj, style='List Bullet')

doc.add_page_break()

# ============================================================================
# 2. TECNOLOGIAS UTILIZADAS
# ============================================================================
doc.add_heading('2. Tecnologias Utilizadas', 1)

doc.add_heading('Flask (Back-end)', 2)
doc.add_paragraph(
    'Framework web em Python para criar aplicações web e APIs. É leve, simples e flexível. '
    'No projeto, o Flask é responsável por todo o back-end, gerenciando o banco de dados '
    'e servindo as páginas HTML através de rotas definidas no arquivo backend/app.py.'
)

doc.add_heading('Bootstrap (Front-end)', 2)
doc.add_paragraph(
    'Framework CSS front-end para criar interfaces responsivas e bonitas rapidamente. '
    'Utilizado em todas as páginas HTML para estilização, incluindo botões, cards, '
    'barra de navegação e formulários. Permite que o sistema seja acessado de qualquer '
    'dispositivo (desktop, tablet ou smartphone) com layout adaptado.'
)

doc.add_heading('SQLite (Banco de Dados)', 2)
doc.add_paragraph(
    'Sistema de gerenciamento de banco de dados relacional leve e embutido. '
    'Perfeito para aplicações de pequeno a médio porte, não requer instalação '
    'de servidor separado. Armazena todos os dados em um único arquivo (clinica.db).'
)

doc.add_heading('Python', 2)
doc.add_paragraph(
    'Linguagem de programação de alto nível, utilizada tanto no back-end (Flask) '
    'quanto nos scripts auxiliares do projeto.'
)

doc.add_heading('HTML5 e JavaScript', 2)
doc.add_paragraph(
    'HTML5 para estruturação das páginas web e JavaScript para interatividade '
    'e comunicação assíncrona com a API REST do back-end.'
)

doc.add_page_break()

# ============================================================================
# 3. FUNCIONALIDADES IMPLEMENTADAS
# ============================================================================
doc.add_heading('3. Funcionalidades Implementadas', 1)

doc.add_heading('3.1 Módulo de Donos de Pets', 2)
funcionalidades_donos = [
    'Cadastro completo com nome, telefone, email, endereço e CEP',
    'Listagem de todos os donos cadastrados',
    'Busca e filtros na tabela',
    'Edição de informações existentes',
    'Exclusão de registros',
    'Máscaras de entrada para telefone (formato brasileiro) e CEP',
    'Validação de dados no formulário'
]
for func in funcionalidades_donos:
    doc.add_paragraph(func, style='List Bullet')

doc.add_heading('3.2 Módulo de Pets (Animais de Estimação)', 2)
funcionalidades_pets = [
    'Cadastro com nome, espécie, raça, idade e peso',
    'Vinculação automática com o dono do pet',
    'Listagem completa com informações do dono',
    'Visualização detalhada de cada animal',
    'Edição de dados cadastrais',
    'Exclusão de registros',
    'Interface intuitiva com seleção do dono via dropdown'
]
for func in funcionalidades_pets:
    doc.add_paragraph(func, style='List Bullet')

doc.add_heading('3.3 Módulo de Veterinários', 2)
funcionalidades_vets = [
    'Cadastro com nome, CRMV, especialidade, email e telefone',
    'Validação de CRMV único (não permite duplicatas)',
    'Listagem de todos os profissionais',
    'Edição de informações profissionais',
    'Exclusão de registros',
    'Máscara de entrada para CRMV (formato: 00000-UF)',
    'Gestão de especialidades médicas veterinárias'
]
for func in funcionalidades_vets:
    doc.add_paragraph(func, style='List Bullet')

doc.add_heading('3.4 Módulo de Agendamento de Consultas', 2)
funcionalidades_consultas = [
    'Agendamento de consultas com data e hora',
    'Seleção do pet e veterinário',
    'Tipos de atendimento: consulta, vacina, cirurgia, exame',
    'Campo para motivo/observações',
    'Controle de status (agendada, realizada, cancelada)',
    'Listagem completa com informações integradas',
    'Visualização de histórico de consultas'
]
for func in funcionalidades_consultas:
    doc.add_paragraph(func, style='List Bullet')

doc.add_page_break()

# ============================================================================
# 4. INSTALAÇÃO E EXECUÇÃO
# ============================================================================
doc.add_heading('4. Instalação e Execução', 1)

doc.add_heading('4.1 Requisitos do Sistema', 2)
requisitos = [
    'Python 3.8 ou superior',
    'pip (gerenciador de pacotes Python)',
    'Navegador web moderno (Chrome, Firefox, Edge)',
    'Sistema operacional: Windows, Linux ou macOS'
]
for req in requisitos:
    doc.add_paragraph(req, style='List Bullet')

doc.add_heading('4.2 Passo a Passo - Windows', 2)
doc.add_paragraph('1. Descompacte o arquivo ra13119972.zip em uma pasta')
doc.add_paragraph('2. Abra o PowerShell na pasta do projeto')
doc.add_paragraph('3. Crie o ambiente virtual:')
doc.add_paragraph('   python -m venv .venv', style='Intense Quote')
doc.add_paragraph('4. Ative o ambiente virtual:')
doc.add_paragraph('   .\\.venv\\Scripts\\Activate.ps1', style='Intense Quote')
doc.add_paragraph('5. Instale as dependências:')
doc.add_paragraph('   pip install -r requirements.txt', style='Intense Quote')
doc.add_paragraph('6. Execute o sistema:')
doc.add_paragraph('   python INICIAR.py', style='Intense Quote')
doc.add_paragraph('7. O navegador abrirá automaticamente em http://127.0.0.1:5000')

doc.add_heading('4.3 Passo a Passo - Linux/Mac', 2)
doc.add_paragraph('1. Descompacte o arquivo ra13119972.zip')
doc.add_paragraph('2. Abra o terminal na pasta do projeto')
doc.add_paragraph('3. Execute os comandos:')
doc.add_paragraph('   python3 -m venv .venv', style='Intense Quote')
doc.add_paragraph('   source .venv/bin/activate', style='Intense Quote')
doc.add_paragraph('   pip install -r requirements.txt', style='Intense Quote')
doc.add_paragraph('   python INICIAR.py', style='Intense Quote')

doc.add_page_break()

# ============================================================================
# 5. MANUAL DE USO
# ============================================================================
doc.add_heading('5. Manual de Uso', 1)

doc.add_heading('5.1 Acessando o Sistema', 2)
doc.add_paragraph(
    'Após executar o comando "python INICIAR.py", o sistema abrirá automaticamente '
    'no navegador padrão. A página inicial apresenta quatro cards principais, '
    'cada um representando um módulo do sistema.'
)

doc.add_heading('5.2 Cadastrando um Dono de Pet', 2)
passos_dono = [
    'Clique no card "Donos de Pets" na página inicial',
    'Preencha o formulário com nome, telefone, email, endereço e CEP',
    'As máscaras de telefone e CEP são aplicadas automaticamente',
    'Clique no botão "Salvar"',
    'O novo dono aparecerá na tabela abaixo',
    'Para editar: clique no botão "Editar" na linha desejada',
    'Para excluir: clique no botão "Excluir" (confirme a ação)'
]
for i, passo in enumerate(passos_dono, 1):
    doc.add_paragraph(f'{i}. {passo}')

doc.add_heading('5.3 Cadastrando um Pet', 2)
passos_pet = [
    'Clique no card "Animais de Estimação"',
    'Selecione o dono do pet no dropdown',
    'Preencha nome, espécie, raça, idade e peso do animal',
    'Clique em "Salvar"',
    'O pet será listado com as informações do dono'
]
for i, passo in enumerate(passos_pet, 1):
    doc.add_paragraph(f'{i}. {passo}')

doc.add_heading('5.4 Cadastrando um Veterinário', 2)
passos_vet = [
    'Clique no card "Veterinários"',
    'Preencha nome, CRMV (formato: 12345-SP), especialidade, email e telefone',
    'O sistema valida se o CRMV já existe',
    'Clique em "Salvar"',
    'O veterinário estará disponível para agendamentos'
]
for i, passo in enumerate(passos_vet, 1):
    doc.add_paragraph(f'{i}. {passo}')

doc.add_heading('5.5 Agendando uma Consulta', 2)
passos_consulta = [
    'Clique no card "Agendamento"',
    'Selecione o pet e o veterinário',
    'Escolha data, hora e tipo de atendimento',
    'Adicione observações sobre o motivo da consulta',
    'Clique em "Agendar Consulta"',
    'A consulta aparecerá na tabela com status "agendada"'
]
for i, passo in enumerate(passos_consulta, 1):
    doc.add_paragraph(f'{i}. {passo}')

doc.add_page_break()

# ============================================================================
# 6. ESTRUTURA DO PROJETO
# ============================================================================
doc.add_heading('6. Estrutura do Projeto', 1)

doc.add_paragraph('O projeto está organizado da seguinte forma:')
doc.add_paragraph('')

estrutura = """ClinicaVeterinaria/
├── backend/
│   └── app.py              # API Flask com todas as rotas
├── database/
│   └── schema.sql          # Estrutura do banco de dados
├── frontend/
│   ├── index.html          # Página inicial (Dashboard)
│   ├── donos.html          # Módulo de donos
│   ├── pets.html           # Módulo de pets
│   ├── veterinarios.html   # Módulo de veterinários
│   └── consultas.html      # Módulo de consultas
├── INICIAR.py              # Script de inicialização
├── requirements.txt        # Dependências do projeto
└── README.md               # Documentação técnica"""

p = doc.add_paragraph(estrutura)
p.style = 'Intense Quote'

doc.add_heading('Descrição dos Arquivos Principais:', 2)
descricoes = [
    'backend/app.py: Contém toda a lógica do servidor, rotas da API REST e conexão com banco de dados',
    'database/schema.sql: Define a estrutura das tabelas (donos, pets, veterinarios, consultas)',
    'frontend/*.html: Páginas web com interface do usuário',
    'INICIAR.py: Script que inicia o servidor Flask e abre o navegador automaticamente',
    'requirements.txt: Lista todas as bibliotecas Python necessárias'
]
for desc in descricoes:
    doc.add_paragraph(desc, style='List Bullet')

doc.add_page_break()

# ============================================================================
# 7. PRINTS DAS TELAS
# ============================================================================
doc.add_heading('7. Prints das Telas do Sistema', 1)

doc.add_paragraph(
    'NOTA: As capturas de tela devem ser inseridas abaixo de cada título. '
    'Tire prints mostrando as funcionalidades em uso (com dados preenchidos).'
)
doc.add_paragraph('')

# Seções para prints
prints_secoes = [
    ('7.1 Página Inicial (Dashboard)', 
     'Print da tela inicial mostrando os quatro cards principais do sistema.'),
    
    ('7.2 Módulo de Donos - Listagem', 
     'Print mostrando a tabela com donos cadastrados e o formulário de cadastro.'),
    
    ('7.3 Módulo de Donos - Cadastro', 
     'Print do formulário preenchido com exemplo de cadastro de um novo dono.'),
    
    ('7.4 Módulo de Pets - Listagem', 
     'Print da tabela de pets mostrando animais cadastrados com seus respectivos donos.'),
    
    ('7.5 Módulo de Pets - Cadastro', 
     'Print do formulário de cadastro de pet com dados de exemplo.'),
    
    ('7.6 Módulo de Veterinários - Listagem', 
     'Print mostrando veterinários cadastrados com CRMV e especialidades.'),
    
    ('7.7 Módulo de Veterinários - Cadastro', 
     'Print do formulário de cadastro de veterinário com dados preenchidos.'),
    
    ('7.8 Módulo de Consultas - Agendamento', 
     'Print da tela de agendamento de consultas com formulário preenchido.'),
    
    ('7.9 Módulo de Consultas - Listagem', 
     'Print da tabela mostrando consultas agendadas com informações completas.')
]

for titulo, descricao in prints_secoes:
    doc.add_heading(titulo, 2)
    doc.add_paragraph(descricao)
    doc.add_paragraph('')
    doc.add_paragraph('[INSERIR PRINT AQUI]')
    doc.add_paragraph('')
    doc.add_paragraph('_' * 80)
    doc.add_paragraph('')

doc.add_page_break()

# ============================================================================
# CONCLUSÃO
# ============================================================================
doc.add_heading('Conclusão', 1)
doc.add_paragraph(
    'O Sistema de Gerenciamento da Clínica Veterinária Unimar foi desenvolvido com sucesso, '
    'atendendo a todos os requisitos propostos pelo projeto integrador. O sistema apresenta '
    'interface intuitiva, funcionalidades completas de CRUD (Create, Read, Update, Delete) '
    'para todos os módulos e integração eficiente entre front-end, back-end e banco de dados.'
)
doc.add_paragraph(
    'A aplicação está pronta para uso em ambiente de clínica veterinária, proporcionando '
    'uma solução completa para gerenciamento de informações e otimização do fluxo de trabalho.'
)

doc.add_paragraph('')
doc.add_paragraph('')
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run('___________________________________\n')
run = p.add_run('Marcio Santos\n')
run.bold = True
run = p.add_run('RA: 13119972\n')
run = p.add_run('UNIMAR - 2025')

# Salvar documento
doc.save('Documentacao_ClinicaVeterinaria_RA13119972.docx')
print("✅ Documentação criada com sucesso!")
print("📄 Arquivo: Documentacao_ClinicaVeterinaria_RA13119972.docx")
print("\n⚠️ IMPORTANTE: Adicione os prints das telas na seção 7 antes de converter para PDF!")
