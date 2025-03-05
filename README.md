# 🛒 Documentação API Mercado

Para começar deve se abri um ambiente virtual  para utilização do FLASK:

### 📱 Criando um ambiente virtual

Para criar um ambiente virtual em Python, use o seguinte comando:

```powershell
python -m venv venv
```

Isso criará uma pasta chamada `venv` com todos os arquivos necessários.

### Ativando o ambiente virtual

### Windows (PowerShell):

```
.\venv\Scripts\Activate.ps1
```

Se ocorrer um erro, talvez seja necessário modificar a permissão de execução de scripts:

```
Set-ExecutionPolicy RemoteSigned
```

### Instalando pacotes dentro do venv

Após ativar o ambiente virtual, você pode instalar pacotes normalmente com pip:

```
pip install flask
```

# 📖 Biblioteca Utilizadas:

## 🟥 Biblioteca `jsonify`

A função `jsonify` é usada para converter dicionários e listas Python em respostas JSON formatadas corretamente.

### Exemplo de Uso

```
from flask import jsonify

@app.route('/data')
def data():
    return jsonify({"message": "Hello, JSON!", "status": 200})
```

## 🟥 Biblioteca `Flask`

A classe `Flask` é a base do framework e permite criar e gerenciar a aplicação.

### Exemplo de Uso

```
app = Flask(__name__)
```

A partir dessa instância, é possível definir rotas, configurar a aplicação e iniciar o servidor.

## 🟥 Biblioteca `Request`

A classe `Request` permite acessar dados das requisições HTTP, como parâmetros, cabeçalhos e corpo da requisição.

### Exemplo de Uso

```
from flask import request, jsonify

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    return jsonify({"username": username, "authenticated": True})
```

## 👑 Métodos HTTP da API

### 🟩 Método GET

Os métodos GET são usados para recuperar informações armazenadas nos arquivos CSV. Nossa API possui três rotas GET:

### 1. Listar clientes

```python
@app.route("/clientes", methods=["GET"])  # Define a rota "/clientes" que só responde a requisições GET.
def cliente():  # Define a função que será executada quando a rota for acessada.
    try:  # Começa um bloco try-except para capturar exceções durante a execução.
        file_path = 'Clientes.csv'  # Define o caminho do arquivo CSV onde os dados dos clientes estão armazenados.
        clientes = []  # Cria uma lista vazia que armazenará os dados dos clientes.
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:  # Abre o arquivo CSV no modo leitura.
            reader = csv.reader(file)  # Cria um objeto reader para ler o conteúdo do CSV.
            for row in reader:  # Itera sobre cada linha do arquivo CSV.
                clientes.append(row)  # Adiciona a linha lida à lista 'clientes'.
        return jsonify(clientes), 200  # Retorna a lista de clientes como resposta JSON com o status 200 (OK).
    except Exception as e:  # Se ocorrer uma exceção durante a execução, o bloco except é executado.
        return jsonify({"error": str(e)}), 404  # Retorna a mensagem de erro como resposta JSON com o status 404 (não encontrado).

```

Essa rota retorna uma lista de clientes armazenados no arquivo `Clientes.csv`. O código lê o arquivo CSV, armazena as linhas em uma lista e retorna a lista em formato JSON. Caso ocorra um erro, uma mensagem de erro é retornada com status 404.

### 2. Listar ordens de venda

```python
@app.route("/ordensdevenda", methods=["GET"])  # Define a rota "/ordensdevenda" que só responde a requisições GET.
def ordens():  # Define a função que será executada quando a rota for acessada.
    try:  # Começa um bloco try-except para capturar exceções durante a execução.
        file_path = 'OrdensDeVenda.csv'  # Define o caminho do arquivo CSV onde os dados das ordens de venda estão armazenados.
        ordens = []  # Cria uma lista vazia que armazenará os dados das ordens de venda.
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:  # Abre o arquivo CSV no modo leitura.
            reader = csv.reader(file)  # Cria um objeto reader para ler o conteúdo do CSV.
            for row in reader:  # Itera sobre cada linha do arquivo CSV.
                ordens.append(row)  # Adiciona a linha lida à lista 'ordens'.
        return jsonify(ordens), 200  # Retorna a lista de ordens como resposta JSON com o status 200 (OK).
    except Exception as e:  # Se ocorrer uma exceção durante a execução, o bloco except é executado.
        return jsonify({"error": str(e)}), 404  # Retorna a mensagem de erro como resposta JSON com o status 404 (não encontrado).

```

