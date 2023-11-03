import pygame, sys, random

from selvaAlta import SelvaAlta

pygame.init()

# Definir colores
white = (255,255,255)

size = (1000, 700)

# crear ventana
screen = pygame.display.set_mode(size)

# Valores aleatorios en el mapa
screen_width, screen_height = size
half_size = 25
center_x = random.randint(half_size, screen_width - half_size)
center_y = random.randint(half_size, screen_height - half_size)

selvaA = SelvaAlta(center_x, center_y)

while True:
    for event in pygame.event.get():
        print(event)
        if event.type==pygame.QUIT:
            sys.exit()
            

    screen.fill(white)

    # -------- Zona de dibujo --------- #

    #pygame.draw.line(screen, red, [0,100],[100,100], 5)

    selvaA.draw(screen)

    # -------- Zona de dibujo --------- #

    #Actualizar pantalla
    pygame.display.flip()