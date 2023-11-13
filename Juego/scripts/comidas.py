import pygame
from scripts.constantes import *
from scripts.objetos import Objetos
from scripts.carga_archivos import cargar_imagenes_sin_ruta

class Comidas():
    def __init__ (self, tipo_comida, rect_personaje,rect_mesa):
        self.tiempo_desde_pedido = 0
        self.numero_pedido = 0
        self.tiempo_comiendo = 0
        self.comida_terminada = False
        self.pedido_preparado = False
        self.tipo_comida = tipo_comida
        self.imagen = cargar_imagenes_sin_ruta("comida",tipo_comida,1)
        self.colision = False
        self.lugar = "fuera de pantalla"
        self.rect_personaje = rect_personaje
        self.rect_mesa = rect_mesa
        self.rect_comida = pygame.Rect((-200,-200),(MEDIDAS_LOSA[0],MEDIDAS_LOSA[1]))
        self.rect_comida = self.imagen.get_rect()
        self.rect_bliteo = self.imagen.get_rect()
        self.rect_bliteo.x = self.rect_comida.x
        self.rect_bliteo.y = self.rect_comida.y
        self.rect_objeto_izquierda = pygame.Rect((self.rect_bliteo.x - MEDIDAS_LOSA[0] + 5,self.rect_bliteo.y),(self.rect_bliteo.width - 5, self.rect_bliteo.height - 15))
        self.comida_siendo_llevada = False

    def actualizar_colision_comida(self, colision: bool):
        self.colision = colision

        def actualizar_imagen (self,imagen):
            self.imagen= imagen

    def determinar_posicion_comida(self, posicion_bliteo:str,pantalla):
        match posicion_bliteo:
            case "barra":
                if self.numero_pedido < 7:
                    self.lugar = "barra"
                    self.rect_comida.x = BARRA_Y
                    self.rect_comida.y = (ESPACIO_ARRIBA + MEDIDAS_LOSA[1] * self.numero_pedido)
            case "mesa":
                self.lugar = "mesa"
                self.rect_comida.x = self.rect_mesa.x -2
                self.rect_comida.y = self.rect_mesa.y - 20
            case "personaje":
                
                self.rect_comida.x = self.rect_personaje.x
                self.rect_comida.y = self.rect_personaje.y
        self.rect_bliteo.x  = self.rect_comida.x
        self.rect_bliteo.y  = self.rect_comida.y
        self.rect_objeto_izquierda = pygame.Rect((self.rect_bliteo.x - MEDIDAS_LOSA[0],self.rect_bliteo.y),(self.rect_bliteo.width, self.rect_bliteo.height))

    def actualizar_tiempo_preparacion(self,tiempo_pedido:int):
        self.tiempo_desde_pedido = tiempo_pedido

    def determinar_pedido_preparado(self, tiempo_juego:int):
        if (tiempo_juego - self.tiempo_desde_pedido) > TIEMPO_PREPARACION_PEDIDOS:
            self.pedido_preparado = True

    def actualizar_tiempo_siendo_comida(self,tiempo_siendo_comido:int):
        self.tiempo_comiendo = tiempo_siendo_comido

    def determinar_comida_terminada(self, tiempo_juego:int):
        if (tiempo_juego - self.tiempo_comiendo) > TIEMPO_COMER_COMIDA:
            self.comida_terminada = True

    def blitear_comida (self,pantalla):
        pantalla.blit(self.imagen,self.rect_bliteo)