Essa rota retorna todas as ordens de venda do arquivo `OrdensDeVenda.csv`. O processo é semelhante ao do método GET de clientes.

### 3. Listar produtos

```python
@app.route("/produtos", methods=["GET"])  # Define a rota "/produtos" que só responde a requisições GET.
def produtos():  # Define a função que será executada quando a rota for acessada.
    try:  # Começa um bloco try-except para capturar exceções durante a execução.
        file_path = 'Produtos.csv'  # Define o caminho do arquivo CSV onde os dados dos produtos estão armazenados.
        produtos = []  # Cria uma lista vazia que armazenará os dados dos produtos.
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:  # Abre o arquivo CSV no modo leitura.
            reader = csv.reader(file)  # Cria um objeto reader para ler o conteúdo do CSV.
            for row in reader:  # Itera sobre cada linha do arquivo CSV.
                produtos.append(row)  # Adiciona a linha lida à lista 'produtos'.
        return jsonify(produtos), 200  # Retorna a lista de produtos como resposta JSON com o status 200 (OK).
    except Exception as e:  # Se ocorrer uma exceção durante a execução, o bloco except é executado.
        return jsonify({"error": str(e)}), 404  # Retorna a mensagem de erro como resposta JSON com o status 404 (não encontrado).

```

Essa rota retorna todos os produtos armazenados no arquivo `Produtos.csv`.

### 🟩 Método POST

O método **POST** é utilizado para enviar dados ao servidor, geralmente para criar novos registros.

### 1. Adicionar Cliente

```python
python
CopiarEditar
@app.route("/add_cliente", methods=["POST"])
def add_cliente():
    try:
        data = request.get_json()  # Obtém os dados enviados na requisição em formato JSON.
        global ids
        ids += 1  # Incrementa o ID para o próximo cliente.
        cliente = [ids, data["nome"], data["sobrenome"], data["data de nascimento"], data["cpf"]]  # Cria o novo cliente.
        file_path = 'Clientes.csv'  # Caminho do arquivo CSV onde os dados serão salvos.
        with open(file_path, mode='a', newline='', encoding='utf-8') as file:  # Abre o arquivo em modo de adição.
            writer = csv.writer(file)  # Cria o objeto que escreve no arquivo.
            writer.writerow(cliente)  # Escreve os dados do cliente no arquivo.
        return jsonify({"message": "Cliente adicionado!", "cliente": cliente}), 200  # Retorna uma resposta com status 200.
    except Exception as e:
        return jsonify({"Error": str(e)}), 404  # Retorna erro em caso de falha.

```

```python
@app.route("/add_produto", methods=["post"])  # Define a rota '/add_produto' com método POST para adicionar um produto.
def add_produto():  # Função chamada quando a rota é acessada.
    try:  # Tenta executar o código abaixo.
        global ids  # Usa a variável global 'ids' para gerar um ID único para o produto.
        ids += 1  # Incrementa o ID global para o próximo produto.
        data = request.get_json()  # Obtém os dados enviados no corpo da requisição como JSON.
        produto = [ids, data["nome"], data["fornecedor"], data["quantidade"]]  # Cria uma lista com as informações do produto.
        file_path = 'Produtos.csv'  # Define o caminho do arquivo CSV onde os dados serão salvos.
        with open(file_path, mode='a', newline='', encoding='utf-8') as arquivo:  # Abre o arquivo CSV no modo de anexar ('a') com codificação UTF-8.
            writer = csv.writer(arquivo)  # Cria um objeto escritor para escrever no arquivo CSV.
            writer.writerow(produto)  # Escreve a lista de produto como uma nova linha no arquivo CSV.
        return jsonify({"message": "Produto adicionado!", "produto": produto}), 200  # Retorna uma resposta JSON com sucesso e os dados do produto.
    except Exception as e:  # Se ocorrer algum erro, entra no bloco de exceção.
        return jsonify({"error": str(e)}), 500  # Retorna uma resposta JSON com a mensagem de erro e status 500 (erro do servidor).

```

