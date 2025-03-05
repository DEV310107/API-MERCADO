import csv
import os
file_path = 'Clientes.csv'
if not os.path.exists(file_path):   
    open(file_path, mode="w").close()
else: 
    print("O arquivo já existe")