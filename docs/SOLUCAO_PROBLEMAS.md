# 🔧 GUIA DE SOLUÇÃO DE PROBLEMAS
**Sistema de Clínica Veterinária - RA13119972-23**

---

## ⚠️ PROBLEMA: Servidor Flask travando ou caindo

### 🎯 SOLUÇÃO RÁPIDA - Use o arquivo BAT

**RECOMENDADO para usuário final:**

1. **Duplo clique no arquivo:** `INICIAR_SERVIDOR.bat`
2. O sistema irá:
   - ✅ Verificar se Python está instalado
   - ✅ Verificar e instalar dependências automaticamente
   - ✅ Iniciar o servidor
   - ✅ Reiniciar automaticamente se o servidor cair
   - ✅ Perguntar se deseja reiniciar quando parar

**Vantagens:**
- Interface amigável para o usuário
- Reinício automático em caso de falhas
- Não precisa usar terminal/PowerShell
- Mensagens claras em português

---

## 🔧 SOLUÇÕES ALTERNATIVAS

### Opção 1: Usar o servidor estável (app_estavel.py)

O arquivo `backend/app_estavel.py` tem melhorias para evitar travamentos:

```powershell
cd c:\Projetos\RA13119972-23
python backend/app_estavel.py
```

**Melhorias implementadas:**
- ✅ Debug mode desativado (evita reload automático)
- ✅ Threaded=True (múltiplas requisições simultâneas)
- ✅ Use_reloader=False (evita travamentos do reloader)
- ✅ Timeout no banco de dados (10 segundos)
- ✅ Try/catch em todas as rotas
- ✅ Handler de erro global
- ✅ Mensagens de erro mais claras

### Opção 2: Usar o arquivo original com correções

Edite o arquivo `INICIAR.py` para desativar o debug:

**Antes:**
```python
if __name__ == "__main__":
    # ...
    app.run(debug=False)
```

**Depois:**
```python
if __name__ == "__main__":
    # ...
    app.run(debug=False, threaded=True, use_reloader=False)
```

---

## 🐛 CAUSAS COMUNS DO PROBLEMA

### 1. **Debug Mode ativo**
- O modo debug do Flask recarrega automaticamente o código
- Isso pode causar travamentos no Windows
- **Solução:** Desativar debug (`debug=False`)

### 2. **Reloader do Flask**
- O reloader monitora arquivos e reinicia o servidor
- Pode causar conflitos no Windows
- **Solução:** Desativar reloader (`use_reloader=False`)

### 3. **Requisições simultâneas**
- Flask por padrão roda em single-thread
- Requisições múltiplas podem travar
- **Solução:** Ativar threading (`threaded=True`)

### 4. **Navegador abrindo automaticamente**
- `webbrowser.open()` pode travar em alguns sistemas
- **Solução:** Abrir em thread separada com delay

### 5. **Timeout no banco de dados**
- SQLite pode travar sem timeout adequado
- **Solução:** Adicionar `timeout=10.0` na conexão

---

## 📝 INSTRUÇÕES PARA O USUÁRIO FINAL

### Como Iniciar o Sistema (MÉTODO RECOMENDADO)

1. **Localize o arquivo** `INICIAR_SERVIDOR.bat` na pasta do projeto
2. **Duplo clique** no arquivo
3. Uma janela preta (terminal) será aberta
4. Aguarde a mensagem: "Acesse: http://127.0.0.1:5000"
5. Abra seu navegador e vá para: `http://127.0.0.1:5000`

### Se o Servidor Travar ou Cair

**O arquivo BAT irá perguntar automaticamente:**
```
[AVISO] O servidor foi encerrado!

Deseja reiniciar o servidor? (S=Sim, N=Não)
```

- Pressione **S** para reiniciar automaticamente
- Pressione **N** para sair

### Para Parar o Sistema

**Opção 1:** Feche a janela do terminal (X no canto)
**Opção 2:** Pressione `Ctrl+C` no terminal
**Opção 3:** Quando perguntado se deseja reiniciar, pressione `N`

---

