# API de Entregas - Endpoint Flask
# Arquivo: delivery_api.py

from flask import Flask, jsonify
from datetime import datetime, timedelta
import json

app = Flask(__name__)

# Dados simulados de entregas (normalmente viria de um banco de dados)
ENTREGAS_MOCK = [
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
    },
    {
        "id": 102,
        "cliente": "Maria Santos",
        "endereco": "Av. Paulista, 1000",
        "bairro": "Bela Vista",
        "cidade": "São Paulo", 
        "estado": "SP",
        "cep": "01310-100",
        "produto": "Pizza Margherita",
        "quantidade": 1,
        "valor": 35.50,
        "telefone": "(11) 99876-5432",
        "entrega_prevista": "2025-08-04T20:00:00",
        "status": "em_transito",
        "prioridade": "alta"
    },
    {
        "id": 103,
        "cliente": "Carlos Oliveira",
        "endereco": "Rua Augusta, 456",
        "bairro": "Consolação",
        "cidade": "São Paulo",
        "estado": "SP", 
        "cep": "01305-000",
        "produto": "Pizza Portuguesa",
        "quantidade": 3,
        "valor": 89.70,
        "telefone": "(11) 97654-3210",
        "entrega_prevista": "2025-08-04T20:15:00",
        "status": "pendente",
        "prioridade": "normal"
    },
    {
        "id": 104,
        "cliente": "Ana Costa", 
        "endereco": "Rua Oscar Freire, 789",
        "bairro": "Jardins",
        "cidade": "São Paulo",
        "estado": "SP",
        "cep": "01426-001",
        "produto": "Pizza Quatro Queijos",
        "quantidade": 1,
        "valor": 42.00,
        "telefone": "(11) 96543-2109",
        "entrega_prevista": "2025-08-04T20:45:00",
        "status": "entregue",
        "prioridade": "normal"
    },
    {
        "id": 105,
        "cliente": "Pedro Ferreira",
        "endereco": "Rua da Consolação, 234",
        "bairro": "Centro",
        "cidade": "São Paulo",
        "estado": "SP",
        "cep": "01302-000", 
        "produto": "Pizza Pepperoni",
        "quantidade": 2,
        "valor": 67.80,
        "telefone": "(11) 95432-1098",
        "entrega_prevista": "2025-08-04T21:00:00",
        "status": "pendente",
        "prioridade": "alta"
    }
]

@app.route('/api/entregas', methods=['GET'])
def listar_entregas():
    """
    Endpoint que retorna todas as entregas do dia
    """
    try:
        return jsonify({
            "status": "success",
            "total": len(ENTREGAS_MOCK),
            "data": ENTREGAS_MOCK,
            "timestamp": datetime.now().isoformat()
        }), 200
    except Exception as e:
        return jsonify({
            "status": "error", 
            "message": str(e),
            "timestamp": datetime.now().isoformat()
        }), 500

@app.route('/api/entregas/pendentes', methods=['GET'])
def listar_entregas_pendentes():
    """
    Endpoint que retorna apenas entregas pendentes
    """
    try:
        pendentes = [e for e in ENTREGAS_MOCK if e['status'] == 'pendente']
        return jsonify({
            "status": "success",
            "total": len(pendentes),
            "data": pendentes,
            "timestamp": datetime.now().isoformat()
        }), 200
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e),
            "timestamp": datetime.now().isoformat()
        }), 500

@app.route('/api/entregas/status/<status>', methods=['GET'])
def listar_por_status(status):
    """
    Endpoint que retorna entregas filtradas por status
    """
    try:
        filtradas = [e for e in ENTREGAS_MOCK if e['status'] == status]
        return jsonify({
            "status": "success",
            "filtro": status,
            "total": len(filtradas),
            "data": filtradas,
            "timestamp": datetime.now().isoformat()
        }), 200
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e),
            "timestamp": datetime.now().isoformat()
        }), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """
    Endpoint de health check
    """
    return jsonify({
        "status": "healthy",
        "service": "delivery-api",
        "version": "1.0.0",
        "timestamp": datetime.now().isoformat()
    }), 200

@app.route('/api/stats', methods=['GET'])
def estatisticas():
    """
    Endpoint que retorna estatísticas das entregas
    """
    try:
        total = len(ENTREGAS_MOCK)
        pendentes = len([e for e in ENTREGAS_MOCK if e['status'] == 'pendente'])
        em_transito = len([e for e in ENTREGAS_MOCK if e['status'] == 'em_transito'])
        entregues = len([e for e in ENTREGAS_MOCK if e['status'] == 'entregue'])
        valor_total = sum(e['valor'] for e in ENTREGAS_MOCK)
        
        return jsonify({
            "status": "success",
            "stats": {
                "total_entregas": total,
                "pendentes": pendentes,
                "em_transito": em_transito,
                "entregues": entregues,
                "valor_total": valor_total,
                "taxa_entrega": round((entregues / total) * 100, 1) if total > 0 else 0
            },
            "timestamp": datetime.now().isoformat()
        }), 200
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e),
            "timestamp": datetime.now().isoformat()
        }), 500

if __name__ == '__main__':
    print("🚀 Iniciando API de Entregas...")
    print("📍 Endpoints disponíveis:")
    print("   GET /api/entregas - Todas as entregas")
    print("   GET /api/entregas/pendentes - Entregas pendentes")
    print("   GET /api/entregas/status/<status> - Entregas por status")
    print("   GET /api/health - Health check")
    print("   GET /api/stats - Estatísticas")
    print("🌐 API rodando em: http://localhost:5000")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
