from flask import Blueprint, render_template, request, jsonify
import logging
logging.basicConfig(level=logging.DEBUG)
routes = Blueprint('routes', __name__)

# === Listas Globais para Armazenamento ===
softwares = []
clientes = []
projetos = []
recursos = []
contas_projeto = []
parceiros = []
contrato = []
colaborador = []
contas = []
# === API: Endpoints JSON ===

# === Clientes (JSON) ===
@routes.route('/api/clientes', methods=['GET'])
def obter_clientes():
    return jsonify(clientes), 200

@routes.route('/api/clientes', methods=['POST'])
def criar_cliente():
    data = request.json
    novo_cliente = {
        "id": len(clientes) + 1,
        "nome": data.get("nome"),
        "endereco": data.get("endereco"),
        "email": data.get("email"),
        "telefone": data.get("telefone"),
        "segmento": data.get("segmento"),
        "status": data.get("status")
    }
    clientes.append(novo_cliente)
    return jsonify({"message": "Cliente criado com sucesso!", "cliente": novo_cliente}), 201

@routes.route('/api/clientes/<int:id>', methods=['PUT'])
def atualizar_cliente(id):
    cliente = next((c for c in clientes if c["id"] == id), None)
    if not cliente:
        return jsonify({"error": "Cliente não encontrado"}), 404
    data = request.json
    cliente.update({
        "nome": data.get("nome", cliente["nome"]),
        "endereco": data.get("endereco", cliente["endereco"]),
        "email": data.get("email", cliente["email"]),
        "telefone": data.get("telefone", cliente["telefone"]),
        "segmento": data.get("segmento", cliente["segmento"]),
        "status": data.get("status", cliente["status"])
    })
    return jsonify({"message": "Cliente atualizado com sucesso!"}), 200

@routes.route('/api/clientes/<int:id>', methods=['DELETE'])
def deletar_cliente(id):
    global clientes
    cliente = next((c for c in clientes if c["id"] == id), None)
    if not cliente:
        return jsonify({"error": "Cliente não encontrado"}), 404
    clientes = [c for c in clientes if c["id"] != id]
    return jsonify({"message": "Cliente deletado com sucesso!"}), 200


# === Projetos ===
@routes.route('/api/projetos', methods=['GET'])
def obter_projetos():
    return jsonify(projetos), 200

@routes.route('/api/projetos', methods=['POST'])
def criar_projeto():
    data = request.json
    novo_projeto = {
        "id": len(projetos) + 1,
        "nome": data.get("nome"),
        "escopo": data.get("escopo"),
        "prazo": data.get("prazo"),
        "gerente": data.get("gerente"),
        "desenvolvedor": data.get("desenvolvedor"),
        "designer": data.get("designer")
    }
    projetos.append(novo_projeto)
    return jsonify({"message": "Projeto criado com sucesso!", "projeto": novo_projeto}), 201

@routes.route('/api/projetos/<int:id>', methods=['PUT'])
def atualizar_projeto(id):
    projeto = next((p for p in projetos if p["id"] == id), None)
    if not projeto:
        return jsonify({"error": "Projeto não encontrado"}), 404
    data = request.json
    projeto.update({
        "nome": data.get("nome", projeto["nome"]),
        "escopo": data.get("escopo", projeto["escopo"]),
        "prazo": data.get("prazo", projeto["prazo"]),
        "gerente": data.get("gerente", projeto["gerente"]),
        "desenvolvedor": data.get("desenvolvedor", projeto["desenvolvedor"]),
        "designer": data.get("designer", projeto["designer"])
    })
    return jsonify({"message": "Projeto atualizado com sucesso!"}), 200

@routes.route('/api/projetos/<int:id>', methods=['DELETE'])
def deletar_projeto(id):
    global projetos
    projeto = next((p for p in projetos if p["id"] == id), None)
    if not projeto:
        return jsonify({"error": "Projeto não encontrado"}), 404
    projetos = [p for p in projetos if p["id"] != id]
    return jsonify({"message": "Projeto deletado com sucesso!"}), 200

