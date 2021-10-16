import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 850))

rect(screen, (0, 30, 40), (0, 0, 600, 500))
rect(screen, (30, 40, 0), (0, 500, 600, 400))
rect(screen, (30, 100, 0), (0, 500, 600, 1))
circle(screen, (255, 255, 255), (420, 250), 100)
ellipse(screen, (100, 100, 100), (400, -5, 400, 100))
ellipse(screen, (100, 100, 100), (-240, 50, 600, 170))
ellipse(screen, (100, 100, 100), (300, 160, 600, 100))
ellipse(screen, (100, 100, 100), (-200, 255, 620, 110))
ellipse(screen, (100, 100, 100), (240, 290, 600, 130))
ellipse(screen, (50, 50, 50), (150, 360, 500, 100))
ellipse(screen, (50, 50, 50), (140, 105, 500, 90))
ellipse(screen, (50, 50, 50), (-150, 215, 450, 105))
polygon(screen, (50, 80, 90), [(60, 500), (130, 370), (200, 500)])
polygon(screen, (130, 200, 100), [(60, 500), (130, 500), (200, 500)])
polygon(screen, (130, 140, 100), [(60, 500), (25, 565), (242, 578), (200, 500)])
ellipse(screen, (150, 150, 150), (10, 380, 250, 90))
ellipse(screen, (200, 200, 200), (45, 370, 180, 65))
ellipse(screen, (255, 255, 255), (18, 416, 35, 15))
ellipse(screen, (255, 255, 255), (50, 435, 35, 15))
ellipse(screen, (255, 255, 255), (91, 445, 35, 15))
ellipse(screen, (255, 255, 255), (139, 445, 35, 15))
ellipse(screen, (255, 255, 255), (180, 435, 35, 15))
ellipse(screen, (255, 255, 255), (215, 420, 35, 15))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()