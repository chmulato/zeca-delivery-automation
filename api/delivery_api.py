"""
API Flask para Sistema de Entregas Zeca
======================================

API REST que fornece endpoints para gerenciar entregas de delivery.
Desenvolvida como demonstração prática do artigo sobre automação de entregas.

Endpoints disponíveis:
- GET /api/entregas - Lista todas as entregas
- GET /api/entregas/pendentes - Lista entregas pendentes
- GET /api/entregas/status/<status> - Filtra por status
- GET /api/health - Health check da API
- GET /api/stats - Estatísticas das entregas

Autor: Demonstração do artigo Zeca Delivery
"""

from flask import Flask, jsonify
from datetime import datetime
import sys
import os

# Adicionar diretório data ao path para importar dados
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'data'))
from sample_data import ENTREGAS_MOCK

app = Flask(__name__)

def format_response(data, status="success", message=None):
    """Formata resposta padrão da API"""
    response = {
        "status": status,
        "timestamp": datetime.now().isoformat(),
        "data": data
    }
    if message:
        response["message"] = message
    if isinstance(data, list):
        response["total"] = len(data)
    return jsonify(response)

@app.route('/')
def home():
    """Página inicial da API"""
    return jsonify({
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
    })

@app.route('/api/health')
def health_check():
    """Health check da API"""
    return jsonify({
        "status": "healthy",
        "service": "delivery-api",
        "version": "1.0.0",
        "timestamp": datetime.now().isoformat(),
        "uptime": "running",
        "database": "mock_data_ready"
    })

@app.route('/api/entregas', methods=['GET'])
def get_entregas():
    """Retorna todas as entregas"""
    try:
        return format_response(ENTREGAS_MOCK)
    except Exception as e:
        return format_response([], status="error", message=str(e)), 500

@app.route('/api/entregas/pendentes', methods=['GET'])
def get_entregas_pendentes():
    """Retorna apenas entregas pendentes"""
    try:
        pendentes = [e for e in ENTREGAS_MOCK if e['status'] == 'pendente']
        return format_response(pendentes)
    except Exception as e:
        return format_response([], status="error", message=str(e)), 500

@app.route('/api/entregas/status/<status>', methods=['GET'])
def get_entregas_por_status(status):
    """Retorna entregas filtradas por status"""
    try:
        status_validos = ['pendente', 'em_transito', 'entregue', 'cancelado']
        if status not in status_validos:
            return format_response([], status="error", 
                                 message=f"Status inválido. Use: {', '.join(status_validos)}"), 400
        
        entregas_filtradas = [e for e in ENTREGAS_MOCK if e['status'] == status]
        return format_response(entregas_filtradas)
    except Exception as e:
        return format_response([], status="error", message=str(e)), 500

@app.route('/api/stats')
def get_estatisticas():
    """Retorna estatísticas das entregas"""
    try:
        total_entregas = len(ENTREGAS_MOCK)
        total_valor = sum(e['valor'] for e in ENTREGAS_MOCK)
        
        # Contagem por status
        status_count = {}
        for entrega in ENTREGAS_MOCK:
            status = entrega['status']
            status_count[status] = status_count.get(status, 0) + 1
        
        # Taxa de entrega
        entregues = status_count.get('entregue', 0)
        taxa_entrega = (entregues / total_entregas * 100) if total_entregas > 0 else 0
        
        estatisticas = {
            "total_entregas": total_entregas,
            "valor_total": round(total_valor, 2),
            "taxa_entrega": round(taxa_entrega, 1),
            "distribuicao_status": status_count,
            "valor_medio": round(total_valor / total_entregas, 2) if total_entregas > 0 else 0
        }
        
        return format_response(estatisticas)
    except Exception as e:
        return format_response({}, status="error", message=str(e)), 500

@app.errorhandler(404)
def not_found(error):
    """Handler para rotas não encontradas"""
    return format_response({}, status="error", message="Endpoint não encontrado"), 404

@app.errorhandler(500)
def internal_error(error):
    """Handler para erros internos"""
    return format_response({}, status="error", message="Erro interno do servidor"), 500

if __name__ == '__main__':
    print("🚀 Iniciando API de Entregas Zeca...")
    print("=" * 50)
    print("📍 Endpoints disponíveis:")
    print("   GET /api/entregas - Todas as entregas")
    print("   GET /api/entregas/pendentes - Entregas pendentes")
    print("   GET /api/entregas/status/<status> - Entregas por status")
    print("   GET /api/health - Health check")
    print("   GET /api/stats - Estatísticas")
    print("=" * 50)
    print("🌐 API rodando em: http://localhost:5000")
    print("📖 Documentação: Veja README.md")
    print("=" * 50)
    
    app.run(debug=True, host='0.0.0.0', port=5000)