# === Contas do Projeto ===
@routes.route('/api/contas-projetos', methods=['GET'])
def obter_contas_projetos():
    return jsonify(contas_projeto), 200

@routes.route('/api/contas-projetos', methods=['POST'])
def criar_conta_projeto():
    data = request.json
    nova_conta = {
        "id": len(contas_projeto) + 1,
        "nome": data.get("nome"),
        "valor": data.get("valor"),
        "vencimento": data.get("vencimento"),
        "status": data.get("status")
    }
    contas_projeto.append(nova_conta)
    return jsonify({"message": "Conta criada com sucesso!", "conta": nova_conta}), 201

@routes.route('/api/contas-projetos/<int:id>', methods=['PUT'])
def atualizar_conta_projeto(id):
    conta = next((c for c in contas_projeto if c["id"] == id), None)
    if not conta:
        return jsonify({"error": "Conta não encontrada"}), 404
    data = request.json
    conta.update({
        "nome": data.get("nome", conta["nome"]),
        "valor": data.get("valor", conta["valor"]),
        "vencimento": data.get("vencimento", conta["vencimento"]),
        "status": data.get("status", conta["status"])
    })
    return jsonify({"message": "Conta do projeto atualizada com sucesso!"}), 200

@routes.route('/api/contas-projetos/<int:id>', methods=['DELETE'])
def deletar_conta_projeto(id):
    global contas_projeto
    conta = next((c for c in contas_projeto if c["id"] == id), None)
    if not conta:
        return jsonify({"error": "Conta não encontrada"}), 404
    contas_projeto = [c for c in contas_projeto if c["id"] != id]
    return jsonify({"message": "Conta deletada com sucesso!"}), 200

# === API: Softwares ===
@routes.route('/api/softwares', methods=['GET'])
def obter_softwares():
    return jsonify(softwares), 200

@routes.route('/api/softwares', methods=['POST'])
def criar_software():
    data = request.json
    novo_software = {
        "id": len(softwares) + 1,
        "projeto": data.get("projeto"),
        "funcionalidade": data.get("funcionalidade"),
        "cliente": data.get("cliente"),
        "versao": data.get("versao")
    }
    softwares.append(novo_software)
    return jsonify({"message": "Software criado com sucesso!", "software": novo_software}), 201

@routes.route('/api/softwares/<int:id>', methods=['PUT'])
def atualizar_software(id):
    software = next((s for s in softwares if s["id"] == id), None)
    if not software:
        return jsonify({"error": "Software não encontrado"}), 404
    data = request.json
    software.update({
        "projeto": data.get("projeto", software["projeto"]),
        "funcionalidade": data.get("funcionalidade", software["funcionalidade"]),
        "cliente": data.get("cliente", software["cliente"]),
        "versao": data.get("versao", software["versao"])
    })
    return jsonify({"message": "Software atualizado com sucesso!"}), 200

@routes.route('/api/softwares/<int:id>', methods=['DELETE'])
def deletar_software(id):
    global softwares
    software = next((s for s in softwares if s["id"] == id), None)
    if not software:
        return jsonify({"error": "Software não encontrado"}), 404
    softwares = [s for s in softwares if s["id"] != id]
    return jsonify({"message": "Software deletado com sucesso!"}), 200

# === API: Recursos ===
@routes.route('/api/recursos', methods=['GET'])
def obter_recursos():
    return jsonify(recursos), 200

@routes.route('/api/recursos', methods=['POST'])
def criar_recurso():
    data = request.json
    novo_recurso = {
        "id": len(recursos) + 1,
        "nome": data.get("nome"),
        "tipo": data.get("tipo"),
        "quantidade": data.get("quantidade")
    }
    recursos.append(novo_recurso)
    return jsonify({"message": "Recurso criado com sucesso!", "recurso": novo_recurso}), 201

@routes.route('/api/recursos/<int:id>', methods=['PUT'])
def atualizar_recurso(id):
    recurso = next((r for r in recursos if r["id"] == id), None)
    if not recurso:
        return jsonify({"error": "Recurso não encontrado"}), 404
    data = request.json
    recurso.update({
        "nome": data.get("nome", recurso["nome"]),
        "tipo": data.get("tipo", recurso["tipo"]),
        "quantidade": data.get("quantidade", recurso["quantidade"])
    })
    return jsonify({"message": "Recurso atualizado com sucesso!"}), 200

