import pygame

def cargar_imagenes (ruta:str, tamaño:int):
    imagen = pygame.image.load(ruta).convert()
    imagen.set_colorkey((4,255,0))
    imagen = pygame.transform.scale(imagen,(imagen.get_width() * tamaño ,imagen.get_height() * tamaño))
    return imagen

def crear_lista_imagenes (ruta_imagen :str, tamaño:int, cantidad_imagenes: int):
    i = 0
    lista_imagenes = []
    for i in range(cantidad_imagenes):
        ruta = ruta_imagen + str (i) + ".png"
        imagen = cargar_imagenes(ruta, tamaño)
        lista_imagenes.append(imagen)
        i += 1
    return lista_imagenes