```python
@app.route("/add_ordemdevenda", methods=["post"])  # Define a rota '/add_ordemdevenda' com método POST para adicionar uma ordem de venda.
def add_ordemdevenda():  # Função chamada quando a rota é acessada.
    try:  # Tenta executar o código abaixo.
        data = request.get_json()  # Obtém os dados enviados no corpo da requisição como JSON.
        ordem = [ids, data["cliente_id"], data["produto_id"]]  # Cria uma lista com o ID da ordem e os IDs do cliente e do produto.
        file_path = 'OrdensDeVenda.csv'  # Define o caminho do arquivo CSV onde os dados serão salvos.
        with open(file_path, mode='a', newline='', encoding='utf-8') as file:  # Abre o arquivo CSV no modo de anexar ('a') com codificação UTF-8.
            writer = csv.writer(file)  # Cria um objeto escritor para escrever no arquivo CSV.
            writer.writerow(ordem)  # Escreve a lista de ordem como uma nova linha no arquivo CSV.
        return jsonify({"message": "Ordem de venda adicionada!", "ordem": ordem}), 200  # Retorna uma resposta JSON com sucesso e os dados da ordem de venda.
    except Exception as e:  # Se ocorrer algum erro, entra no bloco de exceção.
        return jsonify({"error": str(e)}), 500  # Retorna uma resposta JSON com a mensagem de erro e status 500 (erro do servidor).

```

**Explicação**:
Este método adiciona um novo cliente no arquivo `Clientes.csv`. Ele recebe um JSON no corpo da requisição com os dados do cliente e adiciona uma nova linha no arquivo CSV com esses dados.

---

### 🟩 Método PUT

O método **PUT** é utilizado para atualizar registros existentes no servidor.

### 2. Atualizar Cliente

```python
python
CopiarEditar
@app.route("/up_cliente", methods=["PUT"])
def up_cliente():
    try:
        rows = []  # Lista para armazenar as linhas alteradas.
        data = request.get_json()  # Obtém os dados enviados na requisição em formato JSON.
        cliente_id = data["cliente_id"]  # ID do cliente a ser atualizado.
        file_path = 'Clientes.csv'  # Caminho do arquivo CSV.
        with open(file_path, mode='r', newline='', encoding='utf-8') as arquivo:
            reader = csv.reader(arquivo)  # Lê as linhas do arquivo.
            for linha in reader:
                if linha[0] == cliente_id:  # Verifica se o cliente ID corresponde.
                    linha[1] = data.get("nome", linha[1])  # Atualiza o nome, se fornecido.
                    linha[2] = data.get("sobrenome", linha[2])  # Atualiza o sobrenome, se fornecido.
                    linha[3] = data.get("data de nascimento", linha[3])  # Atualiza a data de nascimento, se fornecido.
                    linha[4] = data.get("cpf", linha[4])  # Atualiza o CPF, se fornecido.
                rows.append(linha)  # Adiciona a linha ao array.
        with open(file_path, mode='w', newline='', encoding='utf-8') as arquivo:
            writer = csv.writer(arquivo)  # Reescreve o arquivo com as linhas modificadas.
            writer.writerows(rows)  # Escreve todas as linhas de volta.
        return jsonify({"message": "Cliente atualizado!"}), 200  # Retorna uma resposta de sucesso.
    except Exception as e:
        return jsonify({"error": str(e)}), 404  # Retorna erro caso ocorra uma falha.

```

