from scripts.mesas import Mesa
import pygame
from scripts.constantes import *

class Cliente():
    def __init__ (self,imagen,imagen_cliente_enojado,rect_mesa):
        self.animo = "feliz"
        self.propina = 100
        self.tiempo_espera_antes_de_pedir = 0
        self.tiempo_espera_despues_de_pedir = 0
        self.imagen_enojado = imagen_cliente_enojado
        self.imagen = imagen
        self.rect_mesa = rect_mesa
        self.rect_bliteo = self.imagen.get_rect()
        self.rect_bliteo.x = self.rect_mesa.x 
        self.rect_bliteo.y = self.rect_mesa.y - 15 
    
    def blitear_cliente (self,pantalla):
        pantalla.blit(self.imagen,self.rect_bliteo)

    def actualizar_tiempo_espera_antes_de_pedir(self,tiempo_espera:int):
        self.tiempo_espera_antes_de_pedir = tiempo_espera
    
    def actualizar_tiempo_espera_despues_de_pedir(self,tiempo_espera:int):
        self.tiempo_espera_despues_de_pedir = tiempo_espera

    def actualizar_paciencia_cliente(self, tiempo_juego:int):
        if (tiempo_juego - self.tiempo_espera_antes_de_pedir) > TIEMPO_ENOJO:
            self.propina -= 10
            self.animo = "ira"
            print(self.animo)
        elif (tiempo_juego - self.tiempo_espera_antes_de_pedir) > TIEMPO_NEUTRAL:
            self.propina -= 15
            self.animo = "enojo"
            self.imagen = self.imagen_enojado
            print(self.animo)
        elif (tiempo_juego - self.tiempo_espera_antes_de_pedir) > TIEMPO_FELICES:
            #self.imagen = imagen_feliz
            self.propina -= 20
            self.animo = "neutral"
            print(self.animo)
        else:
            self.animo = "feliz"
            print(self.animo)