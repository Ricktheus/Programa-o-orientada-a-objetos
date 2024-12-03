import requests

BASE_URL = "http://127.0.0.1:5000/api"

def test_clientes():
    print("\n=== Testando Endpoints de Clientes ===")
    
    # POST: Criar Cliente
    cliente_data = {
        "nome": "João Silva",
        "endereco": "Rua 1, Bairro Centro",
        "email": "joao.silva@email.com",
        "telefone": "123456789",
        "segmento": "Varejo",
        "status": "Ativo"
    }
    response = requests.post(f"{BASE_URL}/clientes", json=cliente_data)
    print("POST /clientes:", response.json())
    
    # GET: Obter Todos os Clientes
    response = requests.get(f"{BASE_URL}/clientes")
    print("GET /clientes:", response.json())
    
    # PUT: Atualizar Cliente
    update_data = {"nome": "João Atualizado"}
    response = requests.put(f"{BASE_URL}/clientes/1", json=update_data)
    print("PUT /clientes/1:", response.json())
    
    # DELETE: Deletar Cliente
    response = requests.delete(f"{BASE_URL}/clientes/1")
    print("DELETE /clientes/1:", response.json())


def test_projetos():
    print("\n=== Testando Endpoints de Projetos ===")
    
    # POST: Criar Projeto
    projeto_data = {
        "nome": "Projeto X",
        "escopo": "Desenvolvimento de sistema",
        "prazo": "2024-12-31",
        "gerente": "Alice",
        "desenvolvedor": "Bob",
        "designer": "Carol"
    }
    response = requests.post(f"{BASE_URL}/projetos", json=projeto_data)
    print("POST /projetos:", response.json())
    
    # GET: Obter Todos os Projetos
    response = requests.get(f"{BASE_URL}/projetos")
    print("GET /projetos:", response.json())
    
    # PUT: Atualizar Projeto
    update_data = {"nome": "Projeto Atualizado"}
    response = requests.put(f"{BASE_URL}/projetos/1", json=update_data)
    print("PUT /projetos/1:", response.json())
    
    # DELETE: Deletar Projeto
    response = requests.delete(f"{BASE_URL}/projetos/1")
    print("DELETE /projetos/1:", response.json())


def test_softwares():
    print("\n=== Testando Endpoints de Softwares ===")
    
    # POST: Criar Software
    software_data = {
        "projeto": "Sistema A",
        "funcionalidade": "Gestão",
        "cliente": "Empresa X",
        "versao": "1.0"
    }
    response = requests.post(f"{BASE_URL}/softwares", json=software_data)
    print("POST /softwares:", response.json())
    
    # GET: Obter Todos os Softwares
    response = requests.get(f"{BASE_URL}/softwares")
    print("GET /softwares:", response.json())
    
    # PUT: Atualizar Software
    update_data = {"funcionalidade": "Gestão Avançada"}
    response = requests.put(f"{BASE_URL}/softwares/1", json=update_data)
    print("PUT /softwares/1:", response.json())
    
    # DELETE: Deletar Software
    response = requests.delete(f"{BASE_URL}/softwares/1")
    print("DELETE /softwares/1:", response.json())


def test_recursos():
    print("\n=== Testando Endpoints de Recursos ===")
    
    # POST: Criar Recurso
    recurso_data = {
        "nome": "Servidor",
        "tipo": "Hardware",
        "quantidade": 2
    }
    response = requests.post(f"{BASE_URL}/recursos", json=recurso_data)
    print("POST /recursos:", response.json())
    
    # GET: Obter Todos os Recursos
    response = requests.get(f"{BASE_URL}/recursos")
    print("GET /recursos:", response.json())
    
    # PUT: Atualizar Recurso
    update_data = {"quantidade": 5}
    response = requests.put(f"{BASE_URL}/recursos/1", json=update_data)
    print("PUT /recursos/1:", response.json())
    
    # DELETE: Deletar Recurso
    response = requests.delete(f"{BASE_URL}/recursos/1")
    print("DELETE /recursos/1:", response.json())


