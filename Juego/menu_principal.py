import pygame
from funciones_carga import cargar_imagenes_inicio
from constantes import *
from menu_niveles import iniciar_menu_niveles

def iniciar_menu_inicio():
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO_PANTALLA,ALTO_PANTALLA])
    caption = pygame.display.set_caption("Juego")
    diccionario_imagenes = cargar_imagenes_inicio("menu")
    rect_fondo = diccionario_imagenes["fondo"].get_rect()
    corriendo = True
    rect_boton = diccionario_imagenes["boton_jugar"].get_rect()
    rect_boton.x = 90
    rect_boton.y = 130
    jugar = False

    while corriendo:
        pantalla.blit(diccionario_imagenes["fondo"],rect_fondo)
        #Boton
        pantalla.blit(diccionario_imagenes["boton_jugar"],rect_boton) 

        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                corriendo = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                posicion_click = list(evento.pos)
                if rect_boton.collidepoint(posicion_click):
                    jugar = True
                    corriendo = False

        pygame.display.flip()

    if jugar:
        iniciar_menu_niveles()
