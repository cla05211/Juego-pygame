import pygame

def activar_modo_control (pantalla,lista_rects:list)->None:
    for elemento in lista_rects:
        bordes = pygame.draw.rect(pantalla,(4,255,0),(elemento.x,elemento.y,elemento.width,elemento.height),2)