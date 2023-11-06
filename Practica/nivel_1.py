import pygame
import sys
from constantes import *
from scripts.jugador import Jugador
from scripts.carga_archivos import *
from scripts.comidas import Comidas
from scripts.objetos import Objetos
from scripts.mesas import Mesa
from funciones_colisiones import *
from funciones_carga import *
from funciones_lista_pedidos import *
from scripts.cliente import Cliente
import random

class Juego:
    def __init__ (self):
        
        pygame.init()
        self.pantalla = pygame.display.set_mode([ANCHO_PANTALLA,ALTO_PANTALLA])
        self.timer = pygame.time.Clock() #Tiempo
        pygame.display.set_caption("Juego")
        self_duracion_nivel = 30000
        self.corriendo = True
        self.diccionario_imagenes = cargar_imagenes_inicio()
        self.jugador = Jugador(Juego,"jugador",POSICION_INICIO,self.diccionario_imagenes["personaje_abajo"])
        self.lista_mesas = cargar_lista_mesas([[2,1],[6,1],[2,4],[6,4],[2,7],[6,7]],self.diccionario_imagenes)
        self.rect_fondo = self.diccionario_imagenes["fondo"].get_rect()
        self.rect_barra = self.diccionario_imagenes["barra"].get_rect(),
        self.rect_fuera_pantalla = pygame.Rect((-200,-200),(100, 100))
        self.tiempo_total_juego = 0      
        self.lista_imagenes_comidas = cargar_imagenes_comidas_disponibles(self.diccionario_imagenes)

    def correr_juego(self):
        lista_mesas = self.lista_mesas
        tiempo_desde_pedido = 0
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

            #Llenamos mesas:
            for mesa in lista_mesas:
                if mesa.vacia == True:
                    mesa.vacia = False
                    mesa.actualizar_tiempo_vacia(pygame.time.get_ticks())
                mesa.llenar_mesa(self.tiempo_total_juego,Cliente(self.diccionario_imagenes["cliente"],self.diccionario_imagenes["cliente_enojado"],mesa.rect_objeto))

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.corriendo = False
            lista_teclas = pygame.key.get_pressed()

            #Ajustar a frames
            self.timer.tick(60) 

            #Colisiones mesa
            lista_colisiones_mesas = []
            colisiones_mesas = comprobar_choque_lista_objetos(lista_mesas,self.jugador.rect_personaje)
            
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
                    #Interacciones (tecla Z)        
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

            #Bliteamos Cliente
            for mesa in lista_mesas:
                if mesa.cliente != None:
                    mesa.cliente.blitear_cliente(self.pantalla)

            #Bliteamos mesas
            for mesa in lista_mesas:
                mesa.blitear_objeto(self.pantalla)
            
            #determinar posiciones y bliteamos comidas
            for mesa in lista_mesas:
                if mesa.cliente != None:
                    if not mesa.pedido_tomado and mesa.colision:
                        mesa.cliente.actualizar_tiempo_espera_antes_de_pedir(pygame.time.get_ticks())
                        imagen_pedido = (random.choice(self.lista_imagenes_comidas))
                        pedido = Comidas(imagen_pedido.copy(),self.jugador.rect_personaje,mesa.rect_objeto)
                        mesa.determinar_pedido_mesa(pedido)
                        mesa.pedido.rect_mesa = mesa.rect_objeto
                        lista_pedidos = manejar_lista_pedidos(lista_pedidos,"agregar",pedido)
                        for i in range (len(lista_pedidos)):
                            mesa.pedido.determinar_posicion_comida("barra",i,self.pantalla)
                        mesa.actualizar_pedido_tomado(True)
                        #Actualizamos tiempo
                        mesa.pedido.actualizar_tiempo_preparacion(pygame.time.get_ticks())
                    if mesa.pedido_tomado and not mesa.finalizada:
                        mesa.cliente.actualizar_tiempo_espera_despues_de_pedir(pygame.time.get_ticks())
                        if mesa.pedido.lugar == "barra" and mesa.pedido.colision:
                            mesa.pedido.determinar_posicion_comida("personaje",i,self.pantalla)
                        if mesa.colision and mesa.pedido.colision:
                            mesa.pedido.actualizar_colision_comida(False)
                            mesa.pedido.determinar_posicion_comida("mesa",i,self.pantalla)
                            mesa.actualizar_mesa_finalizada(True)
                            lista_pedidos.pop()
                        #Actualizamos tiempo
                        mesa.pedido.actualizar_tiempo_siendo_comida(pygame.time.get_ticks())
                mesa.actualizar_colision_mesa(False)

            #Vemos que onda el Cliente:
            for mesa in lista_mesas:
                if mesa.ocupada:
                    mesa.cliente.actualizar_paciencia_cliente(self.tiempo_total_juego)

            #Vemos si terminaron de comer:
            for mesa in lista_mesas:
                if mesa.ocupada:
                    if mesa.cliente.animo == "ira":
                        mesa.vaciar_mesa()
                if mesa.pedido_tomado:
                    mesa.pedido.determinar_comida_terminada(self.tiempo_total_juego)
                    if mesa.pedido.comida_terminada:
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

        primer_ingreso = False

        #sys.exit()despues probar si es necesario
        pygame.quit()

Juego().correr_juego()