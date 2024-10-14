import sys

import pygame
# from random import randint
import RGB_Lib

class Bar(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)



class Game:
    def __init__(self, WIDTH, HEIGHT, TITLE):
        pass

# Размер главного окна
WIDTH = 1200
HEIGHT = 800
WINDOW_NAME = "Ping-pong"

scale_widht = 1.5 # сократить ширину картинки "в количество раз..."
scale_height = 1.5 # сократить высоту картинки "в количество раз..."

# отображение главного окна
wind = pygame.display.set_mode((WIDTH, HEIGHT))

# дежурный цвет окна
wind.fill(RGB_Lib.Olive)

bg_surf = pygame.image.load("Ping-pong-background.png")
bg_rect = bg_surf.get_rect(bottomright=(WIDTH, HEIGHT))
wind.blit(bg_surf, bg_rect)

# image_ball = pygame.image.load("ball.png")
# imbl = image_ball.get_rect(bottomright=(100, 100))
# wind.blit(image_ball, imbl)

scale = pygame.transform.scale(
    bg_surf, (bg_surf.get_width() // scale_widht,
              bg_surf.get_height() // scale_height))
scale_rect = scale.get_rect(center=(WIDTH / 2, HEIGHT / 2))
wind.blit(scale, scale_rect)
pygame.display.update(bg_rect)
pygame.time.wait(1000)

pygame.display.update()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.time.delay(20)