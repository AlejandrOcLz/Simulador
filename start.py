import pygame, sys, random, math

from selvaAlta import SelvaAlta
from montanas import Montanas
from desierto import Desierto
from tundra import Tundra

pygame.init()

# Definir colores
white = (255,255,255)
blue = (173, 216, 230)  # Un azul que sirve como color base del agua

size = (1000, 700)

# crear ventana
screen = pygame.display.set_mode(size)

# Valores aleatorios en el mapa
screen_width, screen_height = size
half_size = 25
center_x = random.randint(half_size, screen_width - half_size)
center_y = random.randint(half_size, screen_height - half_size)

selvaA = SelvaAlta(center_x, center_y)
montan = Montanas(center_x, center_y)
desi = Desierto(center_x, center_y)
tund = Tundra(center_x, center_y)

# Definir colores de agua
water_colors = [(0, 105, 148), (0, 125, 168), (0, 95, 128)]  # Tonos de azul

# Crear una superficie para el fondo
water_background = pygame.Surface(size)
water_background.fill(blue)  # Fondo azul

# Dibujar olas en la superficie del fondo
wave_amplitude = 5  # La altura de la ola
wave_frequency = 20  # Qué tan seguido aparecen las olas
segment_length = 100  # Longitud de cada segmento de la ola
gap_length = 10  # Longitud del espacio entre segmentos

for y in range(0, size[1], 20):  # Distancia entre olas verticales
    x = 0
    while x < size[0]:
        wave_length = random.randint(10, 40)  # Longitud aleatoria para el segmento de la ola
        wave_points = []
        for i in range(wave_length):
            if x < size[0]:
                sin_y = y + wave_amplitude * math.sin(x / wave_frequency)
                wave_points.append((x, sin_y))
                x += 1
        if len(wave_points) > 1:  # Asegurarse de que hay al menos dos puntos
            pygame.draw.lines(water_background, white, False, wave_points, 1)
        x += random.randint(5, 20)  # Espacio aleatorio antes del próximo segmento



def create_random_selva_alta():
    marginx = random.randint(40, 200)
    marginy = random.randint(30, 150)
    x = random.randint(marginx, size[0] - marginx)
    y = random.randint(marginy, size[1] - marginy)
    return SelvaAlta(x, y)

def create_random_desierto():
    marginx = random.randint(300, 400)
    marginy = random.randint(150, 200)
    x = random.randint(marginx, size[0] - marginx)
    y = random.randint(marginy, size[1] - marginy)
    return Desierto(x, y)

def create_random_tundra():
    marginx = random.randint(40, 200)
    marginy = random.randint(30, 150)
    x = random.randint(marginx, size[0] - marginx)
    y = random.randint(marginy, size[1] - marginy)
    return Tundra(x, y)

def create_random_montanas():
    marginx = random.randint(156, 200)
    marginy = random.randint(100, 150)
    x = random.randint(marginx, size[0] - marginx)
    y = random.randint(marginy, size[1] - marginy)
    return Montanas(x, y)

# Lista para mantener todas las instancias de SelvaAlta
selva_alta_list = [create_random_selva_alta() for _ in range(400)]

desierto_list = [create_random_desierto() for _ in range(100)]

tundra_list = [create_random_tundra() for _ in range(25)]
# Lista para mantener todas las instancias de Montanas
montanas_list = [create_random_montanas() for _ in range(80)]  # Asumiendo que quieres menos montañas


while True:
    for event in pygame.event.get():
        print(event)
        if event.type==pygame.QUIT:
            sys.exit()

    # Dibujar el fondo de agua
    screen.blit(water_background, (0, 0))

    #screen.fill(white)

    # -------- Zona de dibujo --------- #

    #pygame.draw.line(screen, red, [0,100],[100,100], 5)

    #selvaA.draw(screen)
    for selva in selva_alta_list:
        selva.draw(screen)

    for desierto in desierto_list:
        desierto.draw(screen)
        
    for tundra in tundra_list:
        tundra.draw(screen)
    # Dibujar las montañas
    for montana in montanas_list:
        montana.draw(screen)

    # -------- Zona de dibujo --------- #

    #Actualizar pantalla
    pygame.display.flip()