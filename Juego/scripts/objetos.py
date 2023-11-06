from scripts.constantes import *
import pygame

class Objetos:
    def __init__ (self, losa_apoyo: tuple, imagen):
        self.losa_apoyo = losa_apoyo
        self.imagen = imagen
        self.rect_objeto = imagen.get_rect()
        self.rect_objeto.x = ESPACIO_COSTADOS + (MEDIDAS_LOSA[0] * self.losa_apoyo[0])
        self.rect_objeto.y = ESPACIO_ARRIBA + (MEDIDAS_LOSA[1] * self.losa_apoyo[1])
        self.rect_objeto_izquierda = pygame.Rect((self.rect_objeto.x - MEDIDAS_LOSA[0],self.rect_objeto.y),(self.rect_objeto.width, self.rect_objeto.height))
        self.rect_objeto_derecha = pygame.Rect((self.rect_objeto.x + MEDIDAS_LOSA[0],self.rect_objeto.y),(self.rect_objeto.width, self.rect_objeto.height))
        self.rect_objeto_arriba = pygame.Rect((self.rect_objeto.x,self.rect_objeto.y - MEDIDAS_LOSA[0]),(self.rect_objeto.width, self.rect_objeto.height))
        self.rect_objeto_abajo = pygame.Rect((self.rect_objeto.x,self.rect_objeto.y + MEDIDAS_LOSA[0]),(self.rect_objeto.width, self.rect_objeto.height))
    
    def blitear_objeto (self,pantalla):
        pantalla.blit(self.imagen,self.rect_objeto)
    
    