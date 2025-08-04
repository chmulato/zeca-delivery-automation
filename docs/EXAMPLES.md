# Exemplos de Uso - Zeca Delivery

Este arquivo contém exemplos práticos de como usar o sistema Zeca Delivery em diferentes cenários.

---

## Cenário 1: Execução Básica

### Passo a Passo Completo

```bash
# 1. Clone e configure
git clone git@github.com:chmulato/zeca-delivery-automation.git
cd zeca-delivery-automation
python setup.py

# 2. Inicie a API (Terminal 1)
python api/delivery_api.py

# 3. Gere relatório (Terminal 2)  
python reports/excel_generator.py
```

**Resultado:** Arquivo `relatorio_entregas_YYYYMMDD_HHMMSS.xlsx` criado.

---

## Cenário 2: Consumindo a API com Python

### Script Personalizado

```python
import requests
import json
from datetime import datetime

class ZecaDeliveryClient:
    def __init__(self, base_url="http://localhost:5000"):
        self.base_url = base_url
    
    def get_all_deliveries(self):
        """Busca todas as entregas"""
        response = requests.get(f"{self.base_url}/api/entregas")
        return response.json()
    
    def get_pending_deliveries(self):
        """Busca apenas entregas pendentes"""
        response = requests.get(f"{self.base_url}/api/entregas/pendentes")
        return response.json()
    
    def get_delivery_stats(self):
        """Busca estatísticas"""
        response = requests.get(f"{self.base_url}/api/stats")
        return response.json()
    
    def show_daily_summary(self):
        """Exibe resumo do dia"""
        print("RESUMO DIÁRIO - ZECA DELIVERY")
        print("=" * 40)
        
        # Estatísticas
        stats_response = self.get_delivery_stats()
        if stats_response['status'] == 'success':
            stats = stats_response['data']
            print(f"Total de entregas: {stats['total_entregas']}")
            print(f"Valor total: R$ {stats['valor_total']:.2f}")
            print(f"Taxa de entrega: {stats['taxa_entrega']:.1f}%")
            print(f"Valor médio: R$ {stats['valor_medio']:.2f}")
            
            print("\nDistribuição por status:")
            for status, count in stats['distribuicao_status'].items():
                print(f"  {status.replace('_', ' ').title()}: {count}")
        
        # Entregas pendentes
        pending_response = self.get_pending_deliveries()
        if pending_response['status'] == 'success':
            pending = pending_response['data']
            print(f"\nEntregas pendentes ({len(pending)}):")
            for entrega in pending:
                print(f"  • {entrega['cliente']} - {entrega['produto']} - R$ {entrega['valor']:.2f}")

# Uso do cliente
if __name__ == "__main__":
    client = ZecaDeliveryClient()
    client.show_daily_summary()
```

**Output Esperado:**
```
RESUMO DIÁRIO - ZECA DELIVERY
========================================
Total de entregas: 5
Valor total: R$ 280.90
Taxa de entrega: 20.0%
Valor médio: R$ 56.18

Distribuição por status:
  Pendente: 3
  Em Transito: 1
  Entregue: 1

Entregas pendentes (3):
  • João Silva - Pizza Calabresa - R$ 45.90
  • Carlos Oliveira - Pizza Portuguesa - R$ 89.70
  • Pedro Ferreira - Pizza Pepperoni - R$ 67.80
```

---

## Cenário 3: Monitoramento Automatizado

### Script de Monitoramento

```python
import requests
import time
from datetime import datetime

def monitor_api_health():
    """Monitora saúde da API continuamente"""
    base_url = "http://localhost:5000"
    
    while True:
        try:
            response = requests.get(f"{base_url}/api/health", timeout=5)
            timestamp = datetime.now().strftime("%H:%M:%S")
            
            if response.status_code == 200:
                print(f"[OK] {timestamp} - API Online")
            else:
                print(f"[WARN] {timestamp} - API com problemas (Status: {response.status_code})")
                
        except requests.exceptions.ConnectionError:
            timestamp = datetime.now().strftime("%H:%M:%S")
            print(f"[ERROR] {timestamp} - API Offline")
        except Exception as e:
            timestamp = datetime.now().strftime("%H:%M:%S")
            print(f"[ERROR] {timestamp} - Erro: {e}")
        
        time.sleep(30)  # Verificar a cada 30 segundos

# Executar monitoramento
# monitor_api_health()
```

---

