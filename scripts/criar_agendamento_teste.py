import sqlite3
from datetime import datetime, timedelta

# Conexão com o banco
DB_PATH = 'database/clinica.db'
conn = sqlite3.connect(DB_PATH)
conn.row_factory = sqlite3.Row

# Verificar se existem pets e veterinários
cur = conn.execute("SELECT COUNT(*) as count FROM pets")
pets_count = cur.fetchone()['count']

cur = conn.execute("SELECT COUNT(*) as count FROM veterinarios")
vets_count = cur.fetchone()['count']

# Se não houver registros, vamos criar
if pets_count == 0:
    print("Criando dono e pet de teste...")
    # Criar dono
    cur = conn.execute("""
        INSERT INTO donos (nome, telefone, email, endereco, cep)
        VALUES (?, ?, ?, ?, ?)
    """, ('Maria Silva', '(14) 99999-8888', 'maria@email.com', 'Rua das Flores, 123', '17500-000'))
    dono_id = cur.lastrowid
    
    # Criar pet
    cur = conn.execute("""
        INSERT INTO pets (nome, especie, raca, idade, peso, dono_id)
        VALUES (?, ?, ?, ?, ?, ?)
    """, ('Luna', 'Cachorro', 'Labrador', 3, 25.5, dono_id))
    pet_id = cur.lastrowid
else:
    # Pegar primeiro pet
    cur = conn.execute("SELECT id FROM pets LIMIT 1")
    pet_id = cur.fetchone()['id']

if vets_count == 0:
    print("Criando veterinário de teste...")
    # Criar veterinário
    cur = conn.execute("""
        INSERT INTO veterinarios (nome, crmv, especialidade, telefone, email)
        VALUES (?, ?, ?, ?, ?)
    """, ('Dr. Carlos Santos', 'SP12345', 'Clínica Geral', '(14) 3311-2222', 'carlos@vet.com'))
    vet_id = cur.lastrowid
else:
    # Pegar primeiro veterinário
    cur = conn.execute("SELECT id FROM veterinarios LIMIT 1")
    vet_id = cur.fetchone()['id']

# Data de amanhã
amanha = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
hora = '14:30'  # Horário da consulta

# Criar agendamento
print(f"\nCriando agendamento para {amanha} às {hora}...")
cur = conn.execute("""
    INSERT INTO consultas (data, hora, motivo, status, pet_id, veterinario_id)
    VALUES (?, ?, ?, ?, ?, ?)
""", (amanha, hora, 'Consulta de rotina e vacinação', 'agendada', pet_id, vet_id))

# Commit e fechar conexão
conn.commit()

# Buscar e mostrar detalhes do agendamento
cur = conn.execute("""
    SELECT 
        c.data, c.hora, c.motivo,
        p.nome as pet_nome,
        d.nome as dono_nome,
        v.nome as veterinario_nome
    FROM consultas c
    JOIN pets p ON c.pet_id = p.id
    JOIN donos d ON p.dono_id = d.id
    JOIN veterinarios v ON c.veterinario_id = v.id
    WHERE c.id = ?
""", (cur.lastrowid,))

consulta = cur.fetchone()
print("\nAgendamento criado com sucesso!")
print("================================")
print(f"Data: {consulta['data']}")
print(f"Hora: {consulta['hora']}")
print(f"Pet: {consulta['pet_nome']}")
print(f"Dono: {consulta['dono_nome']}")
print(f"Veterinário: {consulta['veterinario_nome']}")
print(f"Motivo: {consulta['motivo']}")

conn.close()
print("\nBanco de dados atualizado e conexão fechada.")