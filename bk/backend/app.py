import os
import sqlite3
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

BASE_DIR = os.path.dirname(__file__)
DB_PATH = os.path.join(BASE_DIR, '..', 'database', 'clinica.db')
SCHEMA_PATH = os.path.join(BASE_DIR, '..', 'database', 'schema.sql')
FRONT_DIR = os.path.join(BASE_DIR, '..', 'frontend')

app = Flask(__name__, static_folder=FRONT_DIR, static_url_path='')
CORS(app, resources={r"/api/*": {"origins": "*"}})

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return send_from_directory(FRONT_DIR, 'index.html')

@app.route('/api/init-db')
def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    with open(SCHEMA_PATH, 'r', encoding='utf-8') as f:
        schema = f.read()
    with get_conn() as conn:
        conn.executescript(schema)
    return jsonify({'status': 'ok'})

# LISTAR DONOS
@app.get("/api/donos")
def list_donos():
    with get_conn() as conn:
        cur = conn.execute("SELECT * FROM donos ORDER BY id DESC")
        rows = [dict(r) for r in cur.fetchall()]
        return jsonify(rows)

# PEGAR DONO POR ID (para editar)
@app.get("/api/donos/<int:dono_id>")
def get_dono(dono_id):
    with get_conn() as conn:
        cur = conn.execute("SELECT * FROM donos WHERE id = ?", (dono_id,))
        row = cur.fetchone()
        if not row:
            return jsonify({"erro": "dono não encontrado"}), 404
        return jsonify(dict(row))

# CRIAR DONO
@app.post("/api/donos")
def create_dono():
    data = request.get_json() or {}
    nome = data.get("nome")
    telefone = data.get("telefone")
    email = data.get("email")
    endereco = data.get("endereco")
    cep = data.get("cep")

    if not nome:
        return jsonify({"erro": "nome é obrigatório"}), 400

    with get_conn() as conn:
        cur = conn.execute(
            "INSERT INTO donos (nome, telefone, email, endereco, cep) VALUES (?, ?, ?, ?, ?)",
            (nome, telefone, email, endereco, cep)
        )
        conn.commit()
        dono_id = cur.lastrowid
        cur = conn.execute("SELECT * FROM donos WHERE id = ?", (dono_id,))
        return jsonify(dict(cur.fetchone())), 201

# ATUALIZAR DONO
@app.put("/api/donos/<int:dono_id>")
def update_dono(dono_id):
    data = request.get_json() or {}
    with get_conn() as conn:
        cur = conn.execute(
            """
            UPDATE donos SET nome=?, telefone=?, email=?, endereco=?, cep=? WHERE id=?
            """,
            (
                data.get("nome"), data.get("telefone"), data.get("email"),
                data.get("endereco"), data.get("cep"), dono_id
            )
        )
        conn.commit()
        if cur.rowcount == 0:
            return jsonify({"erro": "dono não encontrado"}), 404
        cur = conn.execute("SELECT * FROM donos WHERE id = ?", (dono_id,))
        row = cur.fetchone()
        return jsonify(dict(row))

# EXCLUIR DONO
@app.delete("/api/donos/<int:dono_id>")
def delete_dono(dono_id):
    with get_conn() as conn:
        cur = conn.execute("DELETE FROM donos WHERE id = ?", (dono_id,))
        conn.commit()
        if cur.rowcount == 0:
            return jsonify({"erro": "dono não encontrado"}), 404
        return jsonify({"deleted": True})

if __name__ == "__main__":
    app.run(debug=True)
