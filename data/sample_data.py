"""
Dados de Exemplo para Sistema de Entregas Zeca
=============================================

Este arquivo contém dados mockados para demonstração da API.
Em um sistema real, estes dados viriam de um banco de dados.

Estrutura dos dados:
- id: Identificador único da entrega
- cliente: Nome do cliente
- endereco, bairro, cidade, estado, cep: Endereço completo
- produto: Item a ser entregue
- quantidade: Quantidade do produto
- valor: Valor total da entrega
- telefone: Contato do cliente
- entrega_prevista: Data/hora programada (ISO format)
- status: pendente, em_transito, entregue, cancelado
- prioridade: normal, alta, urgente
"""

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

# Estatísticas dos dados mockados
def get_sample_stats():
    """Retorna estatísticas dos dados de exemplo"""
    total_entregas = len(ENTREGAS_MOCK)
    total_valor = sum(e['valor'] for e in ENTREGAS_MOCK)
    
    status_count = {}
    for entrega in ENTREGAS_MOCK:
        status = entrega['status']
        status_count[status] = status_count.get(status, 0) + 1
    
    entregues = status_count.get('entregue', 0)
    taxa_entrega = (entregues / total_entregas * 100) if total_entregas > 0 else 0
    
    return {
        "total_entregas": total_entregas,
        "valor_total": round(total_valor, 2),
        "taxa_entrega": round(taxa_entrega, 1),
        "distribuicao_status": status_count,
        "valor_medio": round(total_valor / total_entregas, 2) if total_entregas > 0 else 0
    }

if __name__ == "__main__":
    # Demonstração dos dados quando executado diretamente
    print("📊 Dados de Exemplo - Sistema Zeca Delivery")
    print("=" * 50)
    print(f"Total de entregas: {len(ENTREGAS_MOCK)}")
    
    stats = get_sample_stats()
    print(f"Valor total: R$ {stats['valor_total']}")
    print(f"Taxa de entrega: {stats['taxa_entrega']}%")
    print("Distribuição por status:", stats['distribuicao_status'])
    
    print("\n📋 Entregas:")
    for entrega in ENTREGAS_MOCK:
        print(f"  {entrega['id']} - {entrega['cliente']} - {entrega['produto']} - {entrega['status']}")
