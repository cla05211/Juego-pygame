from scripts.mesas import Mesa
import pygame
from scripts.constantes import *

class Cliente():
    def __init__ (self,imagen_cliente_feliz,imagen_cliente_enojado,rect_mesa):
        self.animo = "feliz"
        self.inicio_tiempo_espera = True
        self.propina = 100
        self.tiempo_espera = 0
        self.imagen_enojado = imagen_cliente_enojado
        self.imagen_feliz = imagen_cliente_feliz
        self.imagen_bliteo = self.imagen_feliz
        self.rect_mesa = rect_mesa
        self.rect_bliteo = self.imagen_feliz.get_rect()
        self.rect_bliteo.x = self.rect_mesa.x 
        self.rect_bliteo.y = self.rect_mesa.y - 15 
    
    def actualizar_inicio_tiempo_espera (self,inicio: bool):
        self.inicio_tiempo_espera = inicio

    def blitear_cliente (self,pantalla):
        pantalla.blit(self.imagen_bliteo,self.rect_bliteo)

    def actualizar_tiempo_espera(self,tiempo_espera:int):
        self.tiempo_espera = tiempo_espera
    
    def reinciar_paciencia_cliente(self, tiempo_total_juego:int):
        self.tiempo_espera = tiempo_total_juego

    def revisar_paciencia_cliente(self, tiempo_juego:int):
        if (tiempo_juego - self.tiempo_espera) > TIEMPO_ENOJO:
            self.propina -= 10
            self.imagen_bliteo = self.imagen_enojado
            self.animo = "ira"
        elif (tiempo_juego - self.tiempo_espera) > TIEMPO_NEUTRAL:
            self.propina -= 15
            self.animo = "enojo"
        elif (tiempo_juego - self.tiempo_espera) > TIEMPO_FELICES:
            self.propina -= 20
            self.animo = "neutral"
        else:
            self.animo = "feliz"

    def cambiar_imagen_segun_animo (self):
        match self.animo:
            case "feliz":
                self.imagen_bliteo = self.imagen_feliz
            case "neutral":
                self.imagen_bliteo = self.imagen_feliz
            case "enojo":
                self.imagen_bliteo = self.imagen_enojado
            case "ira":
                self.imagen_bliteo = self.imagen_enojado
        