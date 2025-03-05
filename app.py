from flask import Flask, request, jsonify
import csv

app = Flask(__name__)
ids = 0

@app.route("/clientes", methods=["GET"])
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
        return jsonify({"error": str(e)}), 404

@app.route("/ordensdevenda", methods=["GET"])
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
        return jsonify({"error": str(e)}), 404

@app.route("/produtos", methods=["GET"])
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
        return jsonify({"error": str(e)}), 404

@app.route("/add_cliente", methods=["post"])
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
        return jsonify({"Error"}), 404

@app.route("/add_produto", methods=["post"])
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
        return jsonify({"error": str(e)}), 500

@app.route("/add_ordemdevenda", methods=["post"])
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
        return jsonify({"error": str(e)}), 500
    
@app.route("/up_cliente", methods=["put"])
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
        return jsonify({"error"}), 404

@app.route("/up_produto", methods=["put"])
def up_produto():
    try:
        rows = []
        data = request.get_json()
        produto_id = data["produto_id"]
        file_path = 'Produtos.csv'
        with open(file_path, mode='r', newline='', encoding='utf-8') as arquivo:
            reader = csv.reader(arquivo)
            for linha in reader:
                if linha[0] == produto_id:
                    linha[1] = data.get("nome", linha[1])
                    linha[2] = data.get("fornecedor", linha[2])
                    linha[3] = data.get("quantidade", linha[3])
                rows.append(linha)
        with open(file_path, mode='w', newline='', encoding='utf-8') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerows(rows)
        return jsonify({"message": "Produto atualizado!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404

@app.route("/up_ordemdevenda", methods=["put"])
def up_ordemdevenda():
    try:
        rows = []
        data = request.get_json()
        ordem_id = data["ordem_id"]
        file_path = 'OrdensDeVenda.csv'
        with open(file_path, mode='r', newline='', encoding='utf-8') as arquivo:
            reader = csv.reader(arquivo)
            for linha in reader:
                if linha[0] == ordem_id:
                    linha[1] = data.get("cliente_id", linha[1])
                    linha[2] = data.get("produto_id", linha[2])
                rows.append(linha)
        with open(file_path, mode='w', newline='', encoding='utf-8') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerows(rows)
        return jsonify({"message": "Ordem de venda atualizada!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404

@app.route("/clientes/<int:id>", methods=["DELETE"])
def delete_cliente(id):
    try:
        file_path = 'Clientes.csv'
        rows = []
        with open(file_path, mode='r', newline='', encoding='utf-8') as arquivo:
            reader = csv.reader(arquivo)
            for linha in reader:
                if int(linha[0]) != id:
                    rows.append(linha)
        with open(file_path, mode='w', newline='', encoding='utf-8') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerows(rows)
        return jsonify({"message": "Cliente deletado!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/produtos/<int:id>", methods=["DELETE"])
def delete_produto(id):
    try:
        file_path = 'Produtos.csv'
        rows = []
        with open(file_path, mode='r', newline='', encoding='utf-8') as arquivo:
            reader = csv.reader(arquivo)
            for linha in reader:
                if int(linha[0]) != id:
                    rows.append(linha)
        with open(file_path, mode='w', newline='', encoding='utf-8') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerows(rows)
        return jsonify({"message": "Produto deletado!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/ordensdevenda/<int:id>", methods=["DELETE"])
def delete_ordemdevenda(id):
    try:
        file_path = 'OrdensDeVenda.csv'
        rows = []
        with open(file_path, mode='r', newline='', encoding='utf-8') as arquivo:
            reader = csv.reader(arquivo)
            for linha in reader:
                if int(linha[0]) != id:
                    rows.append(linha)
        with open(file_path, mode='w', newline='', encoding='utf-8') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerows(rows)
        return jsonify({"message": "Ordem de venda deletada!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
                

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')