# models.py

# Classe base para Pessoa
class Pessoa:
    def __init__(self, id, nome, endereco, email, telefone):
        self.id = id
        self.nome = nome
        self.endereco = endereco
        self.email = email
        self.telefone = telefone

# Classe para Cliente
class Cliente(Pessoa):
    def __init__(self, id, nome, endereco, email, telefone, segmento, status):
        super().__init__(id, nome, endereco, email, telefone)
        self.segmento = segmento
        self.status = status

# Classe para Colaborador
class Colaborador(Pessoa):
    def __init__(self, id, nome, endereco, email, telefone, salario, cargo):
        super().__init__(id, nome, endereco, email, telefone)
        self.salario = salario
        self.cargo = cargo

# Classe para Projeto
class Projeto:
    def __init__(self, id, nome, escopo, prazo, gerente, desenvolvedor, designer):
        self.id = id
        self.nome = nome
        self.escopo = escopo
        self.prazo = prazo
        self.gerente = gerente
        self.desenvolvedor = desenvolvedor
        self.designer = designer

# Classe para Recurso
class Recurso:
    def __init__(self, id, nome, tipo, quantidade):
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.quantidade = quantidade

# Classe para Contrato
class Contrato:
    def __init__(self, id, tipo_de_plano, status, valor, cliente_id):
        self.id = id
        self.tipo_de_plano = tipo_de_plano
        self.status = status
        self.valor = valor
        self.cliente_id = cliente_id

# Classe para ContasProjeto
class ContasProjeto:
    def __init__(self, id, nome, valor, vencimento, status):
        self.id = id
        self.nome = nome
        self.valor = valor
        self.vencimento = vencimento
        self.status = status

# Classe para Software
class Software:
    def __init__(self, id, projeto, funcionalidade, cliente, versao):
        self.id = id
        self.projeto = projeto
        self.funcionalidade = funcionalidade
        self.cliente = cliente
        self.versao = versao

# Classe para Parceiro
class Parceiro:
    def __init__(self, id, nome, tipo_de_parceiro):
        self.id = id
        self.nome = nome
        self.tipo_de_parceiro = tipo_de_parceiro
