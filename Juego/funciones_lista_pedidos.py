from scripts.comidas import Comidas

def manejar_diccionario_pedidos (diccionario_pedidos:dict, numero_pedido: int, pedido,operacion:str):
    match operacion:
        case "agregar":
            diccionario_pedidos[str(numero_pedido)] = pedido
        case "eliminar":
            diccionario_pedidos.pop(str(numero_pedido))
    return diccionario_pedidos
