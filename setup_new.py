#!/usr/bin/env python3
"""
Setup Script - Sistema Zeca Delivery  
===================================

Script de configuração automatizada que:
- Verifica compatibilidade do Python
- Instala dependências necessárias  
- Cria estrutura de diretórios
- Valida instalação dos componentes

Uso: python setup.py
"""

import sys
import subprocess
import os
from pathlib import Path

# Configurações
PYTHON_MIN_VERSION = (3, 8)
REQUIRED_PACKAGES = [
    "Flask==2.3.3",
    "openpyxl==3.1.2", 
    "requests==2.31.0"
]

def print_header():
    """Exibe cabeçalho do setup"""
    print("🎯 Setup - Sistema Zeca Delivery")
    print("=" * 50)

def check_python_version():
    """Verifica se a versão do Python é compatível"""
    print("🐍 Verificando versão do Python...")
    
    current_version = sys.version_info[:2]
    
    if current_version >= PYTHON_MIN_VERSION:
        print(f"✅ Python {'.'.join(map(str, current_version))} - Compatível")
        return True
    else:
        print(f"❌ Python {'.'.join(map(str, current_version))} - Incompatível")
        print(f"💡 Versão mínima requerida: Python {'.'.join(map(str, PYTHON_MIN_VERSION))}")
        print("🔗 Download em: https://python.org")
        return False

def create_directory_structure():
    """Cria estrutura de diretórios necessária"""
    print("📁 Criando estrutura de diretórios...")
    
    directories = [
        "logs",
        "output", 
        "temp"
    ]
    
    for directory in directories:
        dir_path = Path(directory)
        try:
            dir_path.mkdir(exist_ok=True)
            print(f"   ✅ Diretório criado: {directory}")
        except Exception as e:
            print(f"   ❌ Erro ao criar {directory}: {e}")
            return False
    
    return True

def install_dependencies():
    """Instala dependências Python"""
    print("📦 Instalando dependências...")
    
    try:
        # Verificar se pip está disponível
        subprocess.run([sys.executable, "-m", "pip", "--version"], 
                      check=True, capture_output=True)
    except subprocess.CalledProcessError:
        print("❌ pip não encontrado!")
        print("💡 Instale o pip ou use uma instalação Python completa")
        return False
    
    # Instalar pacotes
    for package in REQUIRED_PACKAGES:
        try:
            print(f"   Instalando {package}...")
            result = subprocess.run(
                [sys.executable, "-m", "pip", "install", package],
                check=True,
                capture_output=True,
                text=True
            )
            print(f"   ✅ {package} instalado")
        except subprocess.CalledProcessError as e:
            print(f"   ❌ Erro ao instalar {package}")
            print(f"   💬 Erro: {e.stderr}")
            return False
    
    return True

def verify_installation():
    """Verifica se os módulos foram instalados corretamente"""
    print("🔍 Verificando instalação...")
    
    modules_to_test = [
        ("flask", "Flask"),
        ("openpyxl", "openpyxl"),
        ("requests", "requests")
    ]
    
    for module_name, import_name in modules_to_test:
        try:
            __import__(import_name.lower())
            print(f"   ✅ {module_name} - OK")
        except ImportError:
            print(f"   ❌ {module_name} - Falha na importação")
            return False
    
    return True

def check_project_structure():
    """Verifica se a estrutura do projeto está correta"""
    print("📋 Verificando estrutura do projeto...")
    
    required_files = [
        "api/delivery_api.py",
        "reports/excel_generator.py", 
        "data/sample_data.py",
        "requirements.txt"
    ]
    
    missing_files = []
    for file_path in required_files:
        if not Path(file_path).exists():
            missing_files.append(file_path)
        else:
            print(f"   ✅ {file_path}")
    
    if missing_files:
        print("   ❌ Arquivos não encontrados:")
        for file in missing_files:
            print(f"      • {file}")
        return False
    
    return True

def show_usage_instructions():
    """Mostra instruções de uso"""
    print("=" * 50)
    print("🚀 SISTEMA ZECA DELIVERY - CONFIGURADO!")
    print("=" * 50)
    print("📋 Como usar:")
    print()
    print("1. 🔗 Iniciar a API:")
    print("   python api/delivery_api.py")
    print()
    print("2. 📊 Gerar relatório (em outro terminal):")
    print("   python reports/excel_generator.py")
    print()
    print("3. 🧪 Executar testes:")
    print("   python tests/test_api.py")
    print()
    print("🔗 Endpoints da API:")
    print("   GET /api/entregas - Todas as entregas")
    print("   GET /api/entregas/pendentes - Entregas pendentes")
    print("   GET /api/health - Status da API")
    print("   GET /api/stats - Estatísticas")
    print()
    print("📊 Saída:")
    print("   Arquivo Excel formatado com relatório das entregas")
    print()
    print("📖 Documentação:")
    print("   docs/API.md - Documentação da API")
    print("   docs/EXAMPLES.md - Exemplos de uso")
    print("=" * 50)

def main():
    """Função principal do setup"""
    print_header()
    
    # Verificações e configurações
    checks = [
        ("Verificar Python", check_python_version),
        ("Criar diretórios", create_directory_structure),
        ("Instalar dependências", install_dependencies),
        ("Verificar instalação", verify_installation),
        ("Verificar projeto", check_project_structure)
    ]
    
    for check_name, check_func in checks:
        if not check_func():
            print(f"\n❌ Falha em: {check_name}")
            print("🔧 Corrija os erros e execute novamente: python setup.py")
            return False
    
    print("\n✅ Setup concluído com sucesso!")
    show_usage_instructions()
    return True

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n⏹️ Setup interrompido pelo usuário")
        sys.exit(1)
    except Exception as e:
        print(f"\n💥 Erro inesperado: {e}")
        sys.exit(1)
