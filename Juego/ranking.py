import pygame
from constantes import *
from funciones_guardar_datos import listar_datos_buscados
from funciones_carga import cargar_imagenes_inicio
from funciones_carga import cargar_textos

def mostrar_ranking():
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO_PANTALLA,ALTO_PANTALLA])
    caption = pygame.display.set_caption("Juego")
    diccionario_imagenes = cargar_imagenes_inicio("ranking")
    rect_fondo = diccionario_imagenes["fondo"].get_rect()
    corriendo = True
    rect_boton_regresar = pygame.Rect(1083,506,55,66)
    jugar = False
    lista_ranking = listar_datos_buscados(3)
    puestos_x = 293
    primer_puesto_y = 258
    segundo_puesto_y = primer_puesto_y + 80
    tercer_puesto_y = segundo_puesto_y + 80
    texto_puntaje_1 = cargar_textos(str(lista_ranking[0]))
    texto_puntaje_2 = cargar_textos(str(lista_ranking[1]))
    texto_puntaje_3 = cargar_textos(str(lista_ranking[2]))

    while corriendo:
        pantalla.blit(diccionario_imagenes["fondo"],rect_fondo)

        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                corriendo = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                posicion_click = list(evento.pos)
                if rect_boton_regresar.collidepoint(posicion_click):
                    corriendo = False
        
        pantalla.blit(texto_puntaje_1,(puestos_x,primer_puesto_y))
        pantalla.blit(texto_puntaje_2,(puestos_x,segundo_puesto_y))
        pantalla.blit(texto_puntaje_3,(puestos_x,tercer_puesto_y))  

        pygame.display.flip()