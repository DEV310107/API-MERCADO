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
