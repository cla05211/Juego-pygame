import pygame
from constantes import *

def activar_modo_admi(lista_rects:list, pantalla:object):
    for rect in lista_rects:
        pygame.draw.rect(pantalla,COLOR_VERDE,rect,2,3)