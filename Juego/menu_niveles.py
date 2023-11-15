import pygame
from funciones_carga import cargar_imagenes_inicio
from constantes import *
from scripts.carteles import Carteles
from cargar_niveles import cargar_niveles
from funciones_guardar_datos import*

def iniciar_menu_niveles()->None:
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO_PANTALLA,ALTO_PANTALLA])
    caption = pygame.display.set_caption("Juego")
    diccionario_imagenes = cargar_imagenes_inicio("menu_niveles")
    rect_fondo = diccionario_imagenes["fondo"].get_rect()
    rect_boton_regresar = pygame.Rect(1185,11,82,88)
    corriendo = True
    boton_nivel_uno = Carteles(diccionario_imagenes["nivel_uno"],diccionario_imagenes["nivel_uno_bloqueado"])
    boton_nivel_dos = Carteles(diccionario_imagenes["nivel_dos"],diccionario_imagenes["nivel_dos_bloqueado"])
    boton_nivel_tres = Carteles(diccionario_imagenes["nivel_tres"],diccionario_imagenes["nivel_tres_bloqueado"])
    lista_botones = [boton_nivel_uno,boton_nivel_dos,boton_nivel_tres]
    """     crear_tabla_niveles()
    nivel_actual = obtener_ultimo_dato()
    if nivel_actual == 2:
        nivel_uno_completado = True
    elif nivel_actual == 3:
        nivel_uno_completado = True
        nivel_dos_completado = True
    else:"""
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
                    if nivel_uno_completado:
                        cargar_niveles(1)
                    else:
                        nivel_uno_completado = cargar_niveles(1)
                        """ if nivel_uno_completado:
                            insertar_datos_niveles(2) """

                elif boton_nivel_dos.rect.collidepoint(posicion_click):
                    if nivel_dos_completado:
                        cargar_niveles(2)
                    else:
                        nivel_dos_completado = cargar_niveles(2)
                        """ if nivel_uno_completado:
                            insertar_datos_niveles(3) """
                elif boton_nivel_tres.rect.collidepoint(posicion_click):
                    if nivel_tres_completado:
                        cargar_niveles(3)
                    else:
                        nivel_tres_completado = cargar_niveles(3)
                elif rect_boton_regresar.collidepoint(posicion_click):
                    corriendo = False

        #Bliteamos botones
        for i in range (len(lista_botones)):
            lista_botones[i].determinar_posicion(i+1)
            lista_botones[i].blitear_cartel(pantalla)

        pygame.display.flip()

        niveles_completos = {"nivel uno": nivel_uno_completado,"nivel dos":nivel_dos_completado, "nivel tres":nivel_tres_completado}