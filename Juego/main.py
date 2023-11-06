import pygame
import sys
from constantes import *
from scripts.personajes import Fisicas_personajes
from scripts.carga_archivos import *
from scripts.comidas import Comidas
from scripts.objetos import Objetos
from scripts.mesas import Mesa
from funciones_colisiones import *
from funciones_carga import *
from funciones_lista_pedidos import *
class Juego:
    def __init__ (self):
        
        pygame.init()
        self.pantalla = pygame.display.set_mode([ANCHO_PANTALLA,ALTO_PANTALLA])
        self.timer = pygame.time.Clock() #Tiempo
        pygame.display.set_caption("Juego")
        self.corriendo = True
        self.diccionario_imagenes = cargar_imagenes_inicio()
        self.jugador = Fisicas_personajes(Juego,"jugador",POSICION_INICIO,self.diccionario_imagenes["personaje_abajo"])
        self.mesa = Mesa([4,5], self.diccionario_imagenes["mesa"])
        self.mesa_dos = Mesa([4,2],self.diccionario_imagenes["mesa"])
        self.mesa_tres = Mesa([1,3],self.diccionario_imagenes["mesa"])
        self.rect_fondo = self.diccionario_imagenes["fondo"].get_rect()
        self.rect_barra = self.diccionario_imagenes["barra"].get_rect(),
        self.rect_fuera_pantalla = pygame.Rect((-200,-200),(100, 100))
        self.tiempo_total_juego = 0      


    def correr_juego(self):
        lista_mesas = []
        tiempo_desde_pedido = 0
        lista_mesas.append(self.mesa)
        lista_mesas.append(self.mesa_dos)
        lista_mesas.append(self.mesa_tres)
        comida_en_mesa = False
        colision_barra = False
        lista_pedidos = []
        toco_cliente = False
        toco_cliente_con_comida = False
        mantiene_presionado = False
        llevando_comida = False
        toco_comida_barra = False
        while self.corriendo:
            self.pantalla.blit(self.diccionario_imagenes["fondo"],self.rect_fondo)
            self.pantalla.blit(self.diccionario_imagenes["barra"],self.rect_barra)
            
            #Actualizamos tiempo
            self.tiempo_total_juego = pygame.time.get_ticks()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.corriendo = False
            lista_teclas = pygame.key.get_pressed()

            #Ajustar a frames
            self.timer.tick(60) 

            #Colisiones mesa
            lista_colisiones_mesas = []
            colisiones_mesas = comprobar_choque_lista_objetos(lista_mesas,self.jugador.rect_personaje)

            for mesa in lista_mesas:
                colision_mesa = comprobar_choque_losa(self.jugador.rect_personaje,mesa.rect_objeto_izquierda)
            
            #Colisiones_barra 
            colisiones_barra = comprobar_choque_losa_lista(self.jugador.rect_personaje,lista_pedidos)
            
            #Aca controles
            lista_teclas = pygame.key.get_pressed()
            if True in lista_teclas:
                if not mantiene_presionado:
                    mantiene_presionado = True
                    if lista_teclas[pygame.K_RIGHT]:
                        direccion = "derecha"
                        self.jugador.cambiar_imagen(self.diccionario_imagenes["personaje_dcha"])
                        if self.jugador.rect_personaje.x < LIMITE_DCHA_JUGADOR and not True in colisiones_mesas["izquierda"]:
                            movimiento[0] = MOVIMIENTO_JUGADOR_X
                    elif lista_teclas[pygame.K_LEFT]:
                        direccion = "izquierda"
                        self.jugador.cambiar_imagen(self.diccionario_imagenes["personaje_izq"])
                        if self.jugador.rect_personaje.x > LIMITE_IZQ_JUGADOR and not True in colisiones_mesas["derecha"]:
                            movimiento[0] = -MOVIMIENTO_JUGADOR_X
                    elif lista_teclas[pygame.K_DOWN]:
                        direccion = "abajo"
                        self.jugador.cambiar_imagen(self.diccionario_imagenes["personaje_abajo"])
                        if self.jugador.rect_personaje.y < LIMITE_ABAJO_JUGADOR and not True in colisiones_mesas["arriba"]:
                            movimiento[1] = MOVIMIENTO_JUGADOR_Y
                    elif lista_teclas[pygame.K_UP]:
                        direccion = "arriba"
                        self.jugador.cambiar_imagen(self.diccionario_imagenes["personaje_arriba"])
                        if self.jugador.rect_personaje.y > LIMITE_ARRIBA_JUGADOR and not True in colisiones_mesas["abajo"]:
                            movimiento[1] = -MOVIMIENTO_JUGADOR_Y
                    elif lista_teclas[pygame.K_z]:
                        for mesa in lista_mesas:
                            colisiones_mesa = comprobar_colisiones_objeto(mesa,self.jugador.rect_personaje)
                            if colisiones_mesa["choco_objeto"]:
                                mesa.actualizar_colision_mesa(True)
                            if mesa.pedido_tomado:
                                if True in colisiones_barra and comprobar_choque_losa(self.jugador.rect_personaje,mesa.pedido.rect_objeto_izquierda):
                                    mesa.pedido.actualizar_colision_comida(True)
            else:
                mantiene_presionado = False
                movimiento = [0,0]

            #Bliteamos mesas
            for mesa in lista_mesas:
                mesa.blitear_objeto(self.pantalla)
            
            #determinar posiciones y bliteamos comidas
            for mesa in lista_mesas:
                if not mesa.pedido_tomado and mesa.colision:
                    pedido = self.hamburguesa_base = Comidas(self.diccionario_imagenes["hamburguesa"],self.jugador.rect_personaje,mesa.rect_objeto)
                    mesa.determinar_pedido_mesa(pedido)
                    lista_pedidos = manejar_lista_pedidos(lista_pedidos,"agregar",pedido)
                    for i in range (len(lista_pedidos)):
                        mesa.pedido.determinar_posicion_comida("barra",i,self.pantalla)
                    mesa.actualizar_pedido_tomado(True)
                    #Actualizamos tiempo
                    mesa.pedido.actualizar_tiempo_preparacion(pygame.time.get_ticks())
                if mesa.pedido_tomado and not mesa.finalizada:
                    if mesa.pedido.lugar == "barra" and mesa.pedido.colision:
                        mesa.pedido.determinar_posicion_comida("personaje",i,self.pantalla)
                    if mesa.colision and mesa.pedido.colision:
                        mesa.pedido.actualizar_colision_comida(False)
                        mesa.pedido.determinar_posicion_comida("mesa",i,self.pantalla)
                        mesa.actualizar_mesa_finalizada(True)
                    #Actualizamos tiempo
                    mesa.pedido.actualizar_tiempo_siendo_comida(pygame.time.get_ticks())
                mesa.actualizar_colision_mesa(False)

            #Vemos si terminaron de comer:
            for mesa in lista_mesas:
                if mesa.pedido_tomado:
                    mesa.pedido.determinar_comida_terminada(self.tiempo_total_juego)
                    if mesa.pedido.comida_terminada:
                        lista_pedidos.pop()
                        mesa.vaciar_mesa()

            #Bliteamos imagen jugador
            self.jugador.actualizar((movimiento[0],movimiento[1]))
            self.jugador.blitear_personaje(self.pantalla)
            movimiento = [0,0]

            #Bliteamos comida
            for mesa in lista_mesas:
                if mesa.pedido_tomado:
                    mesa.pedido.determinar_pedido_preparado(self.tiempo_total_juego)
                    if mesa.pedido.pedido_preparado:
                        mesa.pedido.blitear_comida(self.pantalla)

            pygame.display.update()

        #sys.exit()despues probar si es necesario
        pygame.quit()

Juego().correr_juego()