## 🚨 PROBLEMAS E SOLUÇÕES

### Problema: "Python não encontrado"

**Erro:**
```
[ERRO] Python não encontrado!
```

**Solução:**
1. Instale o Python 3.x: https://www.python.org/downloads/
2. Durante a instalação, marque "Add Python to PATH"
3. Reinicie o computador
4. Tente novamente

---

### Problema: "Falha ao instalar dependências"

**Erro:**
```
[ERRO] Falha ao instalar dependências
```

**Solução:**
1. Abra o PowerShell como Administrador
2. Execute:
```powershell
cd c:\Projetos\RA13119972-23
pip install --upgrade pip
pip install -r requirements.txt
```

---

### Problema: "Porta 5000 já está em uso"

**Erro:**
```
OSError: [WinError 10048] Apenas um uso de cada endereço de soquete...
```

**Solução:**

**Opção 1 - Fechar processo usando a porta:**
```powershell
# Ver qual processo está usando a porta 5000
netstat -ano | findstr :5000

# Fechar o processo (substitua PID pelo número encontrado)
taskkill /PID <numero_do_pid> /F
```

**Opção 2 - Usar outra porta:**
Edite `backend/app_estavel.py` e altere a linha:
```python
app.run(host='127.0.0.1', port=5001, ...)  # Mudou de 5000 para 5001
```

---

### Problema: "Banco de dados travado"

**Erro:**
```
sqlite3.OperationalError: database is locked
```

**Solução:**
1. Feche todos os terminais/servidores rodando
2. Delete o arquivo: `database/clinica.db`
3. Inicie o servidor novamente (ele cria novo banco)
4. Execute: `python inserir_dados.py` (opcional - dados de exemplo)

---

## 💡 DICAS DE USO

### Para Desenvolvimento

Se você vai modificar o código:
```powershell
# Use o app_estavel.py para desenvolvimento
python backend/app_estavel.py
```

### Para Produção/Uso Final

Use sempre o arquivo `.bat`:
```
Duplo clique em: INICIAR_SERVIDOR.bat
```

### Para Testar API

Use ferramentas como:
- Postman: https://www.postman.com/
- Insomnia: https://insomnia.rest/
- Ou navegador para rotas GET

---

## 📞 SUPORTE

### Logs do Sistema

Os erros são mostrados no terminal com prefixos:
- `[INFO]` - Informações normais
- `[AVISO]` - Avisos (não são erros críticos)
- `[ERRO]` - Erros que impedem funcionamento

### Verificação de Saúde

Teste se o servidor está rodando:
```powershell
# No navegador, acesse:
http://127.0.0.1:5000/api/donos
```

Se retornar JSON `[]` ou dados, está funcionando!

---

## 🔄 COMPARAÇÃO DOS MÉTODOS

| Método | Reinício Automático | Fácil de Usar | Estabilidade | Recomendado |
|--------|-------------------|---------------|--------------|-------------|
| `INICIAR_SERVIDOR.bat` | ✅ Sim | ✅ Muito fácil | ⭐⭐⭐⭐⭐ | ✅ **SIM** |
| `python backend/app_estavel.py` | ❌ Não | ⚠️ Médio | ⭐⭐⭐⭐ | ✅ Sim |
| `python INICIAR.py` (original) | ❌ Não | ⚠️ Médio | ⭐⭐⭐ | ⚠️ Com ressalvas |

---

## ✅ CHECKLIST PARA O USUÁRIO

Antes de iniciar o sistema, verifique:

- [ ] Python 3.x está instalado
- [ ] Dependências instaladas (`pip install -r requirements.txt`)
- [ ] Porta 5000 está livre (nenhum outro servidor rodando)
- [ ] Banco de dados não está corrompido
- [ ] Tem permissões para criar/editar arquivos na pasta

**Se todos os itens acima estão OK:**
- [ ] Use `INICIAR_SERVIDOR.bat` para iniciar
- [ ] Aguarde mensagem de sucesso
- [ ] Acesse http://127.0.0.1:5000

---

**Última atualização:** 05/11/2025  
**Versão do documento:** 1.0
