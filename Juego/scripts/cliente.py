from scripts.mesas import Mesa
import pygame
from scripts.constantes import *

class Cliente():
    def __init__ (self,lista_imagenes_cliente:list,rect_mesa,porcentaje_paciencia:int):
        self.animos_cena = {"estado_antes_atencion": None, "estado_despues_atencion": None}
        self.animo = "feliz"
        self.atendido = False
        self.inicio_tiempo_espera = True
        self.propina = 100
        self.tiempo_espera = 0
        self.imagen_feliz = lista_imagenes_cliente[0]
        self.imagen_neutral = lista_imagenes_cliente[1]
        self.imagen_enojo = lista_imagenes_cliente[2]
        self.imagen_bliteo = self.imagen_feliz
        self.rect_mesa = rect_mesa
        self.rect_bliteo = self.imagen_feliz.get_rect()
        self.rect_bliteo.x = self.rect_mesa.x - 4
        self.rect_bliteo.y = self.rect_mesa.y - 45
        self.burbuja_dialogo = None
        self.porcentaje_paciencia = porcentaje_paciencia
        self.comiendo = False

    def cambiar_imagen_a_feliz(self)->None:
        self.comiendo = True
        self.imagen_bliteo = self.imagen_feliz
    
    def actualizar_inicio_tiempo_espera (self,inicio: bool):
        self.inicio_tiempo_espera = inicio

    def blitear_cliente (self,pantalla):
        pantalla.blit(self.imagen_bliteo,self.rect_bliteo)

    def actualizar_tiempo_espera(self,tiempo_espera:int):
        self.tiempo_espera = tiempo_espera
    
    def reinciar_paciencia_cliente(self, tiempo_total_juego:int):
        self.tiempo_espera = tiempo_total_juego

    def revisar_paciencia_cliente(self, tiempo_juego:int):
        if self.atendido:
            self.animos_cena["estado_despues_atencion"] = self.animo
        else:
            self.animos_cena["estado_antes_atencion"] = self.animo

        if (tiempo_juego - self.tiempo_espera) > (TIEMPO_ENOJO + TIEMPO_FELIZ + TIEMPO_NEUTRAL) / 100 * self.porcentaje_paciencia:
            self.imagen_bliteo = self.imagen_enojo
            self.animo = "ira"
        elif (tiempo_juego - self.tiempo_espera) > (TIEMPO_NEUTRAL + TIEMPO_FELIZ) / 100 * self.porcentaje_paciencia:
            self.animo = "enojo"
        elif (tiempo_juego - self.tiempo_espera) > TIEMPO_FELIZ / 100 * self.porcentaje_paciencia:
            self.animo = "neutral"
        else:
            self.animo = "feliz"

    def cambiar_imagen_segun_animo (self)->None:
        if not self.comiendo: 
            match self.animo:
                case "feliz":
                    self.imagen_bliteo = self.imagen_feliz
                case "neutral":
                    self.imagen_bliteo = self.imagen_neutral
                case "enojo":
                    self.imagen_bliteo = self.imagen_enojo
                case "ira":
                    self.imagen_bliteo = self.imagen_enojo
    
    def determinar_propina (self)-> None:
        propina = 100
        for valor in self.animos_cena.values():
            if valor == "enojo":
                propina -= 30
            if valor == "neutral":
                propina -= 20
        self.propina = propina