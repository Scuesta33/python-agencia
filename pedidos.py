
# ==========================================
# 1. DATOS
# ==========================================

pedidos = [
    {"cliente": "Ana", "producto": "Salmon", "cantidad": 5, "precio": 12},
    {"cliente": "Luis", "producto": "Bacalao", "cantidad": -2, "precio": 9},
    {"cliente": "", "producto": "Salmon", "cantidad": 3, "precio": 12},
    {"cliente": "Maria", "producto": "Atun", "cantidad": 4, "precio": 15}
]


# ==========================================
# 2. VALIDAR PEDIDOS
# ==========================================

def validar_pedido(pedido):
    cliente = pedido["cliente"]
    cantidad = pedido["cantidad"]
    precio = pedido["precio"]

    return cantidad > 0 and cliente != "" and precio > 0


# ==========================================
# 3. CLASIFICAR PEDIDOS
# ==========================================

def clasificar_pedidos(lista_pedidos):
    pedidos_validos = []
    pedidos_invalidos = []

    for pedido in lista_pedidos:
        if validar_pedido(pedido):
            pedidos_validos.append(pedido)
        else:
            pedidos_invalidos.append(pedido)

    return pedidos_validos, pedidos_invalidos


# ==========================================
# 4. CALCULAR FACTURACIÓN
# ==========================================

def calcular_facturacion(lista_pedidos):
    total = 0

    for pedido in lista_pedidos:
        cantidad = pedido["cantidad"]
        precio = pedido["precio"]

        importe_pedido = cantidad * precio
        total += importe_pedido

    return total


# ==========================================
# 5. FUNCIÓN PRINCIPAL
# ==========================================

def main():
    # Clasificar los pedidos
    validos, invalidos = clasificar_pedidos(pedidos)

    # Calcular la facturación
    facturacion = calcular_facturacion(validos)

    # Mostrar resultados
    print("Pedidos válidos:", len(validos))
    print("Pedidos inválidos:", len(invalidos))
    print("Facturación total:", facturacion)


# ==========================================
# 6. EJECUTAR PROGRAMA
# ==========================================

if __name__ == "__main__":
    main()
