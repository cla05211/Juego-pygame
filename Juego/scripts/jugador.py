import pygame
from scripts.constantes import *

class Jugador:
    def __init__ (self, juego, tipo_personaje: str, posicion: tuple, imagen):
        self.dinero = 0
        self.juego = juego
        self.tipo = tipo_personaje
        self.posicion = list(posicion)
        self.imagen_personaje = imagen
        self.velocidad = [0,0]
        self.rect_personaje = pygame.Rect((posicion[0],posicion[1]),(MEDIDAS_LOSA[0]-3, MEDIDAS_LOSA[1]-3))
        self.rect_personaje_bliteo = self.imagen_personaje.get_rect()
        self.rect_personaje_bliteo.x = self.rect_personaje.x
        self.rect_personaje_bliteo.y = self.rect_personaje.y

    def sumar_dinero (cantidad_ganada:int):
        self.dinero += cantidad_ganada

    def actualizar (self, movimiento = (0,0)):
        movimiento_frame = movimiento[0] + self.velocidad[0], movimiento[1] + self.velocidad[1]

        self.rect_personaje.x += movimiento_frame[0]
        self.rect_personaje.y += movimiento_frame[1]
        self.rect_personaje_bliteo.x = self.rect_personaje.x
        self.rect_personaje_bliteo.y = self.rect_personaje.y - 30

    def blitear_personaje (self,pantalla):
        pantalla.blit(self.imagen_personaje,self.rect_personaje_bliteo)

    def cambiar_imagen(self, imagen_cambio):
        self.imagen_personaje = imagen_cambio
    

