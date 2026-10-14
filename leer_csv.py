import csv

with open("pedidos.csv", "r", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)

    for pedido in lector:
        print(pedido)