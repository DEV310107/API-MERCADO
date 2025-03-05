﻿# API-MERCADO
 <!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Documentação da API - Sistema de Gestão</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
        }
        h1, h2 {
            color: #333;
        }
        h3 {
            color: #555;
        }
        pre {
            background-color: #f4f4f4;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        code {
            color: #d6336c;
            font-weight: bold;
        }
        .endpoint {
            margin-bottom: 20px;
        }
        .endpoint h3 {
            margin-top: 10px;
        }
    </style>
</head>
<body>

    <h1>Documentação da API - Sistema de Gestão</h1>

    <p>Esta documentação descreve a API para um sistema de gestão de clientes, produtos e ordens de venda, desenvolvida com Flask e utilizando arquivos CSV para armazenamento.</p>

    <h2>Endpoints da API</h2>

    <div class="endpoint">
        <h3>GET /clientes</h3>
        <p>Retorna todos os clientes armazenados no arquivo <code>Clientes.csv</code>.</p>
        <pre><code>GET /clientes</code></pre>
        <h4>Resposta:</h4>
        <pre><code>[
    [1, "João", "Silva", "1990-01-01", "12345678900"],
    [2, "Maria", "Oliveira", "1985-05-10", "98765432100"]
]</code></pre>
    </div>

    <div class="endpoint">
        <h3>GET /ordensdevenda</h3>
        <p>Retorna todas as ordens de venda armazenadas no arquivo <code>OrdensDeVenda.csv</code>.</p>
        <pre><code>GET /ordensdevenda</code></pre>
        <h4>Resposta:</h4>
        <pre><code>[
    [1, 1, 2],
    [2, 2, 3]
]</code></pre>
    </div>

    <div class="endpoint">
        <h3>GET /produtos</h3>
        <p>Retorna todos os produtos armazenados no arquivo <code>Produtos.csv</code>.</p>
        <pre><code>GET /produtos</code></pre>
        <h4>Resposta:</h4>
        <pre><code>[
    [1, "Produto A", "Fornecedor X", 10],
    [2, "Produto B", "Fornecedor Y", 20]
]</code></pre>
    </div>

    <div class="endpoint">
        <h3>POST /add_cliente</h3>
        <p>Adiciona um novo cliente. A requisição deve enviar um JSON com as informações do cliente.</p>
        <pre><code>POST /add_cliente</code></pre>
        <h4>Corpo da requisição:</h4>
        <pre><code>{
    "nome": "Carlos",
    "sobrenome": "Souza",
    "data de nascimento": "1982-03-15",
    "cpf": "11223344556"
}</code></pre>
        <h4>Resposta:</h4>
        <pre><code>{
    "message": "Cliente adicionado!",
    "cliente": [3, "Carlos", "Souza", "1982-03-15", "11223344556"]
}</code></pre>
    </div>

    <div class="endpoint">
        <h3>POST /add_produto</h3>
        <p>Adiciona um novo produto. A requisição deve enviar um JSON com as informações do produto.</p>
        <pre><code>POST /add_produto</code></pre>
        <h4>Corpo da requisição:</h4>
        <pre><code>{
    "nome": "Produto C",
    "fornecedor": "Fornecedor Z",
    "quantidade": 50
}</code></pre>
        <h4>Resposta:</h4>
        <pre><code>{
    "message": "Produto adicionado!",
    "produto": [3, "Produto C", "Fornecedor Z", 50]
}</code></pre>
    </div>

    <div class="endpoint">
        <h3>POST /add_ordemdevenda</h3>
        <p>Adiciona uma nova ordem de venda. A requisição deve enviar um JSON com as informações da ordem.</p>
        <pre><code>POST /add_ordemdevenda</code></pre>
        <h4>Corpo da requisição:</h4>
        <pre><code>{
    "cliente_id": 1,
    "produto_id": 2
}</code></pre>
        <h4>Resposta:</h4>
        <pre><code>{
    "message": "Ordem de venda adicionada!",
    "ordem": [3, 1, 2]
}</code></pre>
    </div>

    <div class="endpoint">
        <h3>PUT /up_cliente</h3>
        <p>Atualiza as informações de um cliente. A requisição deve enviar um JSON com o ID do cliente e os dados a serem atualizados.</p>
        <pre><code>PUT /up_cliente</code></pre>
        <h4>Corpo da requisição:</h4>
        <pre><code>{
    "cliente_id": 1,
    "nome": "João Pedro"
}</code></pre>
        <h4>Resposta:</h4>
        <pre><code>{
    "message": "Cliente atualizado!"
}</code></pre>
    </div>

    <div class="endpoint">
        <h3>PUT /up_produto</h3>
        <p>Atualiza as informações de um produto. A requisição deve enviar um JSON com o ID do produto e os dados a serem atualizados.</p>
        <pre><code>PUT /up_produto</code></pre>
        <h4>Corpo da requisição:</h4>
        <pre><code>{
    "produto_id": 1,
    "quantidade": 15
}</code></pre>
        <h4>Resposta:</h4>
        <pre><code>{
    "message": "Produto atualizado!"
}</code></pre>
    </div>

    <div class="endpoint">
        <h3>PUT /up_ordemdevenda</h3>
        <p>Atualiza as informações de uma ordem de venda. A requisição deve enviar um JSON com o ID da ordem e os dados a serem atualizados.</p>
        <pre><code>PUT /up_ordemdevenda</code></pre>
        <h4>Corpo da requisição:</h4>
        <pre><code>{
    "ordem_id": 1,
    "cliente_id": 2
}</code></pre>
        <h4>Resposta:</h4>
        <pre><code>{
    "message": "Ordem de venda atualizada!"
}</code></pre>
    </div>

    <div class="endpoint">
        <h3>DELETE /clientes/{id}</h3>
        <p>Deleta um cliente baseado no ID. A requisição deve enviar o ID do cliente na URL.</p>
        <pre><code>DELETE /clientes/1</code></pre>
        <h4>Resposta:</h4>
        <pre><code>{
    "message": "Cliente deletado!"
}</code></pre>
    </div>

    <div class="endpoint">
        <h3>DELETE /produtos/{id}</h3>
        <p>Deleta um produto baseado no ID. A requisição deve enviar o ID do produto na URL.</p>
        <pre><code>DELETE /produtos/1</code></pre>
        <h4>Resposta:</h4>
        <pre><code>{
    "message": "Produto deletado!"
}</code></pre>
    </div>

    <div class="endpoint">
        <h3>DELETE /ordensdevenda/{id}</h3>
        <p>Deleta uma ordem de venda baseada no ID. A requisição deve enviar o ID da ordem de venda na URL.</p>
        <pre><code>DELETE /ordensdevenda/1</code></pre>
        <h4>Resposta:</h4>
        <pre><code>{
    "message": "Ordem de venda deletada!"
}</code></pre>
    </div>

    <h2>Erros Comuns</h2>
    <p>Todos os endpoints retornam um erro com o status 500 ou 404 se algo der errado. A resposta de erro inclui uma mensagem com detalhes sobre o problema.</p>

</body>
</html>

