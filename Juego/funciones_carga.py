from scripts.carga_archivos import cargar_imagenes
from scripts.mesas import Mesa
from scripts.comidas import Comidas

def cargar_imagenes_inicio()->dict:
    imagenes = {
        "fondo" : cargar_imagenes("archivos\imagenes\\fondo.png",1),
        "barra" : cargar_imagenes("archivos\\barra\\barra.png",1),
        "cliente" : cargar_imagenes("archivos\imagenes\clientes\cliente.png",1),
        "mesa" : cargar_imagenes("archivos\imagenes\mesa.png",1),
        "hamburguesa" : cargar_imagenes("archivos\imagenes\comida\hamburguesa.png",1),
        "helado" : cargar_imagenes("archivos\imagenes\comida\helado.png",1),
        "limonada" : cargar_imagenes("archivos\imagenes\comida\limonada.png",1),
        "personaje_dcha" : cargar_imagenes("archivos\imagenes\personaje\derecha.png",1),
        "personaje_abajo" : cargar_imagenes("archivos\imagenes\personaje\\frente.png", 1),
        "personaje_izq" : cargar_imagenes("archivos\imagenes\personaje\izquierda.png",1),
        "personaje_arriba" : cargar_imagenes("archivos\imagenes\personaje\\atras.png",1),
        "cliente": cargar_imagenes("archivos\imagenes\clientes\cliente.png",1),
        "cliente_enojado": cargar_imagenes("archivos\imagenes\clientes\cliente_enojado.png",1)
    }
    return imagenes

def cargar_lista_mesas (ubicaciones:list,diccionario_imagenes:dict):
    lista_mesas = []
    for ubicacion in ubicaciones:   
        mesa = Mesa([ubicacion[0],ubicacion[1]],diccionario_imagenes["mesa"])
        lista_mesas.append(mesa)
    return lista_mesas

def cargar_imagenes_comidas_disponibles (diccionario_imagenes:dict)->list:
    lista_comidas_disponibles = \
    [   
        cargar_imagenes("archivos\imagenes\comida\hamburguesa.png",1),
        cargar_imagenes("archivos\imagenes\comida\helado.png",1),
        cargar_imagenes("archivos\imagenes\comida\limonada.png",1),    
    ]
    return lista_comidas_disponibles

