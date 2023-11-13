class Carteles():
    def __init__ (self,imagen_desbloqueado,imagen_bloqueado):
        self.imagen_desbloqueado = imagen_desbloqueado
        self.imagen_bloqueado = imagen_bloqueado
        self.imagen_bliteo = imagen_desbloqueado
        self.rect_bliteo = self.imagen_desbloqueado.get_rect()
        self.rect = self.rect_bliteo
        self.rect_bliteo.x = 130
        self.rect_bliteo.y = 142
    
    def determinar_posicion(self, numero_cartel:int):
        match numero_cartel:
            case 1:
                pass
            case 2:
                self.rect_bliteo.x = 511
            case 3:
                self.rect_bliteo.x = 885

    def bloquear_cartel (self):
        self.imagen_bliteo = self.imagen_bloqueado
        self.rect.x = -600
    
    def desbloquear_cartel (self):
        self.imagen_bliteo = self.imagen_desbloqueado
        self.rect.x = self.rect_bliteo.x

    def blitear_cartel (self,pantalla):
        pantalla.blit(self.imagen_bliteo,self.rect_bliteo)