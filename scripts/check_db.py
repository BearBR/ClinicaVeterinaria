import sqlite3
import json
import os

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'database', 'clinica.db')
DB_PATH = os.path.abspath(DB_PATH)

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = [r[0] for r in cur.fetchall()]
counts = {}
for t in tables:
    try:
        cur.execute(f"SELECT COUNT(*) FROM {t}")
        counts[t] = cur.fetchone()[0]
    except Exception as e:
        counts[t] = str(e)

output = {'db_path': DB_PATH, 'tables': tables, 'counts': counts}
print(json.dumps(output, ensure_ascii=False, indent=2))
conn.close()
