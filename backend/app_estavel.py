import os
import sys
import sqlite3
import webbrowser
import time
from flask import Flask, jsonify, request, send_from_directory, abort
from flask_cors import CORS

BASE_DIR = os.path.dirname(__file__)
DB_PATH = os.path.join(BASE_DIR, '..', 'database', 'clinica.db')
SCHEMA_PATH = os.path.join(BASE_DIR, '..', 'database', 'schema.sql')
FRONT_DIR = os.path.join(BASE_DIR, '..', 'frontend')

app = Flask(__name__, static_folder=FRONT_DIR, static_url_path='')
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Configuração para evitar travamentos
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

def get_conn():
    """Cria conexão com timeout para evitar travamentos"""
    try:
        conn = sqlite3.connect(DB_PATH, timeout=10.0)
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        print(f"[ERRO] Falha ao conectar ao banco: {e}", file=sys.stderr)
        raise

def init_database():
    """Inicializa o banco de dados se não existir"""
    try:
        if not os.path.exists(DB_PATH):
            print("[INFO] Criando banco de dados...")
            os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
            with open(SCHEMA_PATH, 'r', encoding='utf-8') as f:
                schema = f.read()
            with get_conn() as conn:
                conn.executescript(schema)
            print("[INFO] Banco de dados criado com sucesso!")
    except Exception as e:
        print(f"[ERRO] Falha ao inicializar banco: {e}", file=sys.stderr)

