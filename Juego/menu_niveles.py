import pygame
from funciones_carga import cargar_imagenes_inicio
from constantes import *
from scripts.carteles import Carteles
from cargar_niveles import cargar_niveles

def iniciar_menu_niveles():
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO_PANTALLA,ALTO_PANTALLA])
    caption = pygame.display.set_caption("Juego")
    diccionario_imagenes = cargar_imagenes_inicio("menu_niveles")
    rect_fondo = diccionario_imagenes["fondo"].get_rect()
    corriendo = True
    boton_nivel_uno = Carteles(diccionario_imagenes["nivel_uno"],diccionario_imagenes["nivel_uno_bloqueado"])
    boton_nivel_dos = Carteles(diccionario_imagenes["nivel_dos"],diccionario_imagenes["nivel_dos_bloqueado"])
    boton_nivel_tres = Carteles(diccionario_imagenes["nivel_tres"],diccionario_imagenes["nivel_tres_bloqueado"])
    lista_botones = [boton_nivel_uno,boton_nivel_dos,boton_nivel_tres]
    nivel_uno_completado = False
    nivel_dos_completado = False
    nivel_tres_completado = False

    while corriendo:
        pantalla.blit(diccionario_imagenes["fondo"],rect_fondo)

        if not nivel_uno_completado:
            boton_nivel_dos.bloquear_cartel()
        else:
            boton_nivel_dos.desbloquear_cartel()
        if not nivel_dos_completado:
            boton_nivel_tres.bloquear_cartel()
        else:
            boton_nivel_tres.desbloquear_cartel()

        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                corriendo = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                posicion_click = list(evento.pos)
                if boton_nivel_uno.rect.collidepoint(posicion_click):
                    nivel_uno_completado = cargar_niveles(1)
                    print(nivel_uno_completado)
                elif boton_nivel_dos.rect.collidepoint(posicion_click):
                    nivel_dos_completado = cargar_niveles(2)
                elif boton_nivel_tres.rect.collidepoint(posicion_click):
                    nivel_tres_completado = cargar_niveles(3)

        #Bliteamos botones
        for i in range (len(lista_botones)):
            lista_botones[i].determinar_posicion(i+1)
            lista_botones[i].blitear_cartel(pantalla)
        
        pygame.display.flip()