## Cenário 4: Integração com WhatsApp (Conceitual)

### Simulação de Bot

```python
import requests

class WhatsAppIntegration:
    def __init__(self, api_url="http://localhost:5000"):
        self.api_url = api_url
    
    def process_delivery_request(self, customer_message):
        """Simula processamento de mensagem do WhatsApp"""
        
        # Exemplo de mensagem: "Pizza Margherita para Rua ABC, 123"
        if "pizza" in customer_message.lower():
            # Simular criação de entrega
            delivery_data = self.parse_message(customer_message)
            
            # Em um sistema real, faria POST para criar entrega
            print(f"Nova entrega criada: {delivery_data}")
            
            # Buscar status atual
            return self.get_delivery_status_message()
    
    def parse_message(self, message):
        """Parse básico da mensagem (simulado)"""
        return {
            "produto": "Pizza Margherita",
            "endereco": "Rua ABC, 123", 
            "valor": 35.50,
            "status": "pendente"
        }
    
    def get_delivery_status_message(self):
        """Gera mensagem de status para WhatsApp"""
        try:
            response = requests.get(f"{self.api_url}/api/entregas/pendentes")
            data = response.json()
            
            if data['status'] == 'success':
                pending_count = data['total']
                return f"Pedido recebido! {pending_count} entregas na fila."
            else:
                return "Erro ao processar pedido."
        except:
            return "Sistema temporariamente indisponível."

# Simulação
bot = WhatsAppIntegration()
response = bot.process_delivery_request("Quero uma Pizza Margherita para Rua ABC, 123")
print(response)
```

---

## Cenário 5: Automação com Agenda

### Relatório Automático Diário

```python
import schedule
import time
from reports.excel_generator import DeliveryReportGenerator

def generate_daily_report():
    """Gera relatório diário automaticamente"""
    print("Gerando relatório diário automático...")
    
    generator = DeliveryReportGenerator()
    success = generator.generate_report()
    
    if success:
        print("Relatório diário gerado com sucesso!")
    else:
        print("Falha na geração do relatório diário")

# Agendar para executar todos os dias às 18:00
schedule.every().day.at("18:00").do(generate_daily_report)

# Agendar para executar a cada 4 horas
schedule.every(4).hours.do(generate_daily_report)

# Loop principal (executar em produção)
def run_scheduler():
    print("Agendador iniciado...")
    while True:
        schedule.run_pending()
        time.sleep(60)  # Verificar a cada minuto

# Para executar: 
# run_scheduler()
```

---

## Cenário 6: Dashboard em Tempo Real

### Servidor Web Simples

```python
from flask import Flask, render_template_string
import requests

app = Flask(__name__)

@app.route('/dashboard')
def dashboard():
    """Dashboard web simples"""
    try:
        # Buscar dados da API
        response = requests.get("http://localhost:5000/api/stats")
        stats = response.json()['data']
        
        # Buscar entregas pendentes
        pending_response = requests.get("http://localhost:5000/api/entregas/pendentes")
        pending = pending_response.json()['data']
        
        # Template HTML simples
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Dashboard Zeca Delivery</title>
            <meta charset="utf-8">
            <style>
                body { font-family: Arial; margin: 40px; }
                .stat { padding: 20px; margin: 10px; background: #f0f0f0; }
                .pending { background: #fff3cd; }
                h1 { color: #366092; }
            </style>
        </head>
        <body>
            <h1>Dashboard Zeca Delivery</h1>
            
            <div class="stat">
                <h3>Total de Entregas</h3>
                <p>{{ stats.total_entregas }}</p>
            </div>
            
            <div class="stat">
                <h3>Valor Total</h3>
                <p>R$ {{ "%.2f"|format(stats.valor_total) }}</p>
            </div>
            
            <div class="stat">
                <h3>Taxa de Entrega</h3>
                <p>{{ "%.1f"|format(stats.taxa_entrega) }}%</p>
            </div>
            
            <div class="stat pending">
                <h3>Entregas Pendentes ({{ pending|length }})</h3>
                {% for entrega in pending %}
                <p>• {{ entrega.cliente }} - {{ entrega.produto }} - R$ {{ "%.2f"|format(entrega.valor) }}</p>
                {% endfor %}
            </div>
        </body>
        </html>
        """
        
        return render_template_string(html, stats=stats, pending=pending)
        
    except Exception as e:
        return f"Erro: {e}"

if __name__ == "__main__":
    print("Dashboard disponível em: http://localhost:8000/dashboard")
    app.run(port=8000, debug=True)
```

