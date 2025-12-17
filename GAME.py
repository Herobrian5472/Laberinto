import pygame, random, sys
from CONSTANTES import *
from CLASES import *

def MOSTRAR_MARCADOR():
    font = pygame.font.SysFont('Arial', BALDOSA_TAMANIO - 5)
    background = pygame.Surface((ANCHURA, MARCADOR_ALTURA))
    background = background.convert()
    background.fill(BLANCO)
    text = font.render(_personaje.crono.Timer.strftime("%H:%M:%S"), 1, NEGRO)
    textpos = text.get_rect(centerx=ANCHURA / 2, centery=MARCADOR_ALTURA / 2)
    background.blit(text, textpos)
    screen.blit(background, (0, 0))
    
pygame.init()

screen = pygame.display.set_mode([ANCHURA, ALTURA])
pygame.display.set_caption('EL juego del Laberinto')

XX = 0
YY = 0
with open("Laberinto.txt", "r") as archivo:
    for linea in archivo:
        for sprite in linea:
            if sprite == 'M':
                _pared = PARED(XX, YY)
                LISTA_PAREDES.add(_pared)
                LISTA_GLOBAL_SPRITES.add(_pared)
            XX = XX + 1
        XX = 0
        YY = YY + 1
        
_personaje = None
BUSCAR_PERSONAJE = True
while BUSCAR_PERSONAJE:
    _personaje = PERSONAJE()
    LISTA_CONFLICTO = pygame.sprite.spritecollide(_personaje, LISTA_PAREDES, False)
    if len(LISTA_CONFLICTO) == 0:
        LISTA_GLOBAL_SPRITES.add(_personaje)
        BUSCAR_PERSONAJE = False
        
while len(LISTA_OBJETOS) < 10:
    _objeto = OBJETO()
    LISTA_CONFLICTO = pygame.sprite.spritecollide(_objeto, LISTA_GLOBAL_SPRITES, False)
    if len(LISTA_CONFLICTO) == 0:
        LISTA_GLOBAL_SPRITES.add(_objeto)
        LISTA_OBJETOS.add(_objeto)
        
clock = pygame.time.Clock()

print("EStamos listos...")

TERMINADO = False

while not TERMINADO:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            TERMINADO = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                _personaje.DIRECCION = 'I'
                break
            elif event.key == pygame.K_RIGHT:
                _personaje.DIRECCION = 'D'
                break
            elif event.key == pygame.K_UP:
                _personaje.DIRECCION = 'A'
                break
            elif event.key == pygame.K_DOWN:
                _personaje.DIRECCION = 'B'
                break
            
    LISTA_GLOBAL_SPRITES.update()
    screen.fill(NEGRO)
    
    LISTA_GLOBAL_SPRITES.draw(screen)
    MOSTRAR_MARCADOR()
    
    if _personaje.TERMINADO:
        pygame.time.wait(5000)
        TERMINADO = True
        
    pygame.display.flip()
    dt = clock.tick (60)
    _personaje.crono.update(dt)
    
print("Número de objetos recogidos: %d" % _personaje.PUNTOS)
pygame.quit()