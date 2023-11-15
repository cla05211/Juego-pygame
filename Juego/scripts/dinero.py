from scripts.objetos import Objetos
from scripts.constantes import *
import pygame

class Dinero(Objetos):
    def __init__ (self, losa_apoyo: tuple, imagen):
        super().__init__(losa_apoyo, imagen)
        self.cantidad = 0
        self.rect_objeto.y = self.rect_objeto.y - 10 #Acomodamos bliteo
    
    def juntar_dinero (self,dinero_ahorrado_nivel:int):
        dinero_ahorrado_nivel += self.cantidad