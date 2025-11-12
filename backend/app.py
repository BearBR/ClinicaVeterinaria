import os
import sys
import sqlite3
import webbrowser
import time
import threading
from flask import Flask, jsonify, request, send_from_directory, abort
from flask_cors import CORS

BASE_DIR = os.path.dirname(__file__)
DB_PATH = os.path.join(BASE_DIR, '..', 'database', 'clinica.db')
SCHEMA_PATH = os.path.join(BASE_DIR, '..', 'database', 'schema.sql')
FRONT_DIR = os.path.join(BASE_DIR, '..', 'frontend')

app = Flask(__name__, static_folder=FRONT_DIR, static_url_path='')
CORS(app, resources={r"/api/*": {"origins": "*"}})

# config
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

def get_conn():
    conn = sqlite3.connect(DB_PATH, timeout=10.0)
    conn.row_factory = sqlite3.Row
    return conn

def init_database():
    # cria banco se nao tiver ainda
    if not os.path.exists(DB_PATH):
        print("Criando banco...")
        os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
        schema_file = open(SCHEMA_PATH, 'r', encoding='utf-8')
        schema = schema_file.read()
        schema_file.close()
        
        db = get_conn()
        db.executescript(schema)
        db.close()
        print("Banco criado!")

@app.route('/')
def index():
    return send_from_directory(FRONT_DIR, 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    if filename == 'favicon.ico':
        abort(404)
    
    requested_path = os.path.join(FRONT_DIR, filename)
    if os.path.isfile(requested_path):
        return send_from_directory(FRONT_DIR, filename)
    
    html_path = requested_path + '.html'
    if os.path.isfile(html_path):
        return send_from_directory(FRONT_DIR, filename + '.html')
    
    abort(404)

@app.route('/donos')
def page_donos():
    return send_from_directory(FRONT_DIR, 'donos.html')

@app.route('/pets')
def page_pets():
    return send_from_directory(FRONT_DIR, 'pets.html')

@app.route('/veterinarios')
def page_veterinarios():
    return send_from_directory(FRONT_DIR, 'veterinarios.html')

@app.route('/consultas')
def page_consultas():
    return send_from_directory(FRONT_DIR, 'consultas.html')

@app.route('/api/init-db')
def init_db():
    try:
        os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
        with open(SCHEMA_PATH, 'r', encoding='utf-8') as f:
            schema = f.read()
        with get_conn() as conn:
            conn.executescript(schema)
        return jsonify({'status': 'ok'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

# rotas de donos
@app.get("/api/donos")
def list_donos():
    conn = get_conn()
    cur = conn.execute("SELECT * FROM donos ORDER BY id DESC")
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return jsonify(rows)

@app.get("/api/donos/<int:dono_id>")
def get_dono(dono_id):
    conn = get_conn()
    cur = conn.execute("SELECT * FROM donos WHERE id = ?", (dono_id,))
    row = cur.fetchone()
    conn.close()
    if not row:
        return jsonify({"erro": "dono não encontrado"}), 404
    return jsonify(dict(row))

@app.post("/api/donos")
def create_dono():
    data = request.get_json()
    # pega os dados do form
    nome = data.get("nome")
    tel = data.get("telefone")
    email = data.get("email")
    end = data.get("endereco")
    cep = data.get("cep")

    if not nome:
        return jsonify({"erro": "nome obrigatorio"}), 400

    conn = get_conn()
    cur = conn.execute(
        "INSERT INTO donos (nome, telefone, email, endereco, cep) VALUES (?, ?, ?, ?, ?)",
        (nome, tel, email, end, cep)
    )
    conn.commit()
    new_id = cur.lastrowid
    
    # busca o dono criado
    cur = conn.execute("SELECT * FROM donos WHERE id = ?", (new_id,))
    resultado = dict(cur.fetchone())
    conn.close()
    return jsonify(resultado), 201

@app.put("/api/donos/<int:dono_id>")
def update_dono(dono_id):
    data = request.get_json()
    conn = get_conn()
    # atualiza os dados
    cur = conn.execute(
        "UPDATE donos SET nome=?, telefone=?, email=?, endereco=?, cep=? WHERE id=?",
        (data.get("nome"), data.get("telefone"), data.get("email"),
         data.get("endereco"), data.get("cep"), dono_id)
    )
    conn.commit()
    
    if cur.rowcount == 0:
        conn.close()
        return jsonify({"erro": "dono nao encontrado"}), 404
    
    cur = conn.execute("SELECT * FROM donos WHERE id = ?", (dono_id,))
    res = dict(cur.fetchone())
    conn.close()
    return jsonify(res)

@app.delete("/api/donos/<int:dono_id>")
def delete_dono(dono_id):
    conn = get_conn()
    cur = conn.execute("DELETE FROM donos WHERE id = ?", (dono_id,))
    conn.commit()
    conn.close()
    
    if cur.rowcount == 0:
        return jsonify({"erro": "nao encontrado"}), 404
    return jsonify({"deleted": True})

# pets
@app.get("/api/pets")
def list_pets():
    conn = get_conn()
    # busca pets com nome do dono
    cur = conn.execute("""
        SELECT p.*, d.nome as dono_nome 
        FROM pets p 
        LEFT JOIN donos d ON p.dono_id = d.id 
        ORDER BY p.id DESC
    """)
    pets = []
    for r in cur.fetchall():
        pets.append(dict(r))
    conn.close()
    return jsonify(pets)

@app.get("/api/pets/<int:pet_id>")
def get_pet(pet_id):
    conn = get_conn()
    cur = conn.execute("SELECT * FROM pets WHERE id = ?", (pet_id,))
    row = cur.fetchone()
    conn.close()
    
    if not row:
        return jsonify({"erro": "pet nao encontrado"}), 404
    return jsonify(dict(row))

@app.post("/api/pets")
def create_pet():
    data = request.get_json()
    
    nome = data.get("nome")
    especie = data.get("especie")
    raca = data.get("raca")
    idade = data.get("idade")
    peso = data.get("peso")
    dono = data.get("dono_id")

    # validacao basica
    if not nome or not especie or not dono:
        return jsonify({"erro": "faltam campos obrigatorios"}), 400

    conn = get_conn()
    cur = conn.execute(
        "INSERT INTO pets (nome, especie, raca, idade, peso, dono_id) VALUES (?, ?, ?, ?, ?, ?)",
        (nome, especie, raca, idade, peso, dono)
    )
    conn.commit()
    pet_id = cur.lastrowid
    
    cur = conn.execute("SELECT * FROM pets WHERE id = ?", (pet_id,))
    novo_pet = dict(cur.fetchone())
    conn.close()
    
    return jsonify(novo_pet), 201

@app.put("/api/pets/<int:pet_id>")
def update_pet(pet_id):
    data = request.get_json()
    conn = get_conn()
    cur = conn.execute(
        "UPDATE pets SET nome=?, especie=?, raca=?, idade=?, peso=?, dono_id=? WHERE id=?",
        (data.get("nome"), data.get("especie"), data.get("raca"),
         data.get("idade"), data.get("peso"), data.get("dono_id"), pet_id)
    )
    conn.commit()
    
    if cur.rowcount == 0:
        conn.close()
        return jsonify({"erro": "pet nao existe"}), 404
    
    cur = conn.execute("SELECT * FROM pets WHERE id = ?", (pet_id,))
    resultado = dict(cur.fetchone())
    conn.close()
    return jsonify(resultado)

@app.delete("/api/pets/<int:pet_id>")
def delete_pet(pet_id):
    conn = get_conn()
    cur = conn.execute("DELETE FROM pets WHERE id = ?", (pet_id,))
    conn.commit()
    conn.close()
    if cur.rowcount == 0:
        return jsonify({"erro": "nao achei"}), 404
    return jsonify({"deleted": True})

# veterinarios
@app.get("/api/veterinarios")
def list_veterinarios():
    conn = get_conn()
    cur = conn.execute("SELECT * FROM veterinarios ORDER BY id DESC")
    vets = [dict(r) for r in cur.fetchall()]
    conn.close()
    return jsonify(vets)

@app.get("/api/veterinarios/<int:vet_id>")
def get_veterinario(vet_id):
    conn = get_conn()
    cur = conn.execute("SELECT * FROM veterinarios WHERE id = ?", (vet_id,))
    row = cur.fetchone()
    conn.close()
    if not row:
        return jsonify({"erro": "veterinario nao encontrado"}), 404
    return jsonify(dict(row))

@app.post("/api/veterinarios")
def create_veterinario():
    data = request.get_json()
    
    nome = data.get("nome")
    crmv = data.get("crmv")
    espec = data.get("especialidade")
    tel = data.get("telefone")
    email = data.get("email")

    if not nome or not crmv:
        return jsonify({"erro": "nome e crmv obrigatorios"}), 400

    conn = get_conn()
    # verifica se ja tem esse crmv
    cur = conn.execute("SELECT id FROM veterinarios WHERE crmv = ?", (crmv,))
    if cur.fetchone():
        conn.close()
        return jsonify({"erro": "crmv ja existe"}), 400

    cur = conn.execute(
        "INSERT INTO veterinarios (nome, crmv, especialidade, telefone, email) VALUES (?, ?, ?, ?, ?)",
        (nome, crmv, espec, tel, email)
    )
    conn.commit()
    vet_id = cur.lastrowid
    
    cur = conn.execute("SELECT * FROM veterinarios WHERE id = ?", (vet_id,))
    novo = dict(cur.fetchone())
    conn.close()
    return jsonify(novo), 201

@app.put("/api/veterinarios/<int:vet_id>")
def update_veterinario(vet_id):
    data = request.get_json()
    conn = get_conn()
    
    # verifica crmv duplicado
    if data.get("crmv"):
        cur = conn.execute(
            "SELECT id FROM veterinarios WHERE crmv = ? AND id != ?", 
            (data.get("crmv"), vet_id)
        )
        if cur.fetchone():
            conn.close()
            return jsonify({"erro": "crmv ja cadastrado"}), 400

    cur = conn.execute(
        "UPDATE veterinarios SET nome=?, crmv=?, especialidade=?, telefone=?, email=? WHERE id=?",
        (data.get("nome"), data.get("crmv"), data.get("especialidade"),
         data.get("telefone"), data.get("email"), vet_id)
    )
    conn.commit()
    
    if cur.rowcount == 0:
        conn.close()
        return jsonify({"erro": "vet nao encontrado"}), 404
    
    cur = conn.execute("SELECT * FROM veterinarios WHERE id = ?", (vet_id,))
    res = dict(cur.fetchone())
    conn.close()
    return jsonify(res)

@app.delete("/api/veterinarios/<int:vet_id>")
def delete_veterinario(vet_id):
    conn = get_conn()
    cur = conn.execute("DELETE FROM veterinarios WHERE id = ?", (vet_id,))
    conn.commit()
    conn.close()
    
    if cur.rowcount == 0:
        return jsonify({"erro": "nao achado"}), 404
    return jsonify({"deleted": True})

# consultas
@app.get("/api/consultas")
def list_consultas():
    conn = get_conn()
    # query grande com joins pra pegar tudo
    cur = conn.execute("""
        SELECT c.*, 
               p.nome as pet_nome,
               d.nome as dono_nome,
               v.nome as veterinario_nome
        FROM consultas c
        JOIN pets p ON c.pet_id = p.id
        JOIN donos d ON p.dono_id = d.id
        JOIN veterinarios v ON c.veterinario_id = v.id
        ORDER BY c.data DESC, c.hora DESC
    """)
    consultas = [dict(r) for r in cur.fetchall()]
    conn.close()
    return jsonify(consultas)

@app.post("/api/consultas")
def create_consulta():
    data = request.get_json()
    
    # valida campos obrigatorios
    if not data.get('data') or not data.get('hora') or not data.get('pet_id') or not data.get('veterinario_id'):
        return jsonify({"erro": "faltam campos"}), 400

    conn = get_conn()
    cur = conn.execute(
        "INSERT INTO consultas (data, hora, motivo, pet_id, veterinario_id) VALUES (?, ?, ?, ?, ?)",
        (data['data'], data['hora'], data.get('motivo'), data['pet_id'], data['veterinario_id'])
    )
    conn.commit()
    consulta_id = cur.lastrowid
    
    # busca a consulta criada com os joins
    cur = conn.execute("""
        SELECT c.*, 
               p.nome as pet_nome,
               d.nome as dono_nome,
               v.nome as veterinario_nome
        FROM consultas c
        JOIN pets p ON c.pet_id = p.id
        JOIN donos d ON p.dono_id = d.id
        JOIN veterinarios v ON c.veterinario_id = v.id
        WHERE c.id = ?
    """, (consulta_id,))
    
    nova = dict(cur.fetchone())
    conn.close()
    return jsonify(nova), 201

@app.get("/api/consultas/<int:consulta_id>")
def get_consulta(consulta_id):
    conn = get_conn()
    cur = conn.execute("""
        SELECT c.*, 
               p.nome as pet_nome,
               d.nome as dono_nome,
               v.nome as veterinario_nome
        FROM consultas c
        JOIN pets p ON c.pet_id = p.id
        JOIN donos d ON p.dono_id = d.id
        JOIN veterinarios v ON c.veterinario_id = v.id
        WHERE c.id = ?
    """, (consulta_id,))
    
    row = cur.fetchone()
    conn.close()
    
    if not row:
        return jsonify({"erro": "consulta nao existe"}), 404
    return jsonify(dict(row))

@app.put("/api/consultas/<int:consulta_id>")
def update_consulta(consulta_id):
    data = request.get_json()
    conn = get_conn()
    
    # só atualiza se tiver agendada ainda
    cur = conn.execute(
        """
        UPDATE consultas 
        SET data=?, hora=?, motivo=?, pet_id=?, veterinario_id=?
        WHERE id=? AND status='agendada'
        """,
        (data.get('data'), data.get('hora'), data.get('motivo'),
         data.get('pet_id'), data.get('veterinario_id'), consulta_id)
    )
    conn.commit()
    
    if cur.rowcount == 0:
        conn.close()
        return jsonify({"erro": "nao achou ou ja foi cancelada"}), 404
    
    # pega consulta atualizada
    cur = conn.execute("""
        SELECT c.*, 
               p.nome as pet_nome,
               d.nome as dono_nome,
               v.nome as veterinario_nome
        FROM consultas c
        JOIN pets p ON c.pet_id = p.id
        JOIN donos d ON p.dono_id = d.id
        JOIN veterinarios v ON c.veterinario_id = v.id
        WHERE c.id = ?
    """, (consulta_id,))
    
    resultado = dict(cur.fetchone())
    conn.close()
    return jsonify(resultado)

@app.delete("/api/consultas/<int:consulta_id>")
def cancel_consulta(consulta_id):
    conn = get_conn()
    cur = conn.execute(
        "UPDATE consultas SET status = 'cancelada' WHERE id = ?",
        (consulta_id,)
    )
    conn.commit()
    conn.close()
    
    if cur.rowcount == 0:
        return jsonify({"erro": "consulta nao existe"}), 404
    return jsonify({"status": "cancelada"})

# tratamento de erro
@app.errorhandler(404)
def not_found(e):
    return jsonify({"erro": "nao encontrado"}), 404

@app.errorhandler(Exception)
def handle_exception(e):
    print(f"Erro: {str(e)}")
    return jsonify({"erro": "erro no servidor", "detalhes": str(e)}), 500

if __name__ == "__main__":
    print("=" * 50)
    print("  Sistema Clinica Veterinaria - UNIMAR")
    print("=" * 50)
    print()
    
    init_database()
    
    print("Iniciando servidor...")
    print("Abra o navegador em: http://127.0.0.1:5000")
    print("Aperte CTRL+C pra parar")
    print()
    
    # abre navegador depois de 2 seg
    def abrir_browser():
        time.sleep(2)
        webbrowser.open('http://127.0.0.1:5000')
    
    threading.Thread(target=abrir_browser, daemon=True).start()
    
    # inicia servidor
    app.run(
        host='127.0.0.1',
        port=5000,
        debug=False,
        threaded=True,
        use_reloader=False
    )
