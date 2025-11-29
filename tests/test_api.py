import importlib
import os
import sqlite3
import json
import tempfile
import re
import pytest

# load app module
app_mod = importlib.import_module('backend.app')

@pytest.fixture
def client(tmp_path, monkeypatch):
    # create a temporary DB file
    db_file = tmp_path / 'test_clinica.db'
    # monkeypatch DB_PATH in module
    monkeypatch.setattr(app_mod, 'DB_PATH', str(db_file))
    # ensure schema file path is correct (reuse existing schema)
    # initialize database/schema
    app_mod.init_database()
    app = app_mod.app
    app.config['TESTING'] = True
    client = app.test_client()
    return client

def test_login_admin(client):
    resp = client.post('/api/login', json={"username":"admin","password":"admin123"})
    assert resp.status_code == 200
    data = resp.get_json()
    assert data.get('role') == 'admin'

def test_create_dono_invalid_cep(client):
    resp = client.post('/api/donos', json={"nome":"T1","cep":"1234"})
    assert resp.status_code == 400

def test_create_dono_valid_cep_and_normalized(client):
    resp = client.post('/api/donos', json={"nome":"T2","cep":"12345-678"})
    assert resp.status_code == 201
    data = resp.get_json()
    dono_id = data['id']
    # fetch and check stored cep is digits-only
    resp2 = client.get(f'/api/donos/{dono_id}')
    assert resp2.status_code == 200
    row = resp2.get_json()
    assert row.get('cep') == '12345678'

def test_update_dono_invalid_cep(client):
    # create a donor
    resp = client.post('/api/donos', json={"nome":"T3","cep":"11111-111"})
    assert resp.status_code == 201
    donor = resp.get_json()
    dono_id = donor['id']
    # attempt invalid update
    resp2 = client.put(f'/api/donos/{dono_id}', json={"cep":"abc"})
    assert resp2.status_code == 400

# Extended validations
def test_create_dono_invalid_phone(client):
    resp = client.post('/api/donos', json={"nome":"P1","telefone":"123"})
    assert resp.status_code == 400

def test_create_dono_invalid_email(client):
    resp = client.post('/api/donos', json={"nome":"E1","email":"not-an-email"})
    assert resp.status_code == 400

def test_create_pet_missing_fields(client):
    resp = client.post('/api/pets', json={"nome":"Pet1"})
    assert resp.status_code == 400

def test_full_pet_consulta_flow(client):
    # create dono
    r1 = client.post('/api/donos', json={"nome":"OwnerPet","cep":"11111-111"})
    assert r1.status_code == 201
    dono_id = r1.get_json()['id']
    # create vet with unique crmv
    import random
    crmv = f'CRMV{random.randint(100000,999999)}'
    r2 = client.post('/api/veterinarios', json={"nome":"Dr","crmv":crmv})
    assert r2.status_code == 201
    vet_id = r2.get_json()['id']
    # create pet
    r3 = client.post('/api/pets', json={"nome":"Rex","especie":"Cachorro","dono_id":dono_id})
    assert r3.status_code == 201
    pet_id = r3.get_json()['id']
    # create consulta
    r4 = client.post('/api/consultas', json={"data":"2025-12-01","hora":"10:00","pet_id":pet_id,"veterinario_id":vet_id})
    assert r4.status_code == 201