@routes.route('/api/recursos/<int:id>', methods=['DELETE'])
def deletar_recurso(id):
    global recursos
    recurso = next((r for r in recursos if r["id"] == id), None)
    if not recurso:
        return jsonify({"error": "Recurso não encontrado"}), 404
    recursos = [r for r in recursos if r["id"] != id]
    return jsonify({"message": "Recurso deletado com sucesso!"}), 200

# === API: Parceiros ===
@routes.route('/api/parceiros', methods=['GET'])
def obter_parceiros():
    return jsonify(parceiros), 200

@routes.route('/api/parceiros', methods=['POST'])
def criar_parceiro():
    data = request.json
    novo_parceiro = {
        "id": len(parceiros) + 1,
        "nome": data.get("nome"),
        "endereco": data.get("endereco"),
        "telefone": data.get("telefone"),
        "email": data.get("email"),
        "tipo_de_parceiro": data.get("tipo_de_parceiro")
    }
    parceiros.append(novo_parceiro)
    return jsonify({"message": "Parceiro criado com sucesso!", "parceiro": novo_parceiro}), 201

@routes.route('/api/parceiros/<int:id>', methods=['PUT'])
def atualizar_parceiro(id):
    parceiro = next((p for p in parceiros if p["id"] == id), None)
    if not parceiro:
        return jsonify({"error": "Parceiro não encontrado"}), 404
    data = request.json
    parceiro.update({
        "nome": data.get("nome", parceiro["nome"]),
        "endereco": data.get("endereco", parceiro["endereco"]),
        "telefone": data.get("telefone", parceiro["telefone"]),
        "email": data.get("email", parceiro["email"]),
        "tipo_de_parceiro": data.get("tipo_de_parceiro", parceiro["tipo_de_parceiro"])
    })
    return jsonify({"message": "Parceiro atualizado com sucesso!"}), 200

@routes.route('/api/parceiros/<int:id>', methods=['DELETE'])
def deletar_parceiro(id):
    global parceiros
    parceiro = next((p for p in parceiros if p["id"] == id), None)
    if not parceiro:
        return jsonify({"error": "Parceiro não encontrado"}), 404
    parceiros = [p for p in parceiros if p["id"] != id]
    return jsonify({"message": "Parceiro deletado com sucesso!"}), 200

# === API: Contratos ===
@routes.route('/api/contratos', methods=['GET'])
def obter_contratos():
    return jsonify(contratos), 200

@routes.route('/api/contratos', methods=['POST'])
def criar_contrato():
    global contratos  # Adicione esta linha para referenciar a variável global
    logging.debug(f"Dados recebidos: {request.json}")
    data = request.json
    if not data:
        return jsonify({"error": "Dados inválidos"}), 400
    novo_contrato = {
        "id": len(contratos) + 1,
        "cliente": data.get("cliente"),
        "tipo_plano": data.get("tipo_plano"),
        "status": data.get("status"),
        "valor": data.get("valor")
    }
    contratos.append(novo_contrato)
    return jsonify({"message": "Contrato criado com sucesso!", "contrato": novo_contrato}), 201

@routes.route('/api/contratos/<int:id>', methods=['PUT'])
def atualizar_contrato(id):
    contrato = next((c for c in contratos if c["id"] == id), None)
    if not contrato:
        return jsonify({"error": "Contrato não encontrado"}), 404
    data = request.json
    contrato.update({
        "cliente": data.get("cliente", contrato["cliente"]),
        "tipo_plano": data.get("tipo_plano", contrato["tipo_plano"]),
        "status": data.get("status", contrato["status"]),
        "valor": data.get("valor", contrato["valor"])
    })
    return jsonify({"message": "Contrato atualizado com sucesso!"}), 200

