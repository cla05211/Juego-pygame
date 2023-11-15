import pygame
from funciones_carga import cargar_imagenes_inicio
from constantes import *
from funciones_carga import cargar_textos
from pantalla_guardar_puntaje import guardar_puntaje
from funciones_guardar_datos import *

def mostrar_pantalla_final_juego(victoria_derrota:str,dinero_conseguido:int,dinero_necesario:int,dinero_total:int)-> None:
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO_PANTALLA,ALTO_PANTALLA])
    diccionario_imagenes = cargar_imagenes_inicio("final_juego")
    rect_fondo = diccionario_imagenes["nivel_superado"].get_rect()
    rect_boton_continuar = pygame.Rect((776,541),(282,61))
    rect_boton_puntaje = pygame.Rect((50,541),(460,61))
    texto_dinero_conseguido = cargar_textos(f"{str(dinero_conseguido)}")
    texto_dinero_necesario = cargar_textos(f"{str(dinero_necesario)}")
    texto_dinero_total = cargar_textos(f"{str(dinero_conseguido - dinero_necesario)}")
    corriendo = True

    while corriendo:
        match victoria_derrota:
            case "victoria":
                pantalla.blit(diccionario_imagenes["nivel_superado"],rect_fondo)
            case "derrota":
                pantalla.blit(diccionario_imagenes["nivel_no_superado"],rect_fondo)
        
        #Bliteamos texto:
        pantalla.blit(texto_dinero_conseguido,(655,278))
        pantalla.blit(texto_dinero_necesario,(623,366))
        pantalla.blit(texto_dinero_total,(300,461))

        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                corriendo = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                posicion_click = list(evento.pos)
                if rect_boton_continuar.collidepoint(posicion_click):
                    corriendo = False
                if rect_boton_puntaje.collidepoint(posicion_click):
                    guardar_puntaje(dinero_conseguido)
        pygame.display.flip()

