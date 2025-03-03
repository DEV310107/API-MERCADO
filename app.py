from flask import Flask, jsonify, request
import csv

app = Flask(__name__)

clientes = [["id", "nome", "sobrenome", "data-de-nascimento", "cpf"]]
produtos = [["id", "nome", "fornecedor", "quantidade"]]
ordens_de_venda = [["id", "cliente", "produto"]]


with open("clientes.csv", "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerows(clientes)

with open("produtos.csv", "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerows(produtos)

with open("ordem_de_venda.csv", "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerows(ordens_de_venda)


@app.route("/clientes", methods=["GET"])
def listar_clientes():
    return jsonify(clientes)

@app.route("/produtos", methods=["GET"])
def listar_produtos():
    return jsonify(produtos)

@app.route("/ordens_de_venda", methods=["GET"])
def listar_ordens_de_venda():
    return jsonify(ordens_de_venda)


@app.route("/add_cliente", methods=["POST"])
def add_cliente():
    data = request.get_json()
    clientes[f"{len(clientes) + 1}"] = data
    return jsonify(clientes), 200

@app.route("/add_produto", methods=["POST"])
def add_produto():
    data = request.get_json()
    produtos[f"{len(produtos) + 1}"] = data
    return jsonify(produtos), 200

@app.route("/add_ordem_de_venda", methods=["POST"])
def add_ordem_de_venda():
    data = request.get_json()
    ordens_de_venda[f"{len(ordens_de_venda) + 1}"] = data
    return jsonify(ordens_de_venda),200

@app.route("/update_cliente", methods=["PUT"])
def update_cliente():
    data = request.get_json()
    if data["id"] in clientes:
        for chave, valor in data.items():
            if chave != "id":
                clientes[data["id"]][chave] = valor
        return jsonify(clientes), 200
    else:
        return jsonify({"erro": "Cliente não encontrado"}), 404

@app.route("/update_produto", methods=["PUT"])
def update_produto():
    data = request.get_json()
    if data["id"] in produtos:
        for chave, valor in data.items():
            if chave != "id":
                produtos[data["id"]][chave] = valor
        return jsonify(produtos), 200
    else:
        return jsonify({"erro": "Produto não encontrado"}), 404

@app.route("/update_ordem_de_venda", methods=["PUT"])
def update_ordem_de_venda():
    data = request.get_json()
    if data["id"] in ordens_de_venda:
        for chave, valor in data.items():
            if chave != "id":
                ordens_de_venda[data["id"]][chave] = valor
        return jsonify(ordens_de_venda), 200
    else:
        return jsonify({"erro": "Ordem de venda não encontrada"}), 404
    

@app.route("/delete_cliente/<int:id>", methods=["DELETE"])
def delete_cliente(id):
    global clientes
    clientes = [linha for linha in clientes if linha[0] != id or linha[0] == "id"]
    return jsonify({"mensagem": "Cliente removido!"}), 200

@app.route("/delete_produto/<int:id>", methods=["DELETE"])
def delete_produto(id):
    global produtos
    produtos = [linha for linha in produtos if linha[0] != id or linha[0] == "id"]
    return jsonify({"mensagem": "Produto removido!"}), 200

@app.route("/delete_ordem_de_venda/<int:id>", methods=["DELETE"])
def delete_ordem_de_venda(id):
    global ordens_de_venda
    ordens_de_venda = [linha for linha in ordens_de_venda if linha[0] != id or linha[0] == "id"]
    return jsonify({"mensagem": "Ordem de venda removida!"}), 200

if __name__ == "__main__":
    app.run(debug=True)