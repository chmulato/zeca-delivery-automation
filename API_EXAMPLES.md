# Exemplos de Uso da API

Este arquivo contém exemplos práticos de como consumir os endpoints da API Zeca Delivery.

## Iniciando a API

Primeiro, certifique-se de que a API está rodando:

```bash
python delivery_api.py
```

A API estará disponível em: `http://localhost:5000`

## Exemplos de Requests

### 1. Health Check
Verifica se a API está funcionando:

```bash
curl http://localhost:5000/api/health
```

**Resposta:**
```json
{
  "service": "delivery-api",
  "status": "healthy", 
  "timestamp": "2025-08-04T19:30:00.000000",
  "version": "1.0.0"
}
```

### 2. Listar Todas as Entregas
Obtém a lista completa de entregas:

```bash
curl http://localhost:5000/api/entregas
```

**Resposta:**
```json
{
  "data": [
    {
      "bairro": "Centro",
      "cep": "01010-000",
      "cidade": "São Paulo",
      "cliente": "João Silva",
      "endereco": "Rua das Flores, 123",
      "entrega_prevista": "2025-08-04T19:30:00",
      "estado": "SP",
      "id": 101,
      "prioridade": "normal",
      "produto": "Pizza Calabresa",
      "quantidade": 2,
      "status": "pendente",
      "telefone": "(11) 98765-4321",
      "valor": 45.9
    }
    // ... mais entregas
  ],
  "status": "success",
  "timestamp": "2025-08-04T19:30:00.000000",
  "total": 5
}
```

### 3. Listar Apenas Entregas Pendentes
Filtra apenas entregas com status "pendente":

```bash
curl http://localhost:5000/api/entregas/pendentes
```

### 4. Filtrar por Status Específico
Obtém entregas por status (pendente, em_transito, entregue):

```bash
curl http://localhost:5000/api/entregas/status/em_transito
curl http://localhost:5000/api/entregas/status/entregue
curl http://localhost:5000/api/entregas/status/pendente
```

### 5. Obter Estatísticas
Retorna estatísticas consolidadas:

```bash
curl http://localhost:5000/api/stats
```

**Resposta:**
```json
{
  "stats": {
    "em_transito": 1,
    "entregues": 1,
    "pendentes": 3,
    "taxa_entrega": 20.0,
    "total_entregas": 5,
    "valor_total": 280.9
  },
  "status": "success",
  "timestamp": "2025-08-04T19:30:00.000000"
}
```

## Consumindo com Python

### Exemplo básico com requests:

```python
import requests

# URL base da API
BASE_URL = "http://localhost:5000"

def get_all_deliveries():
    """Obtém todas as entregas"""
    response = requests.get(f"{BASE_URL}/api/entregas")
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro: {response.status_code}")
        return None

def get_pending_deliveries():
    """Obtém apenas entregas pendentes"""
    response = requests.get(f"{BASE_URL}/api/entregas/pendentes")
    return response.json() if response.status_code == 200 else None

def get_statistics():
    """Obtém estatísticas das entregas"""
    response = requests.get(f"{BASE_URL}/api/stats")
    return response.json() if response.status_code == 200 else None

# Uso
if __name__ == "__main__":
    # Testar conexão
    health = requests.get(f"{BASE_URL}/api/health")
    if health.status_code == 200:
        print("API está online!")
        
        # Buscar dados
        deliveries = get_all_deliveries()
        print(f"Total de entregas: {deliveries['total']}")
        
        stats = get_statistics()
        print(f"Valor total: R$ {stats['stats']['valor_total']}")
    else:
        print("API não está respondendo")
```

## Códigos de Status HTTP

| Código | Significado | Quando Ocorre |
|--------|-------------|---------------|
| 200 | Success | Requisição processada com sucesso |
| 404 | Not Found | Endpoint não encontrado |
| 500 | Internal Server Error | Erro interno no servidor |

## Estrutura dos Dados

### Entrega (Delivery Object):
```json
{
  "id": 101,                           // ID único da entrega
  "cliente": "João Silva",             // Nome do cliente
  "endereco": "Rua das Flores, 123",   // Endereço
  "bairro": "Centro",                  // Bairro
  "cidade": "São Paulo",               // Cidade
  "estado": "SP",                      // Estado
  "cep": "01010-000",                  // CEP
  "produto": "Pizza Calabresa",        // Produto
  "quantidade": 2,                     // Quantidade
  "valor": 45.90,                      // Valor em R$
  "telefone": "(11) 98765-4321",       // Telefone
  "entrega_prevista": "2025-08-04T19:30:00", // Data/hora prevista
  "status": "pendente",                // Status atual
  "prioridade": "normal"               // Prioridade
}
```

### Status Possíveis:
- `pendente` - Entrega aguardando envio
- `em_transito` - Entrega a caminho
- `entregue` - Entrega concluída

### Prioridades:
- `normal` - Prioridade padrão
- `alta` - Prioridade alta

## Dicas para Desenvolvimento

1. **Sempre verifique o health check** antes de consumir outros endpoints
2. **Use timeouts** nas requisições para evitar travamentos
3. **Trate erros HTTP** adequadamente
4. **Monitore os logs** da API para debugging
5. **Use o endpoint de estatísticas** para dashboards

## Debugging

### Verificar se a API está rodando:
```bash
# PowerShell/CMD
netstat -an | findstr :5000

# Linux/macOS  
netstat -an | grep :5000
```

### Testar conectividade:
```bash
ping localhost
telnet localhost 5000
```

### Logs da API:
Os logs aparecem no terminal onde você executou `python delivery_api.py`

---

**Estes exemplos demonstram como consumir a API de forma eficiente e robusta!**
