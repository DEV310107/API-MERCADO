import csv
import os
file_path = 'ordens_de_venda.csv'
if not os.path.exists(file_path):   
    open(file_path, mode="w").close()
else: 
    print("O arquivo já existe")