from flask import Flask, jsonify
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

@app.route("/delete_")

if __name__ == "__main__":
    app.run(debug=True)
