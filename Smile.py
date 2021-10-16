import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

rect(screen, (255, 255, 255), (0, 0, 400, 400))
circle(screen, (255, 255, 0), (200, 175), 80)
circle(screen, (0, 0, 0), (200, 175), 80, 3)
circle(screen, (255, 0, 0), (165, 160), 20)
circle(screen, (255, 0, 0), (235, 160), 15)
circle(screen, (0, 0, 0), (165, 160), 21, 2)
circle(screen, (0, 0, 0), (235, 160), 16, 2)
circle(screen, (0, 0, 0), (165, 160), 8)
circle(screen, (0, 0, 0), (235, 160), 6)
rect(screen, (0, 0, 0), (155, 215, 90, 15))
polygon(screen, (0, 0, 0), [(210,143), (290,120)], 9)
polygon(screen, (0, 0, 0), [(110,95), (190,145)], 10)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()