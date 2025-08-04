"""
Testes Unitários - Sistema Zeca Delivery
=======================================

Testes para validar o funcionamento da API e componentes do sistema.

Para executar:
    python -m pytest tests/
    ou
    python tests/test_api.py
"""

import unittest
import requests
import json
import sys
import os

# Adicionar diretórios ao path para importar módulos
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'data'))

from data.sample_data import ENTREGAS_MOCK, get_sample_stats

class TestZecaDeliveryAPI(unittest.TestCase):
    """Testes para a API de entregas"""
    
    @classmethod
    def setUpClass(cls):
        """Configuração inicial dos testes"""
        cls.base_url = "http://localhost:5000"
        cls.timeout = 5
        
        # Verificar se API está rodando
        try:
            response = requests.get(f"{cls.base_url}/api/health", timeout=cls.timeout)
            if response.status_code != 200:
                raise Exception("API não está respondendo")
        except Exception as e:
            print(f"\n❌ ERRO: API não está rodando em {cls.base_url}")
            print("💡 Para executar os testes:")
            print("   1. Abra um terminal: python api/delivery_api.py")
            print("   2. Em outro terminal: python tests/test_api.py")
            raise unittest.SkipTest(f"API não disponível: {e}")
    
    def test_health_check(self):
        """Testa o health check da API"""
        response = requests.get(f"{self.base_url}/api/health", timeout=self.timeout)
        
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        self.assertEqual(data['status'], 'healthy')
        self.assertEqual(data['service'], 'delivery-api')
        self.assertIn('timestamp', data)
        self.assertIn('version', data)
    
    def test_get_all_deliveries(self):
        """Testa busca de todas as entregas"""
        response = requests.get(f"{self.base_url}/api/entregas", timeout=self.timeout)
        
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        self.assertEqual(data['status'], 'success')
        self.assertIn('total', data)
        self.assertIn('data', data)
        self.assertIsInstance(data['data'], list)
        
        # Verificar estrutura de uma entrega
        if data['data']:
            entrega = data['data'][0]
            required_fields = ['id', 'cliente', 'endereco', 'produto', 'valor', 'status']
            for field in required_fields:
                self.assertIn(field, entrega)
    
    def test_get_pending_deliveries(self):
        """Testa busca de entregas pendentes"""
        response = requests.get(f"{self.base_url}/api/entregas/pendentes", timeout=self.timeout)
        
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        self.assertEqual(data['status'], 'success')
        
        # Verificar se todas as entregas retornadas são pendentes
        for entrega in data['data']:
            self.assertEqual(entrega['status'], 'pendente')
    
    def test_get_deliveries_by_status(self):
        """Testa busca por status específico"""
        statuses = ['pendente', 'em_transito', 'entregue']
        
        for status in statuses:
            with self.subTest(status=status):
                response = requests.get(f"{self.base_url}/api/entregas/status/{status}", timeout=self.timeout)
                
                self.assertEqual(response.status_code, 200)
                
                data = response.json()
                self.assertEqual(data['status'], 'success')
                
                # Verificar se todas as entregas têm o status correto
                for entrega in data['data']:
                    self.assertEqual(entrega['status'], status)
    
    def test_invalid_status(self):
        """Testa status inválido"""
        response = requests.get(f"{self.base_url}/api/entregas/status/invalido", timeout=self.timeout)
        
        self.assertEqual(response.status_code, 400)
        
        data = response.json()
        self.assertEqual(data['status'], 'error')
        self.assertIn('Status inválido', data['message'])
    
    def test_get_statistics(self):
        """Testa endpoint de estatísticas"""
        response = requests.get(f"{self.base_url}/api/stats", timeout=self.timeout)
        
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        self.assertEqual(data['status'], 'success')
        
        stats = data['data']
        required_stats = ['total_entregas', 'valor_total', 'taxa_entrega', 'distribuicao_status']
        for stat in required_stats:
            self.assertIn(stat, stats)
        
        # Verificar tipos de dados
        self.assertIsInstance(stats['total_entregas'], int)
        self.assertIsInstance(stats['valor_total'], (int, float))
        self.assertIsInstance(stats['taxa_entrega'], (int, float))
        self.assertIsInstance(stats['distribuicao_status'], dict)
    
    def test_not_found_endpoint(self):
        """Testa endpoint não existente"""
        response = requests.get(f"{self.base_url}/api/inexistente", timeout=self.timeout)
        
        self.assertEqual(response.status_code, 404)
        
        data = response.json()
        self.assertEqual(data['status'], 'error')
        self.assertIn('não encontrado', data['message'].lower())
    
    def test_response_format(self):
        """Testa formato padrão das respostas"""
        endpoints = [
            '/api/entregas',
            '/api/entregas/pendentes', 
            '/api/stats'
        ]
        
        for endpoint in endpoints:
            with self.subTest(endpoint=endpoint):
                response = requests.get(f"{self.base_url}{endpoint}", timeout=self.timeout)
                
                self.assertEqual(response.status_code, 200)
                
                data = response.json()
                # Verificar campos obrigatórios na resposta
                self.assertIn('status', data)
                self.assertIn('timestamp', data)
                self.assertIn('data', data)
                
                # Verificar formato do timestamp
                self.assertRegex(data['timestamp'], r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}')


