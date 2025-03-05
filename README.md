# Introdução ao Flask

Flask é um microframework para a linguagem Python que facilita a criação de aplicações web.

## Instalação

Para instalar o Flask, é necessário ativar um ambiente virtual. Use os seguintes comandos para a ativação:

### Criando um ambiente virtual

Para criar um ambiente virtual em Python, use o seguinte comando:

```bash
python -m venv venv
Isso criará uma pasta chamada venv com todos os arquivos necessários.

Ativando o ambiente virtual
Windows (PowerShell):

bash
Copiar
Editar
.\venv\Scripts\Activate.ps1
Se ocorrer um erro, talvez seja necessário modificar a permissão de execução de scripts:

bash
Copiar
Editar
Set-ExecutionPolicy RemoteSigned
Instalando pacotes dentro do venv
Após ativar o ambiente virtual, você pode instalar pacotes normalmente com pip:

bash
Copiar
Editar
pip install flask
Biblioteca jsonify
A função jsonify é usada para converter dicionários e listas Python em respostas JSON formatadas corretamente.

Exemplo de Uso
python
Copiar
Editar
from flask import jsonify

@app.route('/data')
def data():
    return jsonify({"message": "Hello, JSON!", "status": 200})
Biblioteca Flask
A classe Flask é a base do framework e permite criar e gerenciar a aplicação.

Exemplo de Uso
python
Copiar
Editar
app = Flask(__name__)
A partir dessa instância, é possível definir rotas, configurar a aplicação e iniciar o servidor.

Biblioteca Request
A classe Request permite acessar dados das requisições HTTP, como parâmetros, cabeçalhos e corpo da requisição.

Exemplo de Uso
python
Copiar
Editar
from flask import request, jsonify

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    return jsonify({"username": username, "authenticated": True})
MÉTODO GET
Rota /clientes (GET)
Retorna a lista de clientes cadastrados no arquivo Clientes.csv.

Exemplo de Uso:
python
Copiar
Editar
@app.route("/clientes", methods=["GET"])
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
        return jsonify({"error": str(e)}), 404  # Retorna erro caso ocorra uma exceção
Rota /ordensdevenda (GET)
Retorna a lista de ordens de venda cadastradas no arquivo OrdensDeVenda.csv.

Exemplo de Uso:
python
Copiar
Editar
@app.route("/ordensdevenda", methods=["GET"])
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
        return jsonify({"error": str(e)}), 404  # Retorna erro caso ocorra uma exceção
Rota /produtos (GET)
Retorna a lista de produtos cadastrados no arquivo Produtos.csv.

Exemplo de Uso:
python
Copiar
Editar
@app.route("/produtos", methods=["GET"])
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
        return jsonify({"error": str(e)}), 404  # Retorna erro caso ocorra uma exceção
Explicação
Cada uma dessas rotas:

Lê os dados de um arquivo CSV específico (Clientes.csv, OrdensDeVenda.csv, Produtos.csv).
Converte os dados em uma lista e retorna no formato JSON.
Maneja exceções caso o arquivo não seja encontrado ou ocorra algum erro na leitura.
Comentários sobre o código
try-except: Utilizado para capturar possíveis erros durante a leitura do arquivo.
open(file_path, mode='r', newline='', encoding='utf-8'): Abre o arquivo CSV no modo de leitura, garantindo a compatibilidade com caracteres especiais.
csv.reader(file): Permite a leitura do arquivo CSV linha por linha.
jsonify(lista): Retorna os dados convertidos para JSON, garantindo que sejam acessíveis via API.
return jsonify(data), 200: Retorna os dados e o código HTTP 200 (OK) quando a requisição for bem-sucedida.
return jsonify({"error": str(e)}), 404: Retorna um erro e código HTTP 404 caso o arquivo não seja encontrado ou ocorra outro problema.
css
Copiar
Editar

Isso deve te ajudar a ter o conteúdo em Markdown, que pode ser facilmente interpretado por gerenciadores de markdown como GitHub ou outros editores.






