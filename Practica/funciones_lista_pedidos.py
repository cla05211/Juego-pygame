from scripts.comidas import Comidas

def manejar_lista_pedidos (lista_pedidos:list, agregar_o_sacar: str, pedido):
    if len(lista_pedidos) == 0:
        lista_pedidos = []
    match agregar_o_sacar:
        case "agregar":
            lista_pedidos.append(pedido)
    return lista_pedidos