```python
@app.route("/up_produto", methods=["put"])  # Define a rota '/up_produto' com método PUT para atualizar um produto.
def up_produto():  # Função chamada quando a rota é acessada.
    try:  # Tenta executar o código abaixo.
        rows = []  # Lista para armazenar todas as linhas do arquivo CSV.
        data = request.get_json()  # Obtém os dados enviados no corpo da requisição como JSON.
        produto_id = data["produto_id"]  # Obtém o ID do produto a ser atualizado.
        file_path = 'Produtos.csv'  # Define o caminho do arquivo CSV onde os dados dos produtos estão armazenados.
        with open(file_path, mode='r', newline='', encoding='utf-8') as arquivo:  # Abre o arquivo CSV no modo de leitura.
            reader = csv.reader(arquivo)  # Cria um objeto leitor para ler o arquivo CSV.
            for linha in reader:  # Itera sobre cada linha do arquivo.
                if linha[0] == produto_id:  # Verifica se o ID do produto na linha é igual ao ID fornecido.
                    linha[1] = data.get("nome", linha[1])  # Atualiza o nome, se fornecido; caso contrário, mantém o valor original.
                    linha[2] = data.get("fornecedor", linha[2])  # Atualiza o fornecedor, se fornecido.
                    linha[3] = data.get("quantidade", linha[3])  # Atualiza a quantidade, se fornecido.
                rows.append(linha)  # Adiciona a linha (atualizada ou não) à lista de 'rows'.
        with open(file_path, mode='w', newline='', encoding='utf-8') as arquivo:  # Abre o arquivo CSV no modo de escrita.
            writer = csv.writer(arquivo)  # Cria um objeto escritor para escrever no arquivo CSV.
            writer.writerows(rows)  # Escreve todas as linhas de volta no arquivo CSV, incluindo as atualizações.
        return jsonify({"message": "Produto atualizado!"}), 200  # Retorna uma resposta JSON com sucesso.
    except Exception as e:  # Se ocorrer algum erro, entra no bloco de exceção.
        return jsonify({"error": str(e)}), 404  # Retorna uma resposta JSON com a mensagem de erro e status 404.

```

```python
@app.route("/up_ordemdevenda", methods=["put"])  # Define a rota '/up_ordemdevenda' com método PUT para atualizar uma ordem de venda.
def up_ordemdevenda():  # Função chamada quando a rota é acessada.
    try:  # Tenta executar o código abaixo.
        rows = []  # Lista para armazenar todas as linhas do arquivo CSV.
        data = request.get_json()  # Obtém os dados enviados no corpo da requisição como JSON.
        ordem_id = data["ordem_id"]  # Obtém o ID da ordem de venda a ser atualizada.
        file_path = 'OrdensDeVenda.csv'  # Define o caminho do arquivo CSV onde as ordens de venda estão armazenadas.
        with open(file_path, mode='r', newline='', encoding='utf-8') as arquivo:  # Abre o arquivo CSV no modo de leitura.
            reader = csv.reader(arquivo)  # Cria um objeto leitor para ler o arquivo CSV.
            for linha in reader:  # Itera sobre cada linha do arquivo.
                if linha[0] == ordem_id:  # Verifica se o ID da ordem na linha é igual ao ID fornecido.
                    linha[1] = data.get("cliente_id", linha[1])  # Atualiza o cliente_id, se fornecido; caso contrário, mantém o valor original.
                    linha[2] = data.get("produto_id", linha[2])  # Atualiza o produto_id, se fornecido.
                rows.append(linha)  # Adiciona a linha (atualizada ou não) à lista de 'rows'.
        with open(file_path, mode='w', newline='', encoding='utf-8') as arquivo:  # Abre o arquivo CSV no modo de escrita.
            writer = csv.writer(arquivo)  # Cria um objeto escritor para escrever no arquivo CSV.
            writer.writerows(rows)  # Escreve todas as linhas de volta no arquivo CSV, incluindo as atualizações.
        return jsonify({"message": "Ordem de venda atualizada!"}), 200  # Retorna uma resposta JSON com sucesso.
    except Exception as e:  # Se ocorrer algum erro, entra no bloco de exceção.
        return jsonify({"error": str(e)}), 404  # Retorna uma resposta JSON com a mensagem de erro e status 404.

```