@routes.route('/api/contratos/<int:id>', methods=['DELETE'])
def deletar_contrato(id):
    global contratos
    contrato = next((c for c in contratos if c["id"] == id), None)
    if not contrato:
        return jsonify({"error": "Contrato não encontrado"}), 404
    contratos = [c for c in contratos if c["id"] != id]
    return jsonify({"message": "Contrato deletado com sucesso!"}), 200

# === API: Colaboradores ===
@routes.route('/api/colaboradores', methods=['GET'])
def obter_colaboradores():
    return jsonify(colaboradores), 200

@routes.route('/api/colaboradores', methods=['POST'])
def criar_colaborador():
    data = request.json
    novo_colaborador = {
        "id": len(colaboradores) + 1,
        "nome": data.get("nome"),
        "endereco": data.get("endereco"),
        "salario": data.get("salario"),
        "cargo": data.get("cargo"),
        "telefone": data.get("telefone"),
        "email": data.get("email")
    }
    colaboradores.append(novo_colaborador)
    return jsonify({"message": "Colaborador criado com sucesso!", "colaborador": novo_colaborador}), 201

@routes.route('/api/colaboradores/<int:id>', methods=['PUT'])
def atualizar_colaborador(id):
    colaborador = next((c for c in colaboradores if c["id"] == id), None)
    if not colaborador:
        return jsonify({"error": "Colaborador não encontrado"}), 404
    data = request.json
    colaborador.update({
        "nome": data.get("nome", colaborador["nome"]),
        "endereco": data.get("endereco", colaborador["endereco"]),
        "salario": data.get("salario", colaborador["salario"]),
        "cargo": data.get("cargo", colaborador["cargo"]),
        "telefone": data.get("telefone", colaborador["telefone"]),
        "email": data.get("email", colaborador["email"])
    })
    return jsonify({"message": "Colaborador atualizado com sucesso!"}), 200

@routes.route('/api/colaboradores/<int:id>', methods=['DELETE'])
def deletar_colaborador(id):
    global colaboradores
    colaborador = next((c for c in colaboradores if c["id"] == id), None)
    if not colaborador:
        return jsonify({"error": "Colaborador não encontrado"}), 404
    colaboradores = [c for c in colaboradores if c["id"] != id]
    return jsonify({"message": "Colaborador deletado com sucesso!"}), 200

# === API: Contas ===
@routes.route('/api/contas', methods=['GET'])
def obter_contas():
    return jsonify(contas), 200

@routes.route('/api/contas', methods=['POST'])
def criar_conta():
    data = request.json
    nova_conta = {
        "id": len(contas) + 1,
        "nome": data.get("nome"),
        "valor": data.get("valor"),
        "vencimento": data.get("vencimento"),
        "status": data.get("status")
    }
    contas.append(nova_conta)
    return jsonify({"message": "Conta criada com sucesso!", "conta": nova_conta}), 201

@routes.route('/api/contas/<int:id>', methods=['PUT'])
def atualizar_conta(id):
    conta = next((c for c in contas if c["id"] == id), None)
    if not conta:
        return jsonify({"error": "Conta não encontrada"}), 404
    data = request.json
    conta.update({
        "nome": data.get("nome", conta["nome"]),
        "valor": data.get("valor", conta["valor"]),
        "vencimento": data.get("vencimento", conta["vencimento"]),
        "status": data.get("status", conta["status"])
    })
    return jsonify({"message": "Conta atualizada com sucesso!"}), 200

@routes.route('/api/contas/<int:id>', methods=['DELETE'])
def deletar_conta(id):
    global contas
    conta = next((c for c in contas if c["id"] == id), None)
    if not conta:
        return jsonify({"error": "Conta não encontrada"}), 404
    contas = [c for c in contas if c["id"] != id]
    return jsonify({"message": "Conta deletada com sucesso!"}), 200

# === Rotas HTML: Clientes ===
@routes.route('/clientes', methods=['GET'])
def clientes_page():
    return render_template('clientes.html', clientes=clientes)

@routes.route('/clientes/<int:id>', methods=['GET'])
def cliente_detail(id):
    cliente = next((c for c in clientes if c["id"] == id), None)
    if not cliente:
        return render_template('error.html', message="Cliente não encontrado"), 404
    return render_template('cliente_detail.html', cliente=cliente)

