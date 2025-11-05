import sqlite3

conn = sqlite3.connect('database/clinica.db')

# Inserir dono
conn.execute("INSERT INTO donos (nome, telefone, email, endereco, cep) VALUES (?, ?, ?, ?, ?)",
             ('João Silva', '(11) 99999-0000', 'joao@example.com', 'Rua A, 123', '01234-567'))

# Inserir veterinário
conn.execute("INSERT INTO veterinarios (nome, crmv, especialidade, telefone, email) VALUES (?, ?, ?, ?, ?)",
             ('Dra. Ana', '12345-SP', 'Cirurgia', '(11) 98888-1111', 'ana@vet.com'))

# Inserir pet
conn.execute("INSERT INTO pets (nome, especie, raca, idade, peso, dono_id) VALUES (?, ?, ?, ?, ?, ?)",
             ('Rex', 'Cão', 'SRD', 3, 12.5, 1))

# Inserir consulta
conn.execute("INSERT INTO consultas (pet_id, veterinario_id, data, hora, motivo, status) VALUES (?, ?, ?, ?, ?, ?)",
             (1, 1, '2025-11-05', '14:30', 'Consulta de rotina', 'agendada'))

conn.commit()
conn.close()

print('✅ Dados de exemplo inseridos com sucesso!')
