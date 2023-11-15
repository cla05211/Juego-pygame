import pygame
from funciones_carga import cargar_imagenes_inicio
from constantes import *
from menu_niveles import iniciar_menu_niveles
from funciones_carga import cargar_sonidos
from ranking import mostrar_ranking

def iniciar_menu_inicio()-> bool:
    pygame.init()
    pygame.mixer.init()
    musica = cargar_sonidos("inicio")
    musica["musica_fondo"].play(-1)
    pantalla = pygame.display.set_mode([ANCHO_PANTALLA,ALTO_PANTALLA])
    caption = pygame.display.set_caption("Juego")
    diccionario_imagenes = cargar_imagenes_inicio("menu")
    rect_fondo = diccionario_imagenes["fondo"].get_rect()
    corriendo = True
    rect_boton_jugar = pygame.Rect(54,73,290,82)
    rect_boton_ranking = pygame.Rect(54,191,290,82)

    while corriendo:
        pantalla.blit(diccionario_imagenes["fondo"],rect_fondo)

        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                corriendo = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                posicion_click = list(evento.pos)
                if rect_boton_jugar.collidepoint(posicion_click):
                    iniciar_menu_niveles()
                elif rect_boton_ranking.collidepoint(posicion_click):
                    mostrar_ranking()

        pygame.display.flip()
