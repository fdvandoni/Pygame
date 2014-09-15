import pygame
NEGRO =(   0,   0,   0)
BLANCO = (255, 255, 255)
VERDE =( 43, 133, 133)
class spriteSheet(object):
    """Creacion de prites a partir de sprite_sheet"""
    sprite_sheet = None
    
    def __init__(self, archivo):
        
        self.sprite_sheet = pygame.image.load(archivo).convert() #Carga sprite_sheet y convierte la imagen
        
    def carga_imagen(self, x, y, ancho, alto):
        
        imagen = pygame.Surface([ancho, alto]).convert() #Crea imagen en blanco donde poner el sprite
        
        imagen.blit(self.sprite_sheet, (0, 0), (x, y, ancho, alto)) #Pega el sprite en la imagen en blanco
        
        imagen.set_colorkey(BLANCO)
        
        return imagen
        
        
    
