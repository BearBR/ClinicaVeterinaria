import sqlite3, os
DB=r'C:\ClinicaVeterinaria\database\clinica.db'
print('DB path:', DB)
print('Exists:', os.path.exists(DB))
conn=sqlite3.connect(DB)
cur=conn.execute("SELECT name, type FROM sqlite_master WHERE type IN ('table','index') ORDER BY name")
rows=cur.fetchall()
print('Objects in DB:')
for r in rows:
    print(' -', r)
try:
    cur2=conn.execute("SELECT sql FROM sqlite_master WHERE name='usuarios'")
    print('usuarios.sql:', cur2.fetchone())
except Exception as e:
    print('Erro ao obter usuarios schema:', e)
try:
    cur3=conn.execute("SELECT id, username, password, role FROM usuarios")
    print('usuarios rows:')
    for r in cur3.fetchall():
        print('  ', r)
except Exception as e:
    print('Erro ao consultar usuarios:', e)
conn.close()
