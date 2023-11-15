from funciones_guardar_datos import *
import pygame
from funciones_carga import cargar_imagenes_inicio
from funciones_carga import cargar_textos
from constantes import *

def guardar_puntaje(puntaje:int):
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO_PANTALLA,ALTO_PANTALLA])
    caption = pygame.display.set_caption("Juego")
    diccionario_imagenes = cargar_imagenes_inicio("guardado")
    rect_fondo = diccionario_imagenes["fondo"].get_rect()
    rect_boton_continuar = pygame.Rect((776,541),(282,61))
    corriendo = True
    escribiendo = False
    texto_ingresado = ""
    texto_finalizado = False

    while corriendo:
        lista_teclas = pygame.key.get_pressed()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                posicion_click = list(evento.pos)
                if rect_boton_continuar.collidepoint(posicion_click):
                    texto_finalizado = True
            if True in lista_teclas:
                if lista_teclas[pygame.K_BACKSPACE]:
                    texto_ingresado = texto_ingresado[:-1]
                elif len(texto_ingresado.replace(' ','')) < 9:
                    try:
                        texto_ingresado += f"{evento.unicode} "
                    except:
                        pass
    
        pantalla.blit(diccionario_imagenes["fondo"],rect_fondo)
        texto_usuario = cargar_textos(str(texto_ingresado),TAMAÑO_TEXTO_USUARIO)
        pantalla.blit(texto_usuario,(284,355))
        
        if texto_finalizado:
            if len(texto_ingresado) > 0:
                crear_tabla_puntajes()
                insertar_datos(texto_ingresado.replace(' ',''),str(puntaje))
            corriendo = False

        pygame.display.flip()
