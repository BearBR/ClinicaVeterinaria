import requests
import json

BASE_URL = "http://127.0.0.1:5000/api"

def print_resultado(titulo, response):
    print(f"\n{'='*60}")
    print(f"TESTE: {titulo}")
    print(f"Status Code: {response.status_code}")
    if response.status_code < 400:
        print(f"Resposta: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")
    else:
        print(f"Erro: {response.text}")
    print(f"{'='*60}")

print("\n🏥 TESTANDO SISTEMA DE CLÍNICA VETERINÁRIA 🏥\n")

# 1. TESTAR DONOS
print("\n📋 === TESTANDO MÓDULO DE DONOS ===")

# Listar donos (deve estar vazio inicialmente)
response = requests.get(f"{BASE_URL}/donos")
print_resultado("Listar Donos (inicial)", response)

# Criar novo dono
novo_dono = {
    "nome": "João Silva",
    "telefone": "(14) 99999-8888",
    "email": "joao@email.com",
    "endereco": "Rua das Flores, 123",
    "cep": "17525-000"
}
response = requests.post(f"{BASE_URL}/donos", json=novo_dono)
print_resultado("Criar Dono", response)
dono_id = response.json().get('id') if response.status_code == 201 else None

if dono_id:
    # Buscar dono por ID
    response = requests.get(f"{BASE_URL}/donos/{dono_id}")
    print_resultado(f"Buscar Dono ID {dono_id}", response)
    
    # Atualizar dono
    dono_atualizado = {
        "nome": "João Silva Santos",
        "telefone": "(14) 99999-7777",
        "email": "joao.santos@email.com",
        "endereco": "Rua das Flores, 123 - Casa 2",
        "cep": "17525-000"
    }
    response = requests.put(f"{BASE_URL}/donos/{dono_id}", json=dono_atualizado)
    print_resultado(f"Atualizar Dono ID {dono_id}", response)

# 2. TESTAR PETS
print("\n🐾 === TESTANDO MÓDULO DE PETS ===")

# Listar pets
response = requests.get(f"{BASE_URL}/pets")
print_resultado("Listar Pets (inicial)", response)

if dono_id:
    # Criar novo pet
    novo_pet = {
        "nome": "Rex",
        "especie": "Cachorro",
        "raca": "Labrador",
        "idade": 3,
        "peso": 25.5,
        "dono_id": dono_id
    }
    response = requests.post(f"{BASE_URL}/pets", json=novo_pet)
    print_resultado("Criar Pet", response)
    pet_id = response.json().get('id') if response.status_code == 201 else None
    
    if pet_id:
        # Buscar pet por ID
        response = requests.get(f"{BASE_URL}/pets/{pet_id}")
        print_resultado(f"Buscar Pet ID {pet_id}", response)
        
        # Atualizar pet
        pet_atualizado = {
            "nome": "Rex Jr",
            "especie": "Cachorro",
            "raca": "Labrador",
            "idade": 4,
            "peso": 27.0,
            "dono_id": dono_id
        }
        response = requests.put(f"{BASE_URL}/pets/{pet_id}", json=pet_atualizado)
        print_resultado(f"Atualizar Pet ID {pet_id}", response)

# 3. TESTAR VETERINÁRIOS
print("\n👨‍⚕️ === TESTANDO MÓDULO DE VETERINÁRIOS ===")

# Listar veterinários
response = requests.get(f"{BASE_URL}/veterinarios")
print_resultado("Listar Veterinários (inicial)", response)

# Criar novo veterinário
novo_vet = {
    "nome": "Dra. Maria Oliveira",
    "crmv": "SP-12345",
    "especialidade": "Clínica Geral",
    "telefone": "(14) 3333-4444",
    "email": "dra.maria@clinica.com"
}
response = requests.post(f"{BASE_URL}/veterinarios", json=novo_vet)
print_resultado("Criar Veterinário", response)
vet_id = response.json().get('id') if response.status_code == 201 else None

if vet_id:
    # Buscar veterinário por ID
    response = requests.get(f"{BASE_URL}/veterinarios/{vet_id}")
    print_resultado(f"Buscar Veterinário ID {vet_id}", response)
    
    # Atualizar veterinário
    vet_atualizado = {
        "nome": "Dra. Maria Oliveira Santos",
        "crmv": "SP-12345",
        "especialidade": "Cirurgia",
        "telefone": "(14) 3333-5555",
        "email": "dra.maria.santos@clinica.com"
    }
    response = requests.put(f"{BASE_URL}/veterinarios/{vet_id}", json=vet_atualizado)
    print_resultado(f"Atualizar Veterinário ID {vet_id}", response)

# 4. TESTAR CONSULTAS
print("\n📅 === TESTANDO MÓDULO DE CONSULTAS ===")

# Listar consultas
response = requests.get(f"{BASE_URL}/consultas")
print_resultado("Listar Consultas (inicial)", response)

if pet_id and vet_id:
    # Criar nova consulta
    nova_consulta = {
        "data": "2025-11-10",
        "hora": "14:00",
        "motivo": "Consulta de rotina e vacinação",
        "pet_id": pet_id,
        "veterinario_id": vet_id
    }
    response = requests.post(f"{BASE_URL}/consultas", json=nova_consulta)
    print_resultado("Criar Consulta", response)
    consulta_id = response.json().get('id') if response.status_code == 201 else None
    
    if consulta_id:
        # Cancelar consulta
        response = requests.delete(f"{BASE_URL}/consultas/{consulta_id}")
        print_resultado(f"Cancelar Consulta ID {consulta_id}", response)

# 5. TESTES DE VALIDAÇÃO
print("\n⚠️ === TESTANDO VALIDAÇÕES ===")

# Tentar criar dono sem nome
response = requests.post(f"{BASE_URL}/donos", json={"telefone": "123456"})
print_resultado("Criar Dono SEM nome (deve falhar)", response)

# Tentar criar pet sem campos obrigatórios
response = requests.post(f"{BASE_URL}/pets", json={"nome": "Miau"})
print_resultado("Criar Pet SEM espécie/dono (deve falhar)", response)

# Tentar criar veterinário com CRMV duplicado
if vet_id:
    response = requests.post(f"{BASE_URL}/veterinarios", json={
        "nome": "Dr. Pedro",
        "crmv": "SP-12345"  # CRMV já existe
    })
    print_resultado("Criar Veterinário com CRMV duplicado (deve falhar)", response)

# Tentar criar consulta sem campos obrigatórios
response = requests.post(f"{BASE_URL}/consultas", json={"motivo": "Teste"})
print_resultado("Criar Consulta SEM campos obrigatórios (deve falhar)", response)

print("\n\n✅ === TESTES CONCLUÍDOS ===\n")
print("Resumo:")
print("- Módulo de Donos: Testado ✓")
print("- Módulo de Pets: Testado ✓")
print("- Módulo de Veterinários: Testado ✓")
print("- Módulo de Consultas: Testado ✓")
print("- Validações: Testadas ✓")
