'''
Created on 11/9/2014

@author: Python
'''
#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
  
# Modulos 
import sys, pygame 
from pygame.locals import * 
from jugador import *
  
# Constantes 
ANCHO = 1000  
ALTO = 400
  
# Clases 
# --------------------------------------------------------------------- 
  
# --------------------------------------------------------------------- 
  
# Funciones 
# --------------------------------------------------------------------- 
  
def carga_imagen(archivo, transparente=False): 
    try: imagen = pygame.image.load(archivo) 
    except pygame.error, message: 
        raise SystemExit, message 
    imagen = imagen.convert() 
    if transparente: 
        color = imagen.get_at((0,0)) 
        imagen.set_colorkey(color, RLEACCEL) 
    return imagen 
  
# --------------------------------------------------------------------- 
  
def main(): 
    #Pantalla
    pantalla = pygame.display.set_mode((ANCHO, ALTO)) 
    pygame.display.set_caption("Juego") 
    #Reloj
    reloj = pygame.time.Clock()
    #Fondo 
    imagen_fondo = carga_imagen('imagenes/fondo1.png')
    #jugador
    jugador = Jugador()
    direccion = None
    while True: 
        time = reloj.tick(60)
        for boton in pygame.event.get(): 
            if boton.type == QUIT: 
                sys.exit(0)
            if boton.type == pygame.KEYDOWN:
                if boton.key == pygame.K_UP:
                    direccion = "A"
            if boton.type == pygame.KEYUP:
                if boton.key == pygame.K_UP:
                    direccion = "B"                
        jugador.movimiento(direccion)
        jugador.automatico()
        pantalla.blit(imagen_fondo,(0,0))
        pantalla.blit(jugador.imagen, jugador.rect)        
        pygame.display.flip() 
    return 0 
  
if __name__ == '__main__': 
        pygame.init() 
        main()