**Explicação**:
Este método permite atualizar um cliente existente no arquivo `Clientes.csv`. Ele recebe os novos dados de um cliente no corpo da requisição e atualiza os campos correspondentes.

---

### 🟩 Método DELETE

O método **DELETE** é utilizado para remover um registro do servidor.

### Deletar Cliente

```python
python
CopiarEditar
@app.route("/clientes/<int:id>", methods=["DELETE"])
def delete_cliente(id):
    try:
        file_path = 'Clientes.csv'  # Caminho do arquivo CSV.
        rows = []  # Lista para armazenar as linhas após a exclusão.
        with open(file_path, mode='r', newline='', encoding='utf-8') as arquivo:
            reader = csv.reader(arquivo)  # Lê o arquivo CSV.
            for linha in reader:
                if int(linha[0]) != id:  # Se o ID não corresponde ao cliente a ser deletado, mantém a linha.
                    rows.append(linha)
        with open(file_path, mode='w', newline='', encoding='utf-8') as arquivo:
            writer = csv.writer(arquivo)  # Reescreve o arquivo sem a linha deletada.
            writer.writerows(rows)  # Escreve as linhas restantes.
        return jsonify({"message": "Cliente deletado!"}), 200  # Resposta de sucesso.
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Resposta de erro em caso de falha.

```

```python
@app.route("/produtos/<int:id>", methods=["DELETE"])  # Define a rota '/produtos/<id>' com método DELETE para excluir um produto pelo ID.
def delete_produto(id):  # Função chamada quando a rota é acessada, com o 'id' do produto a ser excluído.
    try:  # Tenta executar o código abaixo.
        file_path = 'Produtos.csv'  # Define o caminho do arquivo CSV onde os dados dos produtos estão armazenados.
        rows = []  # Lista para armazenar as linhas do arquivo, sem o produto a ser excluído.
        with open(file_path, mode='r', newline='', encoding='utf-8') as arquivo:  # Abre o arquivo CSV no modo de leitura.
            reader = csv.reader(arquivo)  # Cria um objeto leitor para ler o arquivo CSV.
            for linha in reader:  # Itera sobre cada linha do arquivo.
                if int(linha[0]) != id:  # Verifica se o ID da linha é diferente do ID fornecido.
                    rows.append(linha)  # Adiciona a linha à lista 'rows' se o produto não for o a ser excluído.
        with open(file_path, mode='w', newline='', encoding='utf-8') as arquivo:  # Abre o arquivo CSV no modo de escrita.
            writer = csv.writer(arquivo)  # Cria um objeto escritor para escrever no arquivo CSV.
            writer.writerows(rows)  # Escreve as linhas restantes de volta no arquivo CSV, excluindo o produto.
        return jsonify({"message": "Produto deletado!"}), 200  # Retorna uma resposta JSON com sucesso.
    except Exception as e:  # Se ocorrer algum erro, entra no bloco de exceção.
        return jsonify({"error": str(e)}), 500  # Retorna uma resposta JSON com a mensagem de erro e status 500.

```

