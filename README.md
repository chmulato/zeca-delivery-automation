# 🚀 Zeca Delivery Automation

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.3.3-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-black.svg)](https://github.com/chmulato/zeca-delivery-automation)

> **Sistema de automação de entregas baseado no artigo "Como o Python Automatizou a Logística de Entregas: Case Real"**

Este repositório contém o **código funcional** que demonstra como transformar um processo manual caótico de delivery em um sistema automatizado e profissional.

🔗 **[Ver artigo completo no LinkedIn](#)** | 📖 **[Documentação da API](docs/API.md)**

## 📋 O Problema que Resolvemos

**ANTES:**
- 📄 Papéis desorganizados espalhados
- 📱 Pedidos confusos vindos do WhatsApp  
- ⏰ 30 minutos diários organizando manualmente
- ❌ Erros constantes de digitação
- 😤 Stress operacional desnecessário

**DEPOIS:**
- 🔄 Sistema automatizado com um clique
- 📊 Relatório Excel profissional gerado automaticamente
- ⚡ Processo reduzido para 2 minutos
- ✅ Zero erros de transcrição
- 📈 Visibilidade completa das operações

## ⚡ Quick Start

### 1. Clonar o repositório
```bash
git clone https://github.com/seu-usuario/zeca-delivery-automation.git
cd zeca-delivery-automation
```

### 2. Configurar ambiente
```bash
### 2. Execute o setup automatizado
```bash
python setup.py
```

### 3. Inicie a API (Terminal 1)
```bash
python api/delivery_api.py
```
*API disponível em: http://localhost:5000*

### 4. Gere o relatório (Terminal 2)  
```bash
python reports/excel_generator.py
```

**Pronto!** Arquivo Excel gerado automaticamente com formatação profissional.

## 🏗️ Arquitetura do Sistema

```
┌─────────────────┐    HTTP     ┌──────────────────┐    Excel    ┌─────────────────┐
│                 │    GET      │                  │   Export    │                 │
│  Delivery API   │◄────────────│  Report Generator│────────────►│   Excel Report  │
│   (Flask)       │             │    (openpyxl)    │             │   (Formatted)   │
│                 │             │                  │             │                 │
└─────────────────┘             └──────────────────┘             └─────────────────┘
       │                                 │                               │
       ▼                                 ▼                               ▼
📊 Sample Data                   🔍 API Verification                📈 Visual Dashboard
   5 Entregas                    Health Check                     Cores por Status
```

### 📁 Estrutura de Pastas:
```
api/             # 🔗 Endpoints Flask
reports/         # 📊 Geração de Excel  
data/            # 📋 Dados mockados
docs/            # 📖 Documentação
tests/           # 🧪 Testes unitários
```

## 📡 Endpoints da API

| Endpoint | Método | Descrição |
|----------|--------|-----------|
| `/api/entregas` | GET | Lista todas as entregas |
| `/api/entregas/pendentes` | GET | Apenas entregas pendentes |
| `/api/entregas/status/<status>` | GET | Filtra por status específico |
| `/api/health` | GET | Health check da API |
| `/api/stats` | GET | Estatísticas consolidadas |

### Exemplo de Resposta:
```json
{
  "status": "success",
  "total": 5,
  "timestamp": "2025-08-04T19:30:00",
  "data": [
    {
      "id": 101,
      "cliente": "João Silva",
      "endereco": "Rua das Flores, 123",
      "bairro": "Centro",
      "cidade": "São Paulo",
      "produto": "Pizza Calabresa",
      "valor": 45.90,
      "status": "pendente",
      "entrega_prevista": "2025-08-04T19:30:00"
    }
  ]
}
```

## 📊 Dados de Demonstração

O sistema inclui 5 entregas mockadas representando um dia típico:

| Cliente | Produto | Valor | Status | Bairro |
|---------|---------|-------|--------|--------|
| João Silva | Pizza Calabresa | R$ 45,90 | 🟡 Pendente | Centro |
| Maria Santos | Pizza Margherita | R$ 35,50 | 🔵 Em trânsito | Bela Vista |
| Carlos Oliveira | Pizza Portuguesa | R$ 89,70 | 🟡 Pendente | Consolação |
| Ana Costa | Pizza Quatro Queijos | R$ 42,00 | 🟢 Entregue | Jardins |
| Pedro Ferreira | Pizza Pepperoni | R$ 67,80 | 🟡 Pendente | Centro |

**Estatísticas:**
- 📊 Total: 5 entregas
- 💰 Faturamento: R$ 280,90
- 📈 Taxa de entrega: 20%

## 🎨 Relatório Excel Gerado

### Aba "Entregas do Dia"
- ✅ Formatação profissional com cabeçalhos azuis
- ✅ Cores condicionais por status:
  - 🟡 **Pendente:** Fundo bege claro
  - 🔵 **Em trânsito:** Fundo azul claro
  - 🟢 **Entregue:** Fundo verde claro
- ✅ Colunas ajustadas automaticamente
- ✅ Endereços completos formatados

### Aba "Estatísticas"
- 📊 Total de entregas por status
- 💰 Valor total do faturamento
- 📈 Taxa de entrega calculada
- 📋 Distribuição percentual

## 🛠️ Tecnologias

- **Backend:** Flask (API REST)
- **Dados:** JSON mockado
- **Excel:** openpyxl (formatação profissional)
- **HTTP:** requests (consumo de API)
- **Setup:** Python 3.8+ automation

## 📁 Estrutura do Projeto

```
zeca-delivery-automation/
├── 📄 delivery_api.py           # API Flask com endpoints
├── 📊 generate_delivery_report.py # Gerador Excel
├── ⚙️ setup.py                  # Configuração automatizada
├── 📋 requirements.txt          # Dependências
├── 📖 README.md                 # Este arquivo
├── 📁 data/                     # Dados (auto-criado)
├── 📁 logs/                     # Logs (auto-criado)
└── 📁 reports/                  # Relatórios (auto-criado)
```

## 🔧 Dependências

```txt
Flask==2.3.3
openpyxl==3.1.2  
requests==2.31.0
python-dotenv==1.0.0
```

## 📈 Resultados Comprovados

### Métricas de Impacto:
- ⏱️ **Tempo:** 30min → 2min (93% redução)
- ✅ **Precisão:** 100% (zero erros de digitação)
- 📊 **Visibilidade:** Dashboard visual completo
- 🔄 **Escalabilidade:** Suporta centenas de entregas
- 💼 **Profissionalismo:** Relatórios corporativos

### Antes vs Depois:
| Aspecto | Manual | Automatizado |
|---------|--------|--------------|
| Tempo prep. | 30 minutos | 2 minutos |
| Erros | Frequentes | Zero |
| Formatação | Inconsistente | Profissional |
| Escalabilidade | Limitada | Ilimitada |
| Stress | Alto | Eliminado |

## 🚀 Expansões Possíveis

Este projeto serve como base para funcionalidades avançadas:

- 🗺️ **Otimização de rotas** com Google Maps API
- 📱 **App móvel** para entregadores
- 📧 **Envio automático** de relatórios
- 🔔 **Notificações** push em tempo real
- 📊 **Dashboard web** interativo
- 🔄 **Integração** com sistemas reais

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## 📝 Licença

MIT License - veja [LICENSE](LICENSE) para detalhes.

## 📞 Contato

- **Artigo original:** [LinkedIn](seu-perfil-linkedin)
- **Dúvidas:** Abra uma [issue](issues)
- **Consultoria:** Entre em contato para soluções personalizadas

---

## 💡 Sobre o Artigo

Este código demonstra na prática os conceitos apresentados no artigo **"Como o Python Automatizou a Logística de Entregas: Case Real"**.

**A transformação do Zeca é real e replicável!** 🚀

---

**⭐ Se este projeto te ajudou, deixe uma estrela no repositório!**