**Acesso:** http://localhost:8000/dashboard

---

## Cenário 7: Testes Automatizados

### Script de Teste Completo

```python
import requests
import time

def test_full_system():
    """Testa todo o sistema automaticamente"""
    base_url = "http://localhost:5000"
    
    print("INICIANDO TESTES DO SISTEMA")
    print("=" * 40)
    
    tests = [
        ("Health Check", f"{base_url}/api/health"),
        ("Todas as entregas", f"{base_url}/api/entregas"),
        ("Entregas pendentes", f"{base_url}/api/entregas/pendentes"),
        ("Entregas em trânsito", f"{base_url}/api/entregas/status/em_transito"),
        ("Estatísticas", f"{base_url}/api/stats")
    ]
    
    results = []
    
    for test_name, url in tests:
        try:
            start_time = time.time()
            response = requests.get(url, timeout=5)
            response_time = time.time() - start_time
            
            if response.status_code == 200:
                data = response.json()
                if data.get('status') == 'success' or 'healthy' in str(data):
                    results.append(f"[PASS] {test_name} - {response_time:.2f}s")
                else:
                    results.append(f"[WARN] {test_name} - Resposta inesperada")
            else:
                results.append(f"[FAIL] {test_name} - Status {response.status_code}")
                
        except Exception as e:
            results.append(f"[ERROR] {test_name} - Erro: {e}")
    
    # Resultados
    print("\nRESULTADOS DOS TESTES:")
    for result in results:
        print(f"  {result}")
    
    # Resumo
    passed = len([r for r in results if r.startswith("[PASS]")])
    total = len(results)
    print(f"\nRESUMO: {passed}/{total} testes passaram")
    
    return passed == total

# Executar testes
if __name__ == "__main__":
    success = test_full_system()
    if success:
        print("Todos os testes passaram!")
    else:
        print("Alguns testes falharam. Verifique a API.")
```

---

## Cenário 8: Personalização dos Dados

### Modificando Dados de Exemplo

```python
# Editar: data/sample_data.py

# Adicionar nova entrega
nova_entrega = {
    "id": 106,
    "cliente": "Lucia Santos",
    "endereco": "Av. Brasil, 555",
    "bairro": "Vila Madalena",
    "cidade": "São Paulo",
    "estado": "SP",
    "cep": "05449-000",
    "produto": "Pizza Vegetariana",
    "quantidade": 1,
    "valor": 52.50,
    "telefone": "(11) 94321-8765",
    "entrega_prevista": "2025-08-04T21:30:00",
    "status": "pendente",
    "prioridade": "alta"
}

# Adicionar à lista ENTREGAS_MOCK
ENTREGAS_MOCK.append(nova_entrega)
```

### Modificando Formatação do Excel

```python
# Editar: reports/excel_generator.py

# Personalizar cores por status
status_colors = {
    'pendente': 'FFCCCC',      # Vermelho claro
    'em_transito': 'CCFFCC',   # Verde claro  
    'entregue': 'CCCCFF',      # Azul claro
    'cancelado': 'DDDDDD'      # Cinza claro
}

# Adicionar novos campos
headers = [
    "ID", "Cliente", "Endereço", "Produto", 
    "Valor", "Status", "Entrega", "Observações"  # Nova coluna
]
```

---

## Recursos Adicionais

### Comandos Úteis

```bash
# Verificar se API está rodando
curl -s http://localhost:5000/api/health | python -m json.tool

# Contar entregas por status
curl -s http://localhost:5000/api/stats | python -c "
import sys, json
data = json.load(sys.stdin)
print('Distribuição:', data['data']['distribuicao_status'])
"

# Gerar relatório com timestamp personalizado
python reports/excel_generator.py --filename "relatorio_$(date +%Y%m%d).xlsx"
```

### Integração com Outros Sistemas

```python
# Exemplo: Enviar dados para outro sistema
import requests

def sync_with_external_system():
    """Sincroniza com sistema externo"""
    local_data = requests.get("http://localhost:5000/api/entregas").json()
    
    # Enviar para sistema externo (exemplo)
    # requests.post("https://external-api.com/deliveries", json=local_data)
    
    print(f"Sincronizado {local_data['total']} entregas")
```

---

Estes exemplos demonstram a flexibilidade e potencial do sistema Zeca Delivery para automação de processos reais de delivery!
