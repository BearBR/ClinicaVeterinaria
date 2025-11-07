# SOLUÇÃO DE PROBLEMAS

**Sistema:** Clínica Veterinária  
**Aluno:** Marcio Santos - RA 13119972

---

## SERVIDOR TRAVANDO

### Causa
Flask em modo debug no Windows pode travar por conflitos do reloader.

### Solução Recomendada
Execute o arquivo: `INICIAR_SERVIDOR.bat`

**Vantagens:**
- Reinício automático
- Verifica dependências
- Interface simples

### Alternativa
Execute: `python backend/app_estavel.py`

Configurações aplicadas:
- debug=False
- threaded=True
- use_reloader=False
- timeout=10.0

---

## PROBLEMAS COMUNS

### Python não encontrado
Instale Python 3.x e marque "Add Python to PATH" durante instalação.

### Falha nas dependências
```powershell
cd c:\Projetos\RA13119972-23
pip install --upgrade pip
pip install -r requirements.txt
```

### Porta 5000 em uso
Identifique e finalize o processo:
```powershell
netstat -ano | findstr :5000
taskkill /PID <numero> /F
```

### Banco travado
Feche o servidor e delete `database/clinica.db`. O sistema recria automaticamente.

---

## USO

### Iniciar
Duplo clique em `INICIAR_SERVIDOR.bat`

### Parar
Pressione Ctrl+C ou feche o terminal

### Verificar funcionamento
Acesse: http://127.0.0.1:5000/api/donos
