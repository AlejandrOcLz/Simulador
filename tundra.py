import pygame
import math

class Tundra:
    def __init__(self, center_x, center_y, size=50, color=(218, 228, 242)):
        self.center_x = center_x
        self.center_y = center_y
        self.size = size
        self.color = color
        self.angle = 45  # Grados para ladear el cuadrado

    def draw(self, surface):
        # Calcular las esquinas del cuadrado ladeado
        half_size = self.size / 2
        cos_angle = math.cos(math.radians(self.angle))
        sin_angle = math.sin(math.radians(self.angle))

        # Puntos del cuadrado antes de la rotación (alrededor del centro)
        square_points = [
            (self.center_x - half_size, self.center_y - half_size),
            (self.center_x + half_size, self.center_y - half_size),
            (self.center_x + half_size, self.center_y + half_size),
            (self.center_x - half_size, self.center_y + half_size)
        ]

        # Rotar cada punto alrededor del centro del cuadrado
        points = []
        for x, y in square_points:
            x_rot = self.center_x + (x - self.center_x) * cos_angle - (y - self.center_y) * sin_angle
            y_rot = self.center_y + (x - self.center_x) * sin_angle + (y - self.center_y) * cos_angle
            points.append((x_rot, y_rot))

        pygame.draw.polygon(surface, self.color, points)

