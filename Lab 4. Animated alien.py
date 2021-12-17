import pygame
from pygame.draw import *

pygame.init()

FPS = 20
screen = pygame.display.set_mode((600, 850))

#background
def background():
    rect(screen, (0, 30, 40), (0, 0, 600, 500))
    rect(screen, (30, 40, 0), (0, 500, 600, 400))
    rect(screen, (30, 100, 0), (0, 500, 600, 1))
def sky():
    circle(screen, (255, 255, 255), (420, 250), 100)
    ellipse(screen, (100, 100, 100), (400, -5, 400, 100))
    ellipse(screen, (100, 100, 100), (-240, 50, 600, 170))
    ellipse(screen, (100, 100, 100), (300, 160, 600, 100))
    ellipse(screen, (100, 100, 100), (-200, 255, 620, 110))
    ellipse(screen, (100, 100, 100), (240, 290, 600, 130))
    ellipse(screen, (50, 50, 50), (150, 360, 500, 100))
    ellipse(screen, (50, 50, 50), (140, 105, 500, 90))
    ellipse(screen, (50, 50, 50), (-150, 215, 450, 105))

def ship():
    polygon(screen, (100, 130, 140), [(60, 500), (130, 370), (200, 500)])
    polygon(screen, (130, 140, 100), [(60, 500), (25, 565), (242, 578), (200, 500)])
    polygon(screen, (130, 200, 100), [(60, 500), (130, 500), (200, 500)])
    ellipse(screen, (150, 150, 150), (10, 380, 250, 90))
    ellipse(screen, (200, 200, 200), (45, 370, 180, 65))
    ellipse(screen, (255, 255, 255), (18, 416, 35, 15))
    ellipse(screen, (255, 255, 255), (50, 435, 35, 15))
    ellipse(screen, (255, 255, 255), (91, 445, 35, 15))
    ellipse(screen, (255, 255, 255), (139, 445, 35, 15))
    ellipse(screen, (255, 255, 255), (180, 435, 35, 15))
    ellipse(screen, (255, 255, 255), (215, 420, 35, 15))

def alien(i):
    ellipse(screen, (255, 255, 200), (370, 580, 70, 120))
    ellipse(screen, (255, 255, 200), (360, 660, 25+i, 45+i))
    ellipse(screen, (255, 255, 200), (360, 690, 15+i, 50+i))
    circle(screen, (255, 255, 200), (351, 735), 12+i)
    ellipse(screen, (255, 255, 200), (420, 670, 25+i, 45+i))
    ellipse(screen, (255, 255, 200), (430, 695, 15+i, 50+i))
    circle(screen, (255, 255, 200), (422, 740), 12+i)
    circle(screen, (255, 255, 200), (370, 600), 14+i)
    circle(screen, (255, 255, 200), (360, 620), 10+i)
    circle(screen, (255, 255, 200), (347, 630), 6+i)
    circle(screen, (255, 255, 200), (435, 600), 14+i)
    circle(screen, (255, 255, 200), (450, 620), 10+i)
    circle(screen, (255, 255, 200), (465, 630), 6+i)
    ellipse(screen, (255, 255, 200), (322, 630, 20, 9+i))
    ellipse(screen, (255, 255, 200), (470, 630, 20, 9+i))

def head(i):
    polygon(screen, (255, 255, 200), [(365, 510), (410, 580), (455, 510)])
    ellipse(screen, (255, 255, 200), (400, 570, 15, 20))
    circle(screen, (255, 255, 200), (365, 505), 7+i)
    circle(screen, (255, 255, 200), (362, 492), 8+i)
    circle(screen, (255, 255, 200), (355, 477), 9+i)
    circle(screen, (255, 255, 200), (340, 465), 10+i)
    circle(screen, (255, 255, 200), (460, 505), 7+i)
    circle(screen, (255, 255, 200), (470, 494), 8+i)
    circle(screen, (255, 255, 200), (484, 490), 9+i)
    circle(screen, (255, 255, 200), (505, 490), 10+i)
    circle(screen, (0, 0, 0), (397, 530), 14)
    circle(screen, (0, 0, 0), (429, 530), 11)
    circle(screen, (255, 255, 255), (399, 533), 3)
    circle(screen, (255, 255, 255), (431, 533), 3)

def apple():
    circle(screen, (255, 50, 50), (490, 610), 20)
    ellipse(screen, (100, 255, 150), (500, 578, 20, 9))
    polygon(screen, (0, 0, 0), [(490, 590), (500, 580)], 2)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
n = 0

while not finished:
    n+=0.5
    i = n%3
    background()
    sky()
    ship()
    alien(i)
    head(i)
    apple()
    clock.tick(FPS)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
