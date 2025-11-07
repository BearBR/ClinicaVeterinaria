# RELATÓRIO DE TESTES

**Projeto:** Sistema de Clínica Veterinária  
**Aluno:** Marcio Santos - RA 13119972  
**Data:** 05/11/2025

---

## 1. AMBIENTE

- Python 3.13
- Flask 3.1.2
- SQLite3
- Servidor: http://127.0.0.1:5000

---

## 2. METODOLOGIA

Testes funcionais realizados manualmente verificando:
- Inicialização do sistema
- Operações CRUD em todas as entidades
- Validações de dados
- Integridade referencial

---

## 3. RESULTADOS

### 3.1 Inicialização
- Servidor: Operacional
- Banco de dados: Criado automaticamente
- Interface web: Acessível

### 3.2 Módulo Donos
- CREATE: Funcionando
- READ: Funcionando
- UPDATE: Funcionando
- DELETE: Funcionando
- Validações: Nome obrigatório implementado

### 3.3 Módulo Pets
- CREATE: Funcionando com vínculo ao dono
- READ: Funcionando com JOIN
- UPDATE: Funcionando
- DELETE: Funcionando
- Validações: Nome, espécie e dono obrigatórios

### 3.4 Módulo Veterinários
- CREATE: Funcionando
- READ: Funcionando
- UPDATE: Funcionando
- DELETE: Funcionando
- Validações: CRMV único implementado

### 3.5 Módulo Consultas
- CREATE: Funcionando com múltiplos JOINs
- READ: Funcionando
- DELETE: Funcionando (cancelamento)
- Validações: Campos obrigatórios verificados

---

## 4. MÉTRICAS

| Módulo | Funcionalidades | Status |
|--------|----------------|--------|
| Donos | 5 | OK |
| Pets | 5 | OK |
| Veterinários | 5 | OK |
| Consultas | 3 | OK |
| **Total** | **18** | **100%** |

---

## 5. CONCLUSÃO

O sistema atende aos requisitos funcionais propostos. Todas as operações CRUD foram validadas com sucesso. As validações de integridade referencial estão funcionando corretamente.

---

## 6. OBSERVAÇÕES TÉCNICAS

### Banco de Dados
O SQLite é criado automaticamente na primeira execução através do arquivo `schema.sql`.

### API REST
Todas as rotas retornam códigos HTTP apropriados:
- 200: Sucesso
- 201: Criado
- 400: Erro de validação
- 404: Não encontrado
- 500: Erro do servidor

### Limitações Identificadas
- Servidor de desenvolvimento (Flask built-in)
- Sem autenticação implementada
- Sem paginação nas listagens
