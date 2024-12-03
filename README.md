Projeto de Programação Orientada a Objetos
Este projeto é uma aplicação web desenvolvida com Flask como parte da disciplina de Programação Orientada a Objetos. Ele implementa um sistema completo com API e templates para gerenciar diversos recursos, como clientes, projetos, contratos e mais.

Funcionalidades
Gestão de Clientes: Cadastro, visualização, atualização e exclusão.
Gestão de Projetos: Controle de projetos, incluindo nome, escopo, prazo e equipe.
Gestão de Contratos: Registro de contratos com clientes, incluindo tipo de plano, status e valor.
Gestão de Softwares: Cadastro de softwares associados aos projetos.
Gestão de Contas e Recursos: Controle financeiro e alocação de recursos para projetos.
Interface Web: Páginas HTML para visualizar e interagir com os dados.
API REST: Endpoints para integração com outros sistemas.
Tecnologias Utilizadas
Linguagem: Python 3.12
Framework: Flask
Banco de Dados: SQLite
Frontend: HTML, CSS (com base no design do Figma)
Versionamento: Git e GitHub
Como Rodar o Projeto
Clone o repositório:

bash
Copiar código
git clone https://github.com/Ricktheus/Programa-o-orientada-a-objetos.git
cd Programa-o-orientada-a-objetos
Crie um ambiente virtual:

bash
Copiar código
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
Instale as dependências:

bash
Copiar código
pip install -r requirements.txt
Execute o servidor:

bash
Copiar código
python main.py
Acesse a aplicação no navegador:

URL: http://127.0.0.1:5000
Estrutura do Projeto
css
Copiar código
Programa-o-orientada-a-objetos/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── menu.html
│   │   ├── clientes.html
│   │   ├── projetos.html
│   │   ├── contratos.html
│   │   ├── ...
│   └── static/
│       └── styles.css
├── test_routes.py
├── main.py
├── requirements.txt
└── README.md
Endpoints
API REST
Clientes:

GET /api/clientes: Lista todos os clientes.
POST /api/clientes: Cria um novo cliente.
PUT /api/clientes/<id>: Atualiza um cliente.
DELETE /api/clientes/<id>: Exclui um cliente.
Projetos:

Similar aos endpoints de clientes.
Contratos, Softwares, Recursos, etc.:

Estrutura similar, alterando o recurso na URL.
Interface Web
GET /menu: Página inicial com botões para acessar as diferentes seções.
GET /clientes: Página para visualizar clientes.
GET /projetos: Página para visualizar projetos.
Outras páginas seguem a mesma estrutura.
Contribuição
Contribuições são bem-vindas! Siga os passos para contribuir:

Faça um fork do repositório.
Crie uma branch para sua feature:
bash
Copiar código
git checkout -b minha-feature
Commit suas mudanças:
bash
Copiar código
git commit -m "Adicionando minha nova feature"
Faça o push para sua branch:
bash
Copiar código
git push origin minha-feature
Abra um pull request.
Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais informações.

Contato
Ricktheus

GitHub: Ricktheus
E-mail: ricktheus@email.com
