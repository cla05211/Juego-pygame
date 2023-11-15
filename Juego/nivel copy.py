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
from scripts.dinero import Dinero
import random
from modo_admin import activar_modo_admi
from scripts.burbuja_dialogo import Burbuja
from pantallas_final_juego import mostrar_pantalla_final_juego

class Nivel:
    def __init__ (self,duracion_nivel:int,objetivo_dinero:int,lista_mesas:list,rutas_comidas_adicionales:list,rutas_clientes_adicionales:list,porcentaje_paciencia_clientes):
        pygame.init()
        pygame.mixer.init()
        self.paciencia_clientes = porcentaje_paciencia_clientes
        self.pantalla = pygame.display.set_mode([ANCHO_PANTALLA,ALTO_PANTALLA])
        self.timer = pygame.time.Clock() #Tiempo
        self.caption = pygame.display.set_caption("Juego")
        self.diccionario_imagenes = cargar_imagenes_inicio("nivel")
        self.sonidos = cargar_sonidos()
        self.jugador = Jugador("jugador",POSICION_INICIO,self.diccionario_imagenes["personaje_abajo"])
        self.rect_fondo = self.diccionario_imagenes["fondo"].get_rect()
        self.rect_barra = self.diccionario_imagenes["barra"].get_rect(),
        self.rect_fuera_pantalla = pygame.Rect((-200,-200),(100, 100))
        self.duracion_nivel = duracion_nivel
        self.corriendo = True
        self.lista_mesas = cargar_lista_mesas(lista_mesas,self.diccionario_imagenes)
        self.tiempo_total_juego = 0
        self.tiempo_total_nivel = 0      
        self.lista_comidas_disponibles = ["bebida_celeste","bebida_rosa","bebida_verde"]
        self.lista_clientes_disponibles = cargar_imagenes_clientes_disponibles(rutas_clientes_adicionales)
        self.objetivo_dinero = objetivo_dinero
        self.dinero_ahorrado = 0

    def correr_nivel(self):
        primer_ingreso = True
        nivel_completado = False
        pedido_equivocado = False
        lista_mesas = self.lista_mesas
        tiempo_desde_pedido = 0
        comida_en_mesa = False
        colision_barra = False
        diccionario_pedidos = {}
        toco_cliente = False
        toco_cliente_con_comida = False
        mantiene_presionado = False
        llevando_comida = False
        toco_comida_barra = False
        
        while self.corriendo:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.corriendo = False
            lista_teclas = pygame.key.get_pressed()

            self.pantalla.blit(self.diccionario_imagenes["fondo"],self.rect_fondo)
            
            #Actualizamos tiempo
            self.tiempo_total_juego = pygame.time.get_ticks()
            if primer_ingreso:
                momento_comienzo_nivel = self.tiempo_total_juego
            self.tiempo_total_nivel = self.tiempo_total_juego - momento_comienzo_nivel

            nro_mesa_actual = 0
            #Llenamos mesas:
            for mesa in lista_mesas:
                if mesa.vacia == True and mesa.dinero == None:
                    mesa.vacia = False
                    #Aca empezamos a contar
                    mesa.actualizar_tiempo_vacia(pygame.time.get_ticks())
                #Aca si se cumple la condicion de tiempo la mesa se ocupa
                if not mesa.ocupada:
                    imagenes_cliente = (random.choice(self.lista_clientes_disponibles))
                    mesa.llenar_mesa(self.tiempo_total_juego,Cliente(imagenes_cliente,mesa.rect_objeto,self.paciencia_clientes),nro_mesa_actual)
                nro_mesa_actual += 1

            #Ajustar a frames
            self.timer.tick(60) 

            #Colisiones mesa
            lista_colisiones_mesas = []
            colisiones_mesas = comprobar_choque_lista_objetos(lista_mesas,self.jugador.rect_personaje)

            #Colisiones_barra 
            colisiones_barra = comprobar_choque_losa_lista(self.jugador.rect_personaje,list(diccionario_pedidos.values()))
            
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
                            if mesa.colision and mesa.ocupada and mesa.pedido == None:
                                mesa.cliente.reinciar_paciencia_cliente(self.tiempo_total_juego)
                            if mesa.colision and mesa.ocupada and mesa.pedido != None:
                                if mesa.pedido.lugar == "personaje":
                                    mesa.cliente.reinciar_paciencia_cliente(self.tiempo_total_juego)
                            elif mesa.colision and mesa.dinero != None:
                                self.sonidos["sonido_dinero"].play()
                                self.dinero_ahorrado += mesa.dinero.cantidad
                                mesa.dinero = None
                            if mesa.pedido_tomado:
                                if True in colisiones_barra and comprobar_choque_losa(self.jugador.rect_personaje,mesa.pedido.rect_objeto_izquierda):
                                    mesa.pedido.actualizar_colision_comida(True)
            else:
                mantiene_presionado = False
                movimiento = [0,0]

            #Vemos que onda el Cliente:
            for mesa in lista_mesas:
                if mesa.ocupada:
                    if mesa.cliente.inicio_tiempo_espera:
                        mesa.cliente.actualizar_inicio_tiempo_espera(False)
                        #Arrancamos a contar paciencia cliente
                        mesa.cliente.actualizar_tiempo_espera(pygame.time.get_ticks())
                        mesa.cliente.burbuja_dialogo = Burbuja(self.diccionario_imagenes,mesa.cliente.rect_bliteo,self.diccionario_imagenes["burbuja_esperando"])#ESTO HAY QUE CHEQUEARLOOOOO
                    if mesa.finalizada:
                        mesa.cliente.revisar_paciencia_cliente(self.tiempo_total_juego)
                    else:
                        mesa.cliente.revisar_paciencia_cliente(self.tiempo_total_juego)

            #Bliteamos imagen jugador
            self.jugador.actualizar((movimiento[0],movimiento[1]))
            self.jugador.blitear_personaje(self.pantalla)
            movimiento = [0,0]

            #Bliteamos Cliente
            for mesa in lista_mesas:
                if mesa.ocupada:
                    mesa.cliente.cambiar_imagen_segun_animo()
                    mesa.cliente.blitear_cliente(self.pantalla)

            #Bliteamos mesas
            for mesa in lista_mesas:
                mesa.blitear_objeto(self.pantalla)
            
            #determinar posiciones y bliteamos comidas
            for mesa in lista_mesas:
                if mesa.cliente != None:
                    if not mesa.pedido_tomado and mesa.colision:
                        tipo_pedido = (random.choice(self.lista_comidas_disponibles))
                        mesa.cliente.atendido = True
                        pedido = Comidas(tipo_pedido,self.jugador.rect_personaje,mesa.rect_objeto)
                        mesa.determinar_pedido_mesa(pedido)
                        mesa.pedido.rect_mesa = mesa.rect_objeto
                        mesa.pedido.numero_pedido = len(diccionario_pedidos)
                        diccionario_pedidos = manejar_diccionario_pedidos(diccionario_pedidos,mesa.pedido.numero_pedido,mesa.pedido,"agregar")
                        mesa.pedido.determinar_posicion_comida("barra",self.pantalla)
                        mesa.actualizar_pedido_tomado(True)
                        #Actualizamos tiempo
                        mesa.pedido.actualizar_tiempo_preparacion(pygame.time.get_ticks())
                    if mesa.pedido_tomado and not mesa.finalizada:
                        if mesa.pedido.lugar == "barra" and mesa.pedido.colision and self.jugador.platos_cargados < 2:
                            self.jugador.cargar_plato(True,mesa.pedido.comida_siendo_llevada,mesa.pedido.tipo_comida)
                            mesa.pedido.comida_siendo_llevada = True
                        if mesa.pedido.comida_siendo_llevada:
                            mesa.pedido.determinar_posicion_comida("personaje",self.pantalla)
                        else:
                            mesa.pedido.colision = False
                        if mesa.colision and mesa.pedido.colision:
                            self.jugador.tipos_pedidos_llevados.remove(mesa.pedido.tipo_comida)
                            self.jugador.descargar_plato(False,mesa.pedido.comida_siendo_llevada,mesa.pedido.tipo_comida)
                            mesa.pedido.determinar_posicion_comida("mesa",self.pantalla)
                            self.sonidos["sonido_plato"].play()
                            mesa.pedido.actualizar_colision_comida(False)
                            mesa.actualizar_mesa_finalizada(True)
                            mesa.cliente.cambiar_imagen_a_feliz()
                            mesa.cliente.determinar_propina()
                            diccionario_pedidos = manejar_diccionario_pedidos(diccionario_pedidos,mesa.pedido.numero_pedido,mesa.pedido,"eliminar")#ACAAAAAAAAAAAAAAAAAAAAAA
                        #Actualizamos tiempo
                        mesa.pedido.actualizar_tiempo_siendo_comida(pygame.time.get_ticks())
                mesa.actualizar_colision_mesa(False)

            #Vemos si terminaron de comer:
            for mesa in lista_mesas:
                if mesa.ocupada:
                    if mesa.cliente.animo == "ira":
                        mesa.vaciar_mesa()
                if mesa.pedido_tomado:
                    mesa.pedido.determinar_comida_terminada(self.tiempo_total_juego)
                    if mesa.pedido.comida_terminada:
                        dinero = Dinero(mesa.losa_apoyo,self.diccionario_imagenes["billetes"])
                        dinero.cantidad = mesa.cliente.propina
                        mesa.dinero = dinero
                        mesa.vaciar_mesa()

            #Bliteamos billetes
            for mesa in lista_mesas:
                if mesa.dinero != None:
                    mesa.dinero.blitear_objeto(self.pantalla)

            #Blitemos texto dinero
            texto_dinero = cargar_textos(str(self.dinero_ahorrado))
            self.pantalla.blit(texto_dinero,(85,21))

            #Bliteamos burbuja
            for mesa in lista_mesas:
                if mesa.cliente != None:
                    mesa.cliente.burbuja_dialogo.blitear_imagen(self.pantalla)
                    if mesa.pedido != None and not mesa.cliente.burbuja_dialogo.pedido_equivocado:
                        match mesa.pedido.lugar:
                            case "barra" | "personaje":
                                pedido_equivocado = False
                                mesa.cliente.burbuja_dialogo.cambiar_imagen(self.diccionario_imagenes["burbuja_dialogo_vacia"])
                                mesa.cliente.burbuja_dialogo.blitear_comida(mesa.pedido.imagen,self.pantalla)
                            case "mesa":
                                mesa.cliente.burbuja_dialogo.cambiar_imagen(self.diccionario_imagenes["burbuja_corazon"])
                    else:
                        mesa.cliente.burbuja_dialogo.cambiar_imagen(self.diccionario_imagenes["burbuja_esperando"])

            #Bliteamos comida
            for mesa in lista_mesas:
                if mesa.pedido_tomado:
                    mesa.pedido.determinar_pedido_preparado(self.tiempo_total_juego)
                    if mesa.pedido.pedido_preparado:
                        mesa.pedido.blitear_comida(self.pantalla)

            #activar_modo_admi([self.jugador.rect_personaje,lista_mesas[0].rect_objeto_abajo,lista_mesas[0].rect_objeto_arriba,lista_mesas[0].rect_objeto_derecha,lista_mesas[0].rect_objeto_izquierda],self.pantalla)
            
            #Comprobamos si termino nivel:
            if (self.tiempo_total_nivel) > self.duracion_nivel:
                if self.dinero_ahorrado >= self.objetivo_dinero:
                    mostrar_pantalla_final_juego("victoria",self.dinero_ahorrado,self.objetivo_dinero,self.jugador.dinero)
                    nivel_completado = True
                else:
                    mostrar_pantalla_final_juego("derrota",self.dinero_ahorrado,self.objetivo_dinero,self.jugador.dinero)
                    nivel_completado = False
                self.corriendo = False
                break

            pygame.display.update()

            primer_ingreso = False
        return nivel_completado