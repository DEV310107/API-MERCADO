from flask import Flask
import csv

clientes = [["id", "nome", "sobrenome", "data-de-nascimento", "cpf"]]
produtos = [["id", "nome", "fornecedor", "quantidade"]]
ordem_de_venda = [["id", "cliente", "produto"]]

with open("clientes.csv", "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerows(clientes) 

with open("produtos.csv", "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerows(produtos)

with open("ordem_de_venda.csv", "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerows(ordem_de_venda)


@app.route("/clientes", methods=["get"])
def cliente():
    return clientes

@app.route("/produtos", methods=["get"])
def produto():
    return produtos

@app.route("/ordem_de_venda", methods=["get"])
def ordem_de_venda():
    return ordem_de_venda


 