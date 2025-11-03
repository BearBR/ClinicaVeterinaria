import sqlite3

DB_PATH = r'C:\Users\masco\OneDrive\Unimar\Projeto Integrador Ext 3\RA13119972-23\database\clinica.db'

try:
    conn = sqlite3.connect(DB_PATH)
    cur = conn.execute("SELECT * FROM donos")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    conn.close()
    print("Banco acessado com sucesso.")
except Exception as e:
    print("Erro ao acessar o banco:", e)
