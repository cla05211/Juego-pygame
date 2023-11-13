import pygame


def cargar_imagenes_sin_ruta (categoria_imagen:str,nombre_imagen:str,tamaño:int):
    ruta = f"archivos\imagenes\{categoria_imagen}\{nombre_imagen}.png"
    imagen = pygame.image.load(ruta).convert()
    imagen.set_colorkey((105,67,63))
    imagen = pygame.transform.scale(imagen,(imagen.get_width() * tamaño ,imagen.get_height() * tamaño))
    return imagen

def cargar_imagenes (ruta:str,tamaño:int):
    imagen = pygame.image.load(ruta).convert()
    imagen.set_colorkey((105,67,63))
    imagen = pygame.transform.scale(imagen,(imagen.get_width() * tamaño ,imagen.get_height() * tamaño))
    return imagen