@app.route('/')
def index():
    return send_from_directory(FRONT_DIR, 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
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

# ==================== DONOS ====================
@app.get("/api/donos")
def list_donos():
    try:
        with get_conn() as conn:
            cur = conn.execute("SELECT * FROM donos ORDER BY id DESC")
            rows = [dict(r) for r in cur.fetchall()]
            return jsonify(rows)
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.get("/api/donos/<int:dono_id>")
def get_dono(dono_id):
    try:
        with get_conn() as conn:
            cur = conn.execute("SELECT * FROM donos WHERE id = ?", (dono_id,))
            row = cur.fetchone()
            if not row:
                return jsonify({"erro": "dono não encontrado"}), 404
            return jsonify(dict(row))
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.post("/api/donos")
def create_dono():
    try:
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
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.put("/api/donos/<int:dono_id>")
def update_dono(dono_id):
    try:
        data = request.get_json() or {}
        with get_conn() as conn:
            cur = conn.execute(
                """UPDATE donos SET nome=?, telefone=?, email=?, endereco=?, cep=? WHERE id=?""",
                (data.get("nome"), data.get("telefone"), data.get("email"),
                 data.get("endereco"), data.get("cep"), dono_id)
            )
            conn.commit()
            if cur.rowcount == 0:
                return jsonify({"erro": "dono não encontrado"}), 404
            cur = conn.execute("SELECT * FROM donos WHERE id = ?", (dono_id,))
            return jsonify(dict(cur.fetchone()))
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.delete("/api/donos/<int:dono_id>")
def delete_dono(dono_id):
    try:
        with get_conn() as conn:
            cur = conn.execute("DELETE FROM donos WHERE id = ?", (dono_id,))
            conn.commit()
            if cur.rowcount == 0:
                return jsonify({"erro": "dono não encontrado"}), 404
            return jsonify({"deleted": True})
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

# ==================== PETS ====================
@app.get("/api/pets")
def list_pets():
    try:
        with get_conn() as conn:
            cur = conn.execute("""
                SELECT p.*, d.nome as dono_nome 
                FROM pets p 
                LEFT JOIN donos d ON p.dono_id = d.id 
                ORDER BY p.id DESC
            """)
            rows = [dict(r) for r in cur.fetchall()]
            return jsonify(rows)
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.get("/api/pets/<int:pet_id>")
def get_pet(pet_id):
    try:
        with get_conn() as conn:
            cur = conn.execute("SELECT * FROM pets WHERE id = ?", (pet_id,))
            row = cur.fetchone()
            if not row:
                return jsonify({"erro": "pet não encontrado"}), 404
            return jsonify(dict(row))
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.post("/api/pets")
def create_pet():
    try:
        data = request.get_json() or {}
        nome = data.get("nome")
        especie = data.get("especie")
        raca = data.get("raca")
        idade = data.get("idade")
        peso = data.get("peso")
        dono_id = data.get("dono_id")

        if not nome or not especie or not dono_id:
            return jsonify({"erro": "nome, espécie e dono são obrigatórios"}), 400

        with get_conn() as conn:
            cur = conn.execute(
                "INSERT INTO pets (nome, especie, raca, idade, peso, dono_id) VALUES (?, ?, ?, ?, ?, ?)",
                (nome, especie, raca, idade, peso, dono_id)
            )
            conn.commit()
            pet_id = cur.lastrowid
            cur = conn.execute("SELECT * FROM pets WHERE id = ?", (pet_id,))
            return jsonify(dict(cur.fetchone())), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.put("/api/pets/<int:pet_id>")
def update_pet(pet_id):
    try:
        data = request.get_json() or {}
        with get_conn() as conn:
            cur = conn.execute(
                """UPDATE pets SET nome=?, especie=?, raca=?, idade=?, peso=?, dono_id=? WHERE id=?""",
                (data.get("nome"), data.get("especie"), data.get("raca"),
                 data.get("idade"), data.get("peso"), data.get("dono_id"), pet_id)
            )
            conn.commit()
            if cur.rowcount == 0:
                return jsonify({"erro": "pet não encontrado"}), 404
            cur = conn.execute("SELECT * FROM pets WHERE id = ?", (pet_id,))
            return jsonify(dict(cur.fetchone()))
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.delete("/api/pets/<int:pet_id>")
def delete_pet(pet_id):
    try:
        with get_conn() as conn:
            cur = conn.execute("DELETE FROM pets WHERE id = ?", (pet_id,))
            conn.commit()
            if cur.rowcount == 0:
                return jsonify({"erro": "pet não encontrado"}), 404
            return jsonify({"deleted": True})
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

# ==================== VETERINÁRIOS ====================
@app.get("/api/veterinarios")
def list_veterinarios():
    try:
        with get_conn() as conn:
            cur = conn.execute("SELECT * FROM veterinarios ORDER BY id DESC")
            rows = [dict(r) for r in cur.fetchall()]
            return jsonify(rows)
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.get("/api/veterinarios/<int:vet_id>")
def get_veterinario(vet_id):
    try:
        with get_conn() as conn:
            cur = conn.execute("SELECT * FROM veterinarios WHERE id = ?", (vet_id,))
            row = cur.fetchone()
            if not row:
                return jsonify({"erro": "veterinário não encontrado"}), 404
            return jsonify(dict(row))
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.post("/api/veterinarios")
def create_veterinario():
    try:
        data = request.get_json() or {}
        nome = data.get("nome")
        crmv = data.get("crmv")
        especialidade = data.get("especialidade")
        telefone = data.get("telefone")
        email = data.get("email")

        if not nome or not crmv:
            return jsonify({"erro": "nome e CRMV são obrigatórios"}), 400

        with get_conn() as conn:
            cur = conn.execute("SELECT id FROM veterinarios WHERE crmv = ?", (crmv,))
            if cur.fetchone():
                return jsonify({"erro": "CRMV já cadastrado"}), 400

            cur = conn.execute(
                "INSERT INTO veterinarios (nome, crmv, especialidade, telefone, email) VALUES (?, ?, ?, ?, ?)",
                (nome, crmv, especialidade, telefone, email)
            )
            conn.commit()
            vet_id = cur.lastrowid
            cur = conn.execute("SELECT * FROM veterinarios WHERE id = ?", (vet_id,))
            return jsonify(dict(cur.fetchone())), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.put("/api/veterinarios/<int:vet_id>")
def update_veterinario(vet_id):
    try:
        data = request.get_json() or {}
        with get_conn() as conn:
            if data.get("crmv"):
                cur = conn.execute(
                    "SELECT id FROM veterinarios WHERE crmv = ? AND id != ?", 
                    (data.get("crmv"), vet_id)
                )
                if cur.fetchone():
                    return jsonify({"erro": "CRMV já cadastrado para outro veterinário"}), 400

            cur = conn.execute(
                """UPDATE veterinarios SET nome=?, crmv=?, especialidade=?, telefone=?, email=? WHERE id=?""",
                (data.get("nome"), data.get("crmv"), data.get("especialidade"),
                 data.get("telefone"), data.get("email"), vet_id)
            )
            conn.commit()
            if cur.rowcount == 0:
                return jsonify({"erro": "veterinário não encontrado"}), 404
            cur = conn.execute("SELECT * FROM veterinarios WHERE id = ?", (vet_id,))
            return jsonify(dict(cur.fetchone()))
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.delete("/api/veterinarios/<int:vet_id>")
def delete_veterinario(vet_id):
    try:
        with get_conn() as conn:
            cur = conn.execute("DELETE FROM veterinarios WHERE id = ?", (vet_id,))
            conn.commit()
            if cur.rowcount == 0:
                return jsonify({"erro": "veterinário não encontrado"}), 404
            return jsonify({"deleted": True})
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

# ==================== CONSULTAS ====================
@app.get("/api/consultas")
def list_consultas():
    try:
        with get_conn() as conn:
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
            rows = [dict(r) for r in cur.fetchall()]
            return jsonify(rows)
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.post("/api/consultas")
def create_consulta():
    try:
        data = request.get_json() or {}
        required = ['data', 'hora', 'pet_id', 'veterinario_id']
        
        if not all(field in data for field in required):
            return jsonify({"erro": "Campos obrigatórios: data, hora, pet_id, veterinario_id"}), 400

        with get_conn() as conn:
            cur = conn.execute(
                """INSERT INTO consultas (data, hora, motivo, pet_id, veterinario_id)
                   VALUES (?, ?, ?, ?, ?)""",
                (data['data'], data['hora'], data.get('motivo'), 
                 data['pet_id'], data['veterinario_id'])
            )
            conn.commit()
            consulta_id = cur.lastrowid
            
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
            return jsonify(dict(cur.fetchone())), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.delete("/api/consultas/<int:consulta_id>")
def cancel_consulta(consulta_id):
    try:
        with get_conn() as conn:
            cur = conn.execute(
                "UPDATE consultas SET status = 'cancelada' WHERE id = ?",
                (consulta_id,)
            )
            conn.commit()
            if cur.rowcount == 0:
                return jsonify({"erro": "consulta não encontrada"}), 404
            return jsonify({"status": "cancelada"})
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

# Handler de erro global
@app.errorhandler(Exception)
def handle_exception(e):
    print(f"[ERRO] {str(e)}", file=sys.stderr)
    return jsonify({"erro": "Erro interno do servidor", "detalhes": str(e)}), 500

if __name__ == "__main__":
    print("=" * 60)
    print("    SISTEMA DE CLÍNICA VETERINÁRIA - UNIMAR")
    print("=" * 60)
    print()
    
    # Inicializa o banco de dados
    init_database()
    
    print("[INFO] Servidor inicializando...")
    print("[INFO] Acesse: http://127.0.0.1:5000")
    print("[INFO] Pressione CTRL+C para parar o servidor")
    print()
    
    # Abre o navegador após 2 segundos
    try:
        import threading
        def open_browser():
            time.sleep(2)
            webbrowser.open('http://127.0.0.1:5000')
        
        threading.Thread(target=open_browser, daemon=True).start()
    except:
        pass
    
    # Inicia o servidor com configurações mais estáveis
    try:
        app.run(
            host='127.0.0.1',
            port=5000,
            debug=False,  # Desativa debug para evitar reload automático
            threaded=True,  # Permite múltiplas requisições simultâneas
            use_reloader=False  # Desativa reloader que pode causar travamentos
        )
    except KeyboardInterrupt:
        print("\n[INFO] Servidor encerrado pelo usuário")
    except Exception as e:
        print(f"\n[ERRO] Falha ao iniciar servidor: {e}", file=sys.stderr)
        sys.exit(1)
