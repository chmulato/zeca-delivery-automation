# 📖 Documentação da API - Zeca Delivery

## Visão Geral

A API REST do sistema Zeca Delivery fornece endpoints para gerenciar entregas de delivery. Desenvolvida em Flask, oferece dados estruturados em formato JSON para consumo por aplicações externas.

**Base URL:** `http://localhost:5000`

---

## 🏠 Endpoint Principal

### `GET /`
Página inicial da API com informações básicas.

**Resposta:**
```json
{
  "service": "Zeca Delivery API",
  "version": "1.0.0", 
  "description": "API para automação de entregas",
  "endpoints": {
    "health": "/api/health",
    "entregas": "/api/entregas",
    "pendentes": "/api/entregas/pendentes", 
    "por_status": "/api/entregas/status/<status>",
    "estatisticas": "/api/stats"
  },
  "article": "Sistema baseado no artigo: Como o Python Automatizou a Logística de Entregas"
}
```

---

## 🔍 Health Check

### `GET /api/health`
Verifica se a API está funcionando corretamente.

**Resposta de Sucesso:**
```json
{
  "status": "healthy",
  "service": "delivery-api", 
  "version": "1.0.0",
  "timestamp": "2025-08-04T19:30:00.123456",
  "uptime": "running",
  "database": "mock_data_ready"
}
```

---

## 📦 Endpoints de Entregas

### `GET /api/entregas`
Retorna todas as entregas cadastradas.

**Resposta de Sucesso:**
```json
{
  "status": "success",
  "timestamp": "2025-08-04T19:30:00.123456",
  "total": 5,
  "data": [
    {
      "id": 101,
      "cliente": "João Silva",
      "endereco": "Rua das Flores, 123",
      "bairro": "Centro", 
      "cidade": "São Paulo",
      "estado": "SP",
      "cep": "01010-000",
      "produto": "Pizza Calabresa",
      "quantidade": 2,
      "valor": 45.90,
      "telefone": "(11) 98765-4321",
      "entrega_prevista": "2025-08-04T19:30:00",
      "status": "pendente",
      "prioridade": "normal"
    }
    // ... mais entregas
  ]
}
```

### `GET /api/entregas/pendentes`
Retorna apenas entregas com status "pendente".

**Resposta:** Mesmo formato do endpoint principal, mas filtrado.

### `GET /api/entregas/status/<status>`
Filtra entregas por status específico.

**Parâmetros:**
- `status` (string): Status desejado

**Status Válidos:**
- `pendente`
- `em_transito` 
- `entregue`
- `cancelado`

**Exemplo de Uso:**
```
GET /api/entregas/status/em_transito
```

**Resposta de Erro (Status Inválido):**
```json
{
  "status": "error",
  "timestamp": "2025-08-04T19:30:00.123456",
  "message": "Status inválido. Use: pendente, em_transito, entregue, cancelado",
  "data": []
}
```

---

## 📊 Estatísticas

### `GET /api/stats`
Retorna estatísticas consolidadas das entregas.

**Resposta de Sucesso:**
```json
{
  "status": "success",
  "timestamp": "2025-08-04T19:30:00.123456", 
  "data": {
    "total_entregas": 5,
    "valor_total": 280.90,
    "taxa_entrega": 20.0,
    "valor_medio": 56.18,
    "distribuicao_status": {
      "pendente": 3,
      "em_transito": 1,
      "entregue": 1
    }
  }
}
```

**Campos Explicados:**
- `total_entregas`: Número total de entregas
- `valor_total`: Soma de todos os valores (R$)
- `taxa_entrega`: Percentual de entregas concluídas
- `valor_medio`: Valor médio por entrega (R$)
- `distribuicao_status`: Contagem por status

---

## ❌ Tratamento de Erros

### Códigos de Status HTTP

| Código | Descrição |
|--------|-----------|
| 200 | Sucesso |
| 400 | Requisição inválida (ex: status inválido) |
| 404 | Endpoint não encontrado |
| 500 | Erro interno do servidor |

