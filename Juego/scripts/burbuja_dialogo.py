from scripts.cliente import Cliente
import pygame

class Burbuja():
    def __init__ (self,imagenes_burbujas:dict,rect_cliente,imagen_default):
        self.imagenes =  imagenes_burbujas
        self.imagen_actual = imagen_default
        self.rect_cliente = rect_cliente
        self.rect_burbuja = self.imagen_actual.get_rect()
        self.rect_burbuja.y = self.rect_cliente.y - 60
        self.rect_burbuja.x = self.rect_cliente.x
        self.imagen_pedido = None
        self.rect_comida = None
        self.pedido_equivocado = False
    
    def cambiar_imagen (self,imagen_actual:str):
        self.imagen_actual = imagen_actual
    
    def blitear_comida(self,imagen_pedido,pantalla):
        imagen_pedido = pygame.transform.scale(imagen_pedido,(imagen_pedido.get_width() / 1.5 ,imagen_pedido.get_height() / 1.5))
        self.imagen_pedido = imagen_pedido
        self.rect_comida = imagen_pedido.get_rect()
        self.rect_comida.y = self.rect_burbuja.y + 4
        self.rect_comida.x = self.rect_burbuja.x + 10
        pantalla.blit(self.imagen_pedido,self.rect_comida)
    
    def blitear_imagen(self,pantalla):
        pantalla.blit(self.imagen_actual,self.rect_burbuja)