```python
@app.route("/ordensdevenda/<int:id>", methods=["DELETE"])  # Define a rota '/ordensdevenda/<id>' com método DELETE para excluir uma ordem de venda pelo ID.
def delete_ordemdevenda(id):  # Função chamada quando a rota é acessada, com o 'id' da ordem de venda a ser excluída.
    try:  # Tenta executar o código abaixo.
        file_path = 'OrdensDeVenda.csv'  # Define o caminho do arquivo CSV onde as ordens de venda estão armazenadas.
        rows = []  # Lista para armazenar as linhas do arquivo, sem a ordem de venda a ser excluída.
        with open(file_path, mode='r', newline='', encoding='utf-8') as arquivo:  # Abre o arquivo CSV no modo de leitura.
            reader = csv.reader(arquivo)  # Cria um objeto leitor para ler o arquivo CSV.
            for linha in reader:  # Itera sobre cada linha do arquivo.
                if int(linha[0]) != id:  # Verifica se o ID da linha é diferente do ID fornecido.
                    rows.append(linha)  # Adiciona a linha à lista 'rows' se a ordem de venda não for a a ser excluída.
        with open(file_path, mode='w', newline='', encoding='utf-8') as arquivo:  # Abre o arquivo CSV no modo de escrita.
            writer = csv.writer(arquivo)  # Cria um objeto escritor para escrever no arquivo CSV.
            writer.writerows(rows)  # Escreve as linhas restantes de volta no arquivo CSV, excluindo a ordem de venda.
        return jsonify({"message": "Ordem de venda deletada!"}), 200  # Retorna uma resposta JSON com sucesso.
    except Exception as e:  # Se ocorrer algum erro, entra no bloco de exceção.
        return jsonify({"error": str(e)}), 500  # Retorna uma resposta JSON com a mensagem de erro e status 500.

```

**Explicação**:
Este método deleta um cliente específico do arquivo `Clientes.csv` com base no ID fornecido na URL. As linhas do arquivo são lidas, e todas as linhas que não correspondem ao cliente a ser deletado são mantidas no arquivo.

```

```python
if __name__ == '__main__':  # Verifica se o script está sendo executado diretamente (não importado como módulo).
    app.run(debug=True, host='0.0.0.0')  # Inicia o servidor Flask em modo de depuração (debug) e disponível em todas as interfaces de rede (0.0.0.0).

```

**Parágrafo:**

Esse trecho de código é responsável por iniciar a aplicação Flask quando o script é executado diretamente. A linha `app.run(debug=True, host='0.0.0.0')` faz o servidor rodar em modo de depuração, o que ajuda a identificar erros facilmente, e configura o Flask para aceitar conexões de qualquer interface de rede (`0.0.0.0`). Isso é útil, por exemplo, para rodar a aplicação em um ambiente de desenvolvimento ou testar localmente.


# 💻 Como testar os métodos GET no Postman

1. Abra o Postman.
2. Selecione o método **GET**.
3. Insira a URL da API:
    - `http://127.0.0.1:5000/clientes` para listar clientes.
    - `http://127.0.0.1:5000/ordensdevenda` para listar ordens de venda.
    - `http://127.0.0.1:5000/produtos` para listar produtos.
4. Clique em **Send** e veja a resposta JSON.

### 🖱️ Como testar os métodos POST, PUT e DELETE no Postman

- **POST**:
    1. Escolha o método **POST**.
    2. Insira a URL da API, por exemplo: `http://127.0.0.1:5000/adicionar_cliente`.
    3. Vá para a aba **Body** e escolha **raw**.
    4. Selecione **JSON** no menu dropdown.
    5. Insira os dados no formato:
        
        ```
        {
          "nome": "Cliente Teste",
          "email": "cliente@teste.com"
        }
        ```
        
    6. Clique em **Send** e veja a resposta.
- **PUT**:
    1. Escolha o método **PUT**.
    2. Insira a URL, por exemplo: `http://127.0.0.1:5000/atualizar_cliente/1`.
    3. Insira os novos dados no **Body** como no POST.
    4. Envie a requisição.
- **DELETE**:
    1. Escolha o método **DELETE**.
    2. Insira a URL, por exemplo: `http://127.0.0.1:5000/deletar_cliente/1`.
    3. Clique em **Send** para remover o registro.
