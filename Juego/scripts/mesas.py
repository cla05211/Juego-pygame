from scripts.objetos import Objetos
from scripts.constantes import *
import pygame

class Mesa(Objetos):
    def __init__ (self, losa_apoyo: tuple, imagen):
        super().__init__(losa_apoyo, imagen)
        self.vacia = True
        self.ocupada = False
        self.tiempo_vacia = 0
        self.pedido_tomado = False
        self.finalizada = False
        self.colision = False
        self.pedido = None
        self.cliente = None
        self.dinero = None

    def actualizar_pedido_tomado (self,mesa_pedido_tomado:bool):
        self.pedido_tomado = mesa_pedido_tomado
    
    def actualizar_mesa_finalizada (self,mesa_finalizada:bool):
        self.finalizada = mesa_finalizada

    def actualizar_colision_mesa (self,colision_mesa:bool):
        self.colision = colision_mesa
    
    def determinar_pedido_mesa (self, pedido):
        self.pedido = pedido
    
    def actualizar_tiempo_vacia(self,tiempo_vacia:int):
        self.tiempo_vacia = tiempo_vacia
    
    def llenar_mesa(self, tiempo_juego:int,cliente):
        if (tiempo_juego - self.tiempo_vacia) > TIEMPO_LIMITE_MESA_VACIA and self.dinero == None:
            self.cliente = cliente
            self.ocupada = True

    def vaciar_mesa (self):
        self.pedido_tomado = False
        self.finalizada = False
        self.colision = False
        self.pedido = None
        self.cliente = None
        self.vacia = True
        self.ocupada = False