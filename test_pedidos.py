from pedidos import validar_pedido

def test_validar_pedido():
    pedido_1 = {"cliente": "Pedro", "cantidad": True, "precio": 12}
    pedido_2 = {"cliente": "Maria", "cantidad": 4, "precio": 15}
    pedido_3 = {"cliente": "", "cantidad": 3, "precio": 10}

    assert validar_pedido(pedido_1) == False
    assert validar_pedido(pedido_2) == True
    assert validar_pedido(pedido_3) == False

    print("Todas las pruebas han pasado correctamente")