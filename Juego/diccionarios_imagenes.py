import pygame
from scripts.carga_archivos import cargar_imagenes

imagenes_niveles = {
        "fondo" : cargar_imagenes("archivos\imagenes\\fondo_actualizado.png",1),
        "barra" : cargar_imagenes("archivos\\barra\\barra.png",1),
        "cliente" : cargar_imagenes("archivos\imagenes\clientes\cliente.png",1),
        "mesa" : cargar_imagenes("archivos\imagenes\mesa.png",1),
        "personaje_dcha" : cargar_imagenes("archivos\imagenes\personaje\derecha.png",1),
        "personaje_abajo" : cargar_imagenes("archivos\imagenes\personaje\\frente.png", 1),
        "personaje_izq" : cargar_imagenes("archivos\imagenes\personaje\izquierda.png",1),
        "personaje_arriba" : cargar_imagenes("archivos\imagenes\personaje\\atras.png",1),
        "cliente_enojado": cargar_imagenes("archivos\imagenes\clientes\cliente_enojado.png",1),
        "monedas": cargar_imagenes("archivos\imagenes\dinero\monedas.png",1),
        "pilas_monedas": cargar_imagenes("archivos\imagenes\dinero\pila_monedas.png",1),
        "billetes": cargar_imagenes("archivos\imagenes\dinero\\billetes.png",1),
        "burbuja_dialogo_vacia": cargar_imagenes("archivos\imagenes\\burbujas_dialogo\\burbuja_blanco.png",1),
        "burbuja_esperando": cargar_imagenes("archivos\imagenes\\burbujas_dialogo\\burbuja_puntos_suspensivos.png",1),
        "burbuja_corazon": cargar_imagenes("archivos\imagenes\\burbujas_dialogo\\burbuja_corazon.png",1),
        "burbuja_cruz": cargar_imagenes("archivos\imagenes\\burbujas_dialogo\\burbuja_cruz.png",1)
    }

