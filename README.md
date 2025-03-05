<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Documentação sobre Flask e Ambiente Virtual</title>
</head>
<body>
    <h1>Introdução ao Flask</h1>
    <p>Flask é um microframework para a linguagem Python que facilita a criação de aplicações web.</p>

    <h2>Instalação</h2>
    <p>Para instalar o Flask precisa ativar um ambiente virtual, use os seguintes comandos para a ativação:</p>

    <h3>Criando um ambiente virtual</h3>
    <p>Para criar um ambiente virtual em Python, use o seguinte comando:</p>
    <pre><code>python -m venv venv</code></pre>
    <p>Isso criará uma pasta chamada venv com todos os arquivos necessários.</p>

    <h3>Ativando o ambiente virtual</h3>
    <p>Windows (PowerShell):</p>
    <pre><code>.\venv\Scripts\Activate.ps1</code></pre>
    <p>Se ocorrer um erro, talvez seja necessário modificar a permissão de execução de scripts:</p>
    <pre><code>Set-ExecutionPolicy RemoteSigned</code></pre>

    <h3>Instalando pacotes dentro do venv</h3>
    <p>Após ativar o ambiente virtual, você pode instalar pacotes normalmente com pip:</p>
    <pre><code>pip install flask</code></pre>

    <h2>Biblioteca jsonify</h2>
    <p>A função jsonify é usada para converter dicionários e listas Python em respostas JSON formatadas corretamente.</p>
    <h3>Exemplo de Uso</h3>
    <pre><code>from flask import jsonify

@app.route('/data')
def data():
    return jsonify({"message": "Hello, JSON!", "status": 200})</code></pre>

    <h2>Biblioteca Flask</h2>
    <p>A classe Flask é a base do framework e permite criar e gerenciar a aplicação.</p>
    <h3>Exemplo de Uso</h3>
    <pre><code>app = Flask(__name__)</code></pre>
    <p>A partir dessa instância, é possível definir rotas, configurar a aplicação e iniciar o servidor.</p>

    <h2>Biblioteca Request</h2>
    <p>A classe Request permite acessar dados das requisições HTTP, como parâmetros, cabeçalhos e corpo da requisição.</p>
    <h3>Exemplo de Uso</h3>
    <pre><code>from flask import request, jsonify

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    return jsonify({"username": username, "authenticated": True})</code></pre>

    <h2>MÉTODO GET</h2>

    <h3>Rota /clientes (GET)</h3>
    <p>Retorna a lista de clientes cadastrados no arquivo Clientes.csv.</p>
    <h4>Exemplo de Uso:</h4>
    <pre><code>@app.route("/clientes", methods=["GET"])
def cliente():
    try:
        file_path = 'Clientes.csv'
        clientes = []
        # Abre o arquivo CSV e lê seus dados
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                clientes.append(row)  # Adiciona cada linha do CSV à lista
        return jsonify(clientes), 200  # Retorna a lista em formato JSON
    except Exception as e:
        return jsonify({"error": str(e)}), 404  # Retorna erro caso ocorra uma exceção</code></pre>

    <h3>Rota /ordensdevenda (GET)</h3>
    <p>Retorna a lista de ordens de venda cadastradas no arquivo OrdensDeVenda.csv.</p>
    <h4>Exemplo de Uso:</h4>
    <pre><code>@app.route("/ordensdevenda", methods=["GET"])
def ordens():
    try:
        file_path = 'OrdensDeVenda.csv'
        ordens = []
        # Abre o arquivo CSV e lê seus dados
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                ordens.append(row)  # Adiciona cada linha do CSV à lista
        return jsonify(ordens), 200  # Retorna a lista em formato JSON
    except Exception as e:
        return jsonify({"error": str(e)}), 404  # Retorna erro caso ocorra uma exceção</code></pre>

    <h3>Rota /produtos (GET)</h3>
    <p>Retorna a lista de produtos cadastrados no arquivo Produtos.csv.</p>
    <h4>Exemplo de Uso:</h4>
    <pre><code>@app.route("/produtos", methods=["GET"])
def produtos():
    try:
        file_path = 'Produtos.csv'
        produtos = []
        # Abre o arquivo CSV e lê seus dados
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                produtos.append(row)  # Adiciona cada linha do CSV à lista
        return jsonify(produtos), 200  # Retorna a lista em formato JSON
    except Exception as e:
        return jsonify({"error": str(e)}), 404  # Retorna erro caso ocorra uma exceção</code></pre>

    <h2>Explicação</h2>
    <p>Cada uma dessas rotas:</p>
    <ul>
        <li>Lê os dados de um arquivo CSV específico (Clientes.csv, OrdensDeVenda.csv, Produtos.csv).</li>
        <li>Converte os dados em uma lista e retorna no formato JSON.</li>
        <li>Maneja exceções caso o arquivo não seja encontrado ou ocorra algum erro na leitura.</li>
    </ul>

    <h2>Comentários sobre o código</h2>
    <ul>
        <li><strong>try-except:</strong> Utilizado para capturar possíveis erros durante a leitura do arquivo.</li>
        <li><strong>open(file_path, mode='r', newline='', encoding='utf-8'):</strong> Abre o arquivo CSV no modo de leitura, garantindo a compatibilidade com caracteres especiais.</li>
        <li><strong>csv.reader(file):</strong> Permite a leitura do arquivo CSV linha por linha.</li>
        <li><strong>jsonify(lista):</strong> Retorna os dados convertidos para JSON, garantindo que sejam acessíveis via API.</li>
        <li><strong>return jsonify(data), 200:</strong> Retorna os dados e o código HTTP 200 (OK) quando a requisição for bem-sucedida.</li>
        <li><strong>return jsonify({"error": str(e)}), 404:</strong> Retorna um erro e código HTTP 404 caso o arquivo não seja encontrado ou ocorra outro problema.</li>
    </ul>
</body>
</html>