# === Rotas HTML: Projetos ===
@routes.route('/projetos', methods=['GET'])
def projetos_page():
    return render_template('projetos.html', projetos=projetos)

@routes.route('/projetos/<int:id>', methods=['GET'])
def projeto_detail(id):
    projeto = next((p for p in projetos if p["id"] == id), None)
    if not projeto:
        return render_template('error.html', message="Projeto não encontrado"), 404
    return render_template('projeto_detail.html', projeto=projeto)

# === Rotas HTML: Contas do Projeto ===
@routes.route('/contasprojeto', methods=['GET'])
def contasprojeto_page():
    return render_template('contasprojeto.html', projetos=projetos)

@routes.route('/contasprojeto/<int:id>', methods=['GET'])
def contaprojeto_detail(id):
    projeto = next((p for p in projetos if p["id"] == id), None)
    if not projeto:
        return render_template('error.html', message="Conta do projeto não encontrada"), 404
    return render_template('contaprojeto_detail.html', projeto=projeto)

# === Rotas HTML: Softwares ===
@routes.route('/softwares', methods=['GET'])
def softwares_page():
    return render_template('softwares.html', softwares=softwares)

@routes.route('/softwares/<int:id>', methods=['GET'])
def software_detail(id):
    software = next((s for s in softwares if s["id"] == id), None)
    if not software:
        return render_template('error.html', message="Software não encontrado"), 404
    return render_template('software_detail.html', software=software)

# === Rotas HTML: Recursos ===
@routes.route('/recursos', methods=['GET'])
def recursos_page():
    return render_template('recursos.html', recursos=recursos)

@routes.route('/recursos/<int:id>', methods=['GET'])
def recurso_detail(id):
    recurso = next((r for r in recursos if r["id"] == id), None)
    if not recurso:
        return render_template('error.html', message="Recurso não encontrado"), 404
    return render_template('recurso_detail.html', recurso=recurso)

# === Rotas HTML: Parceiros ===
@routes.route('/parceiros', methods=['GET'])
def parceiros_page():
    return render_template('parceiros.html', parceiros=parceiros)

@routes.route('/parceiros/<int:id>', methods=['GET'])
def parceiro_detail(id):
    parceiro = next((p for p in parceiros if p["id"] == id), None)
    if not parceiro:
        return render_template('error.html', message="Parceiro não encontrado"), 404
    return render_template('parceiro_detail.html', parceiro=parceiro)

# === Rotas HTML: Contratos ===
@routes.route('/contratos', methods=['GET'])
def contratos_page():
    return render_template('contratos.html', contratos=contratos)

@routes.route('/contratos/<int:id>', methods=['GET'])
def contrato_detail(id):
    contrato = next((c for c in contratos if c["id"] == id), None)
    if not contrato:
        return render_template('error.html', message="Contrato não encontrado"), 404
    return render_template('contrato_detail.html', contrato=contrato)

# === Rotas HTML: Colaboradores ===
@routes.route('/colaboradores', methods=['GET'])
def colaboradores_page():
    return render_template('colaboradores.html', colaboradores=colaboradores)

@routes.route('/colaboradores/<int:id>', methods=['GET'])
def colaborador_detail(id):
    colaborador = next((c for c in colaboradores if c["id"] == id), None)
    if not colaborador:
        return render_template('error.html', message="Colaborador não encontrado"), 404
    return render_template('colaborador_detail.html', colaborador=colaborador)

# === Rotas HTML: Contas ===
@routes.route('/contas', methods=['GET'])
def contas_page():
    return render_template('contas.html', contas=contas)

@routes.route('/contas/<int:id>', methods=['GET'])
def conta_detail(id):
    conta = next((c for c in contas if c["id"] == id), None)
    if not conta:
        return render_template('error.html', message="Conta não encontrada"), 404
    return render_template('conta_detail.html', conta=conta)
# === Rota para o Menu Principal ===
@routes.route('/menu', methods=['GET'])
def menu_page():
    return render_template('menu.html')
