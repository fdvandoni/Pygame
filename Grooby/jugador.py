#Importa
import pygame
from pygame.locals import *
from creacion_sprites import spriteSheet
ANCHO = 600 
ALTO = 400
#Jugador
class Jugador(pygame.sprite.Sprite):
    #Atributos------------------
    
    #velocidad
    velocidad_x = 2
    velocidad_y = -3
    #Vectores de movimiento
    v_sprites_d = []
    #Direccion
    imagen = None
    
    #Funciones------------------
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #Carga de sprite sheet
        sprite_sheet = spriteSheet("imagenes/kirby.png")
        #Carga de imagenes DERECHAS
        imagen = sprite_sheet.carga_imagen(0, 0, 24, 24)
        self.v_sprites_d.append(imagen)
        imagen = sprite_sheet.carga_imagen(24, 0, 24, 24)
        self.v_sprites_d.append(imagen)       
                
        #Imagen inicial
        self.imagen = self.v_sprites_d[0]
        
        #Saca el rect
        self.rect = self.imagen.get_rect()
        self.rect.centerx = 30
        self.rect.centery = ALTO/2
        #Inicio movimiento-------------------------------------------------------------------------------       
   
    def movimiento(self,direccion):
        if direccion == "A":
        #Mueve arriba        
            if self.rect.top > 0:
                pos_y = self.rect.centery + self.velocidad_y
                self.rect.centery = pos_y
        elif direccion == "B":
                #Mueve abajo
            if self.rect.bottom < 400:
                pos_y = self.rect.centery - self.velocidad_y
                self.rect.centery = pos_y   
            
    def automatico(self):
        #Mueve derecha
        if self.rect.centerx < 400:
            self.pos_x = self.rect.centerx + self.velocidad_x
            frame = (self.pos_x // 30) % len(self.v_sprites_d)
            self.imagen = self.v_sprites_d[frame] 
            self.rect.centerx = self.pos_x
        else:
            frame = (self.pos_x // 30) % len(self.v_sprites_d)
            self.imagen = self.v_sprites_d[frame]             
            self.pos_x = self.pos_x + self.velocidad_x
