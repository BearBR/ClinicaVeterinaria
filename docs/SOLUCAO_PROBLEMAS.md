# PROBLEMAS COMUNS

## Python não encontrado

Instale Python em: https://www.python.org/downloads/  
Marque "Add Python to PATH" durante instalação.

---

## Servidor travando

Use: `INICIAR_SERVIDOR.bat` (duplo clique)

Este arquivo reinicia automaticamente se o servidor cair.

---

## Porta 5000 em uso

Feche outros programas usando a porta:
```powershell
netstat -ano | findstr :5000
taskkill /PID <numero> /F
```

---

## Banco travado

Feche o servidor e delete: `database/clinica.db`  
O sistema recria automaticamente ao iniciar.