def test_parceiros():
    print("\n=== Testando Endpoints de Parceiros ===")
    
    # POST: Criar Parceiro
    parceiro_data = {
        "nome": "Empresa Z",
        "endereco": "Rua Parceiro 1",
        "telefone": "987654321",
        "email": "parceiro@email.com",
        "tipo_de_parceiro": "Fornecedor"
    }
    response = requests.post(f"{BASE_URL}/parceiros", json=parceiro_data)
    print("POST /parceiros:", response.json())
    
    # GET: Obter Todos os Parceiros
    response = requests.get(f"{BASE_URL}/parceiros")
    print("GET /parceiros:", response.json())
    
    # PUT: Atualizar Parceiro
    update_data = {"nome": "Empresa Z Atualizada"}
    response = requests.put(f"{BASE_URL}/parceiros/1", json=update_data)
    print("PUT /parceiros/1:", response.json())
    
    # DELETE: Deletar Parceiro
    response = requests.delete(f"{BASE_URL}/parceiros/1")
    print("DELETE /parceiros/1:", response.json())

def test_contas_projeto():
    print("\n=== Testando Endpoints de Contas do Projeto ===")
    conta_projeto_data = {
        "nome": "Conta do Projeto X",
        "valor": 1500.00,
        "vencimento": "2024-12-31",
        "status": "Pendente"
    }
    response = requests.post(f"{BASE_URL}/contas-projetos", json=conta_projeto_data)
    print("POST /contas-projetos:", response.json())
    
    response = requests.get(f"{BASE_URL}/contas-projetos")
    print("GET /contas-projetos:", response.json())
    
    update_data = {"status": "Pago"}
    response = requests.put(f"{BASE_URL}/contas-projetos/1", json=update_data)
    print("PUT /contas-projetos/1:", response.json())
    
    response = requests.delete(f"{BASE_URL}/contas-projetos/1")
    print("DELETE /contas-projetos/1:", response.json())

def test_contratos():
    print("\n=== Testando Endpoints de Contratos ===")
    contrato_data = {
        "cliente": "Empresa X",
        "tipo_plano": "Premium",
        "status": "Ativo",
        "valor": 5000.00
    }
    response = requests.post(f"{BASE_URL}/contratos", json=contrato_data)
    print("POST /contratos:", response.json())
    
    response = requests.get(f"{BASE_URL}/contratos")
    print("GET /contratos:", response.json())
    
    update_data = {"status": "Cancelado"}
    response = requests.put(f"{BASE_URL}/contratos/1", json=update_data)
    print("PUT /contratos/1:", response.json())
    
    response = requests.delete(f"{BASE_URL}/contratos/1")
    print("DELETE /contratos/1:", response.json())

def test_colaboradores():
    print("\n=== Testando Endpoints de Colaboradores ===")
    colaborador_data = {
        "nome": "Maria Santos",
        "endereco": "Rua 5, Bairro Sul",
        "salario": 3500.00,
        "cargo": "Analista",
        "telefone": "987654321",
        "email": "maria.santos@email.com"
    }
    response = requests.post(f"{BASE_URL}/colaboradores", json=colaborador_data)
    print("POST /colaboradores:", response.json())
    
    response = requests.get(f"{BASE_URL}/colaboradores")
    print("GET /colaboradores:", response.json())
    
    update_data = {"salario": 4000.00}
    response = requests.put(f"{BASE_URL}/colaboradores/1", json=update_data)
    print("PUT /colaboradores/1:", response.json())
    
    response = requests.delete(f"{BASE_URL}/colaboradores/1")
    print("DELETE /colaboradores/1:", response.json())

def test_contas():
    print("\n=== Testando Endpoints de Contas ===")
    conta_data = {
        "nome": "Conta de Luz",
        "valor": 200.00,
        "vencimento": "2024-12-15",
        "status": "Aberto"
    }
    response = requests.post(f"{BASE_URL}/contas", json=conta_data)
    print("POST /contas:", response.json())
    
    response = requests.get(f"{BASE_URL}/contas")
    print("GET /contas:", response.json())
    
    update_data = {"status": "Pago"}
    response = requests.put(f"{BASE_URL}/contas/1", json=update_data)
    print("PUT /contas/1:", response.json())
    
    response = requests.delete(f"{BASE_URL}/contas/1")
    print("DELETE /contas/1:", response.json())

# Chamando as funções de teste
if __name__ == "__main__":
    test_clientes()
    test_projetos()
    test_softwares()
    test_recursos()
    test_parceiros()
    test_contas_projeto()
    test_contratos()
    test_colaboradores()
    test_contas()