class TestSampleData(unittest.TestCase):
    """Testes para os dados de exemplo"""
    
    def test_mock_data_structure(self):
        """Testa estrutura dos dados mockados"""
        self.assertIsInstance(ENTREGAS_MOCK, list)
        self.assertGreater(len(ENTREGAS_MOCK), 0)
        
        # Verificar estrutura de cada entrega
        required_fields = [
            'id', 'cliente', 'endereco', 'bairro', 'cidade', 'estado', 'cep',
            'produto', 'quantidade', 'valor', 'telefone', 'entrega_prevista',
            'status', 'prioridade'
        ]
        
        for entrega in ENTREGAS_MOCK:
            for field in required_fields:
                self.assertIn(field, entrega, f"Campo {field} não encontrado na entrega {entrega['id']}")
    
    def test_mock_data_values(self):
        """Testa valores dos dados mockados"""
        for entrega in ENTREGAS_MOCK:
            # ID deve ser número positivo
            self.assertIsInstance(entrega['id'], int)
            self.assertGreater(entrega['id'], 0)
            
            # Valor deve ser positivo
            self.assertIsInstance(entrega['valor'], (int, float))
            self.assertGreater(entrega['valor'], 0)
            
            # Quantidade deve ser positiva
            self.assertIsInstance(entrega['quantidade'], int)
            self.assertGreater(entrega['quantidade'], 0)
            
            # Status deve ser válido
            valid_statuses = ['pendente', 'em_transito', 'entregue', 'cancelado']
            self.assertIn(entrega['status'], valid_statuses)
            
            # CEP deve ter formato brasileiro
            self.assertRegex(entrega['cep'], r'\d{5}-\d{3}')
    
    def test_sample_statistics(self):
        """Testa função de estatísticas dos dados"""
        stats = get_sample_stats()
        
        # Verificar campos obrigatórios
        required_fields = ['total_entregas', 'valor_total', 'taxa_entrega', 'distribuicao_status']
        for field in required_fields:
            self.assertIn(field, stats)
        
        # Verificar consistência
        self.assertEqual(stats['total_entregas'], len(ENTREGAS_MOCK))
        
        # Taxa de entrega deve estar entre 0 e 100
        self.assertGreaterEqual(stats['taxa_entrega'], 0)
        self.assertLessEqual(stats['taxa_entrega'], 100)
        
        # Valor total deve ser positivo
        self.assertGreater(stats['valor_total'], 0)


class TestSystemIntegration(unittest.TestCase):
    """Testes de integração do sistema"""
    
    def setUp(self):
        """Configuração para cada teste"""
        self.base_url = "http://localhost:5000"
        self.timeout = 10
    
    def test_api_data_consistency(self):
        """Testa consistência entre API e dados mockados"""
        # Buscar dados da API
        response = requests.get(f"{self.base_url}/api/entregas", timeout=self.timeout)
        self.assertEqual(response.status_code, 200)
        
        api_data = response.json()['data']
        
        # Comparar com dados mockados
        self.assertEqual(len(api_data), len(ENTREGAS_MOCK))
        
        # Verificar se IDs são consistentes
        api_ids = {entrega['id'] for entrega in api_data}
        mock_ids = {entrega['id'] for entrega in ENTREGAS_MOCK}
        self.assertEqual(api_ids, mock_ids)
    
    def test_statistics_calculation(self):
        """Testa se estatísticas da API batem com cálculo local"""
        # Estatísticas da API
        response = requests.get(f"{self.base_url}/api/stats", timeout=self.timeout)
        self.assertEqual(response.status_code, 200)
        
        api_stats = response.json()['data']
        
        # Estatísticas locais
        local_stats = get_sample_stats()
        
        # Comparar valores
        self.assertEqual(api_stats['total_entregas'], local_stats['total_entregas'])
        self.assertAlmostEqual(api_stats['valor_total'], local_stats['valor_total'], places=2)
        self.assertAlmostEqual(api_stats['taxa_entrega'], local_stats['taxa_entrega'], places=1)


def run_tests():
    """Executa todos os testes com relatório"""
    print("🧪 EXECUTANDO TESTES DO SISTEMA ZECA DELIVERY")
    print("=" * 60)
    
    # Configurar runner de testes
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Adicionar classes de teste
    test_classes = [TestZecaDeliveryAPI, TestSampleData, TestSystemIntegration]
    for test_class in test_classes:
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    
    # Executar testes
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Resumo
    print("\n" + "=" * 60)
    print("📊 RESUMO DOS TESTES:")
    print(f"✅ Sucessos: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"❌ Falhas: {len(result.failures)}")
    print(f"💥 Erros: {len(result.errors)}")
    print(f"⏭️ Ignorados: {len(result.skipped)}")
    
    if result.wasSuccessful():
        print("\n🎉 TODOS OS TESTES PASSARAM!")
        return True
    else:
        print("\n🔧 ALGUNS TESTES FALHARAM!")
        return False


if __name__ == "__main__":
    success = run_tests()
    exit(0 if success else 1)