### Formato de Resposta de Erro

```json
{
  "status": "error",
  "timestamp": "2025-08-04T19:30:00.123456",
  "message": "Descrição do erro",
  "data": []
}
```

### Exemplo - Endpoint Não Encontrado
```
GET /api/inexistente
```

**Resposta (404):**
```json
{
  "status": "error", 
  "timestamp": "2025-08-04T19:30:00.123456",
  "message": "Endpoint não encontrado",
  "data": {}
}
```

---

## 🔧 Estrutura dos Dados

### Objeto Entrega

| Campo | Tipo | Descrição | Exemplo |
|-------|------|-----------|---------|
| `id` | integer | Identificador único | 101 |
| `cliente` | string | Nome do cliente | "João Silva" |
| `endereco` | string | Rua e número | "Rua das Flores, 123" |
| `bairro` | string | Bairro | "Centro" |
| `cidade` | string | Cidade | "São Paulo" |
| `estado` | string | Estado (sigla) | "SP" |
| `cep` | string | CEP formatado | "01010-000" |
| `produto` | string | Item a ser entregue | "Pizza Calabresa" |
| `quantidade` | integer | Quantidade do produto | 2 |
| `valor` | float | Valor em reais | 45.90 |
| `telefone` | string | Contato do cliente | "(11) 98765-4321" |
| `entrega_prevista` | string | Data/hora ISO | "2025-08-04T19:30:00" |
| `status` | string | Status atual | "pendente" |
| `prioridade` | string | Prioridade | "normal" |

### Status Possíveis
- **pendente**: Aguardando saída para entrega
- **em_transito**: Entregador a caminho
- **entregue**: Entrega concluída com sucesso
- **cancelado**: Entrega cancelada

### Prioridades
- **normal**: Prioridade padrão
- **alta**: Prioridade elevada
- **urgente**: Máxima prioridade

---

## 🧪 Testando a API

### Usando curl (Terminal)

```bash
# Health check
curl http://localhost:5000/api/health

# Listar todas as entregas
curl http://localhost:5000/api/entregas

# Entregas pendentes
curl http://localhost:5000/api/entregas/pendentes

# Entregas por status
curl http://localhost:5000/api/entregas/status/entregue

# Estatísticas
curl http://localhost:5000/api/stats
```

### Usando Python (requests)

```python
import requests

# Base URL
base_url = "http://localhost:5000"

# Health check
response = requests.get(f"{base_url}/api/health")
print(response.json())

# Listar entregas
response = requests.get(f"{base_url}/api/entregas")
entregas = response.json()
print(f"Total: {entregas['total']} entregas")

# Estatísticas
response = requests.get(f"{base_url}/api/stats")
stats = response.json()['data']
print(f"Valor total: R$ {stats['valor_total']}")
```

---

## 📈 Monitoramento

### Logs da API
A API exibe logs no terminal durante execução:

```
🚀 Iniciando API de Entregas Zeca...
📍 Endpoints disponíveis:
   GET /api/entregas - Todas as entregas
   GET /api/health - Health check
🌐 API rodando em: http://localhost:5000
```

### Verificação de Saúde
Use o endpoint `/api/health` para monitoramento automatizado.

---

## 🚀 Executando a API

```bash
# Navegar para o diretório
cd zeca-delivery-automation

# Iniciar a API
python api/delivery_api.py
```

A API estará disponível em `http://localhost:5000` com debug ativado.

---

## 💡 Próximos Passos

Esta API serve como base para expansões:

- 🔐 **Autenticação** com JWT
- 🗄️ **Banco de dados** real (PostgreSQL/MySQL)  
- 🔄 **CRUD completo** (POST, PUT, DELETE)
- 📧 **Notificações** por email/SMS
- 🗺️ **Integração** com APIs de mapas
- 📱 **Versionamento** da API (v1, v2)

Para implementar essas funcionalidades, consulte a documentação oficial do [Flask](https://flask.palletsprojects.com/).
