# 🧪 Scripts de Teste

Esta pasta contém scripts para testar o sistema.

## 📄 Arquivos

### testar_api.py
Script completo para testar todas as funcionalidades da API REST:
- Testa CRUD de Donos
- Testa CRUD de Pets
- Testa CRUD de Veterinários
- Testa CRUD de Consultas
- Testa validações

## 🚀 Como Usar

### Pré-requisito
Certifique-se de que o servidor está rodando:
```powershell
# Em outra janela do terminal, inicie o servidor:
cd c:\Projetos\RA13119972-23
python INICIAR.py
```

### Executar os Testes
```powershell
cd c:\Projetos\RA13119972-23
python tests/testar_api.py
```

## 📊 Saída Esperada

O script irá exibir:
- ✅ Testes bem-sucedidos em verde
- ❌ Falhas em vermelho (se houver)
- Resumo final com estatísticas

---

**Nota:** O servidor precisa estar rodando antes de executar os testes!
