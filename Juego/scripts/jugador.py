import pygame
from scripts.constantes import *

class Jugador:
    def __init__ (self, tipo_personaje: str, posicion: tuple, imagen):
        self.dinero = 0
        self.tipo = tipo_personaje
        self.posicion = list(posicion)
        self.imagen_personaje = imagen
        self.velocidad = [0,0]
        self.rect_personaje = pygame.Rect((posicion[0] ,posicion[1] + 10),(MEDIDAS_LOSA[0] - 5, MEDIDAS_LOSA[1]- ALTO_CABEZA_JUGADOR))
        self.rect_personaje_bliteo = self.imagen_personaje.get_rect()
        self.rect_personaje_bliteo.x = self.rect_personaje.x 
        self.rect_personaje_bliteo.y = self.rect_personaje.y 
        self.plato_uno_cargado = False
        self.plato_dos_cargado = False
        self.platos_cargados = 0
        self.tipos_pedidos_llevados = []

    def cargar_plato(self,cargar:bool,comida_siendo_llevada:bool,tipo_comida:str):
        if not comida_siendo_llevada:
            if cargar != self.plato_uno_cargado:
                self.platos_cargados += 1
                self.tipos_pedidos_llevados.append(tipo_comida)
                self.plato_uno_cargado = True
            elif cargar != self.plato_dos_cargado:
                self.platos_cargados += 1
                self.tipos_pedidos_llevados.append(tipo_comida)
                self.plato_dos_cargado = True
        
    def descargar_plato(self,cargar:bool,comida_siendo_llevada:bool,tipo_comida:str):
        if comida_siendo_llevada: #Evitamos que entre dos veces por mesa
            if cargar != self.plato_uno_cargado:
                self.platos_cargados -= 1
                self.plato_uno_cargado = False
            elif cargar != self.plato_dos_cargado:
                self.platos_cargados -= 1
                self.plato_dos_cargado = False

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
    

