<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Documentação Flask</title>
</head>
<body>
    <h1>Documentação sobre Flask</h1>

    <h2>Introdução ao Flask</h2>
    <p>Flask é um microframework para a linguagem Python que facilita a criação de aplicações web.</p>

    <h3>Instalação</h3>
    <p>Para instalar o Flask precisa ativar um ambiente virtual, use os seguintes comandos para a ativação:</p>

    <h4>Criando um ambiente virtual</h4>
    <p>Para criar um ambiente virtual em Python, use o seguinte comando:</p>
    <pre><code>python -m venv venv</code></pre>
    <p>Isso criará uma pasta chamada <code>venv</code> com todos os arquivos necessários.</p>

    <h4>Ativando o ambiente virtual</h4>
    <h5>Windows (PowerShell):</h5>
    <pre><code>.\venv\Scripts\Activate.ps1</code></pre>
    <p>Se ocorrer um erro, talvez seja necessário modificar a permissão de execução de scripts:</p>
    <pre><code>Set-ExecutionPolicy RemoteSigned</code></pre>

    <h4>Instalando pacotes dentro do venv</h4>
    <p>Após ativar o ambiente virtual, você pode instalar pacotes normalmente com pip:</p>
    <pre><code>pip install flask</code></pre>

    <h2>Biblioteca <code>jsonify</code></h2>
    <p>A função <code>jsonify</code> é usada para converter dicionários e listas Python em respostas JSON formatadas corretamente.</p>
    
    <h3>Exemplo de Uso</h3>
    <pre><code>from flask import jsonify

@app.route('/data')
def data():
    return jsonify({"message": "Hello, JSON!", "status": 200})</code></pre>

    <h2>Biblioteca <code>Flask</code></h2>
    <p>A classe <code>Flask</code> é a base do framework e permite criar e gerenciar a aplicação.</p>

    <h3>Exemplo de Uso</h3>
    <pre><code>app = Flask(__name__)</code></pre>
    <p>A partir dessa instância, é possível definir rotas, configurar a aplicação e iniciar o servidor.</p>

    <h2>Biblioteca <code>Request</code></h2>
    <p>A classe <code>Request</code> permite acessar dados das requisições HTTP, como parâmetros, cabeçalhos e corpo da requisição.</p>

    <h3>Exemplo de Uso</h3>
    <pre><code>from flask import request, jsonify

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    return jsonify({"username": username, "authenticated": True})</code></pre>

    <h2>Métodos HTTP da API</h2>

    <h3>Método GET</h3>
    <p>Os métodos GET são usados para recuperar informações armazenadas nos arquivos CSV. Nossa API possui três rotas GET:</p>

    <h4>1. Listar clientes</h4>
    <pre><code>@app.route("/clientes", methods=["GET"])  # Define a rota "/clientes" que só responde a requisições GET.
def cliente():
    try:
        file_path = 'Clientes.csv'
        clientes = []
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                clientes.append(row)
        return jsonify(clientes), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404</code></pre>

    <h4>2. Listar ordens de venda</h4>
    <pre><code>@app.route("/ordensdevenda", methods=["GET"])  # Define a rota "/ordensdevenda" que só responde a requisições GET.
def ordens():
    try:
        file_path = 'OrdensDeVenda.csv'
        ordens = []
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                ordens.append(row)
        return jsonify(ordens), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404</code></pre>

    <h4>3. Listar produtos</h4>
    <pre><code>@app.route("/produtos", methods=["GET"])  # Define a rota "/produtos" que só responde a requisições GET.
def produtos():
    try:
        file_path = 'Produtos.csv'
        produtos = []
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                produtos.append(row)
        return jsonify(produtos), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404</code></pre>

    <h3>Método POST</h3>
    <p>O método POST é utilizado para enviar dados ao servidor, geralmente para criar novos registros.</p>

    <h4>1. Adicionar Cliente</h4>
    <pre><code>@app.route("/add_cliente", methods=["POST"])
def add_cliente():
    try:
        data = request.get_json()
        global ids
        ids += 1
        cliente = [ids, data["nome"], data["sobrenome"], data["data de nascimento"], data["cpf"]]
        file_path = 'Clientes.csv'
        with open(file_path, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(cliente)
        return jsonify({"message": "Cliente adicionado!", "cliente": cliente}), 200
    except Exception as e:
        return jsonify({"Error": str(e)}), 404</code></pre>

    <h4>2. Adicionar Produto</h4>
    <pre><code>@app.route("/add_produto", methods=["post"])
def add_produto():
    try:
        global ids
        ids += 1
        data = request.get_json()
        produto = [ids, data["nome"], data["fornecedor"], data["quantidade"]]
        file_path = 'Produtos.csv'
        with open(file_path, mode='a', newline='', encoding='utf-8') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow(produto)
        return jsonify({"message": "Produto adicionado!", "produto": produto}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500</code></pre>

    <h4>3. Adicionar Ordem de Venda</h4>
    <pre><code>@app.route("/add_ordemdevenda", methods=["post"])
def add_ordemdevenda():
    try:
        data = request.get_json()
        ordem = [ids, data["cliente_id"], data["produto_id"]]
        file_path = 'OrdensDeVenda.csv'
        with open(file_path, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(ordem)
        return jsonify({"message": "Ordem de venda adicionada!", "ordem": ordem}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500</code></pre>

    <h3>Método PUT</h3>
    <p>O método PUT é utilizado para atualizar registros existentes no servidor.</p>

    <h4>1. Atualizar Cliente</h4>
    <pre><code>@app.route("/up_cliente", methods=["PUT"])
def up_cliente():
    try:
        rows = []
        data = request.get_json()
        cliente_id = data["cliente_id"]
        file_path = 'Clientes.csv'
        with open(file_path, mode='r', newline='', encoding='utf-8') as arquivo:
            reader = csv.reader(arquivo)
            for linha in reader:
                if linha[0] == cliente_id:
                    linha[1] = data.get("nome", linha[1])
                    linha[2] = data.get("sobrenome", linha[2])
                    linha[3] = data.get("data de nascimento", linha[3])
                    linha[4] = data.get("cpf", linha[4])
                rows.append(linha)
        with open(file_path, mode='w', newline='', encoding='utf-8') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerows(rows)
        return jsonify({"message": "Cliente atualizado!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404</code></pre>

    <h4>2. Atualizar Produto</h4>
    <pre><code>@app.route("/up_produto", methods=["put"])
def up_produto():
    try:
        rows = []
        data = request.get_json()
        produto_id = data["produto_id"]
        file_path = 'Produtos.csv'
        with open(file_path, mode='r', newline='', encoding='utf-8
