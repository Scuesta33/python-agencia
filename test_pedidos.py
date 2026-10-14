import pytest
from pedidos import validar_pedido, calcular_facturacion

def test_validar_pedido():
    pedido_1 = {"cliente": "Pedro", "cantidad": True, "precio": 12}
    pedido_2 = {"cliente": "Maria", "cantidad": 4, "precio": 15}
    pedido_3 = {"cliente": "", "cantidad": 3, "precio": 10}

    assert validar_pedido(pedido_1) == False
    assert validar_pedido(pedido_2) == True
    assert validar_pedido(pedido_3) == False

    print("Todas las pruebas han pasado correctamente")

def test_facturacion():
    pedidos = [
        {"cliente": "Ana", "cantidad": 5, "precio": 12},
        {"cliente": "Maria", "cantidad": 4, "precio": 15}
    ]

    assert calcular_facturacion(pedidos) == 120

def test_facturacion_vacia():
    pedido = []

    assert calcular_facturacion(pedido) == 0

@pytest.mark.parametrize(
    "precio, resultado_esperado",
    [
        (10, True),
        (15.5, True),
        (0, False),
        (-5, False),
        ("gratis", False),
        (True, False)
    ]
)
def test_precios(precio, resultado_esperado):
    pedido = {
        "cliente": "Ana",
        "cantidad": 5,
        "precio": precio
    }

    assert validar_pedido(pedido) == resultado_esperado