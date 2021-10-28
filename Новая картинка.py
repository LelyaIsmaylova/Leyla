import pygame
from pygame.draw import *

pygame.init()

screen = pygame.display.set_mode((600, 850))
screen.fill((171, 223, 136))


##небо
line_sky_mountains=[(0,262),(72,87),(124,207),(206,112),(358,340),(467,105),(503,147),(600,32)]
polygon(screen,(176,222,234),[(0,0)]+line_sky_mountains+[(600,0)])
lines(screen,(28,27,32),False,line_sky_mountains,4)
line(screen,(28,27,32),[124,207],[206,112],5)
line(screen,(28,27,32),[467,105],[503,147],4)
line(screen,(28,27,32),[503,147],[600,32],5)

##горы
line_mountains_land=[(0,448),(28,437),(58,433),(77,433),(128,425),(316,424),(323,427),(326,426),
                          (329,432),(332,434),(333,450),(335,453),(335,495),(350,502),(600,502)]
polygon(screen,(180,180,180),line_mountains_land+line_sky_mountains[::-1])
lines(screen,(28,27,32),False,line_mountains_land,1)

##штука
#   size-размер штуки;   orientation-(False;право)(True;лево)
def her_znaet_chto(x,y,size,orientation):
    shtyka_surface = pygame.Surface((160*size, 255*size), pygame.SRCALPHA)
    # грудь
    ellipse(shtyka_surface,(255,255,255),(0,115*size,135*size,55*size))
    # шея
    ellipse(shtyka_surface, (255, 255, 255),(105*size,35*size,40*size,100*size))
    #голова
    ellipse(shtyka_surface, (255, 255, 255), (110*size,10*size,50*size,30*size))
    # ушки
    polygon(shtyka_surface, (255,255,255),[(116*size,16*size),(111*size,10*size),(109*size,0),
                                                         (114*size,8*size),(121*size,15*size)])

    polygon(shtyka_surface, (255, 255, 255),[(115*size,18*size),(105*size,12*size),(102*size,9*size),
              (99*size,size),(101*size,11*size),(105*size,17*size),(111*size,25*size)])

    #ГЛАЗ
    #глазное яблоко
    ellipse(shtyka_surface, (230, 129, 255), (120*size,15*size,25*size,19*size))
    #зрачёк
    ellipse(shtyka_surface, (0, 0, 0), (135*size,20*size,8*size,8*size))
    #блик на глазу
    blic = pygame.Surface((12*size, 4*size), pygame.SRCALPHA)
    ellipse(blic, (255, 255, 255), (0, 0, 12*size, 4*size))
    povernuli_blic = pygame.transform.rotate(blic, 330)
    shtyka_surface.blit(povernuli_blic, (125*size, 15*size))


    #НОГИ  ляшки i[0];  икры i[1];   ступни i[2]
    for i in [[(20,50),(8,140),(35,160),(85,140),(103,160)],[(20,40),(8,181),(35,202),(85,181),(103,202)],[(20,14),(11,220),(38,240),(90,220),(107,240)]]:
        for j in i[1:5]:
            ellipse(shtyka_surface, (255, 255, 255), (j[0]*size, j[1]*size, i[0][0]*size, i[0][1]*size))

   shtyka_surface=pygame.transform.flip(shtyka_surface,orientation,False)
    screen.blit(shtyka_surface,(x,y))


#   size-размер штуки;   orientation-(False;право)(True;лево)
def poljana_s_jajcami(x,y,size,orientation):
    # поляна
    poljana = pygame.Surface((230*size, 230*size), pygame.SRCALPHA)
    circle(poljana, (113, 201, 52), (114*size, 114*size), 113*size)

    def kuchka_jaic( x, y, size, angle):
        kuchka = pygame.Surface((53*size, 28*size), pygame.SRCALPHA)

        if size>=0.5:
            def kontur_jajca(x,y):
                ellipse(kuchka, (175, 175, 175), (x*size, 2+y*size, 20*size, 10*size), 1)
        else:
            def kontur_jajca(x,y):
                pass

        # яйца
        for i in [(15,0),(5,4),(28,4)]:
            ellipse(kuchka, (255, 255, 255), (i[0]*size, 2+i[1]*size, 20*size, 10*size))
            kontur_jajca(i[0],i[1])

        # желток
        ellipse(kuchka, (255, 255, 0), (17*size, 2+9*size, 25*size, 10*size))

        # яйца
        for i in [(2,12),(13,14),(33,9),(27,15)]:
            ellipse(kuchka, (255, 255, 255), (i[0]*size, 2+i[1]*size, 20*size, 10*size))
            kontur_jajca(i[0], i[1])

        poljana.blit(pygame.transform.rotate(kuchka, angle), (x, y))

    for i in [(90, 15, 1, 0), (26, 40, 0.9, 30), (40, 90, 1, 15),
    (130, 50, 1.4, 330), (80, 133, 1.2, 350), (160, 120, 1, 300)]:
        kuchka_jaic(i[0]*size, i[1]*size, i[2]*size, i[3])

    poljana = pygame.transform.flip(poljana, orientation, False)

    screen.blit(poljana,(x,y))

for i in [(-20,430,0.4,False),(400,505,0.3,False),(370,690,0.6,False),(515,440,0.5,True),(500,580,0.7,True),(560,790,0.4,True)]:
    poljana_s_jajcami(i[0],i[1],i[2],i[3])

for i in [(230,340,0.5,False),(140,450,0.5,False),(-300,550,3.2,False),(262,486,0.5,True),(485,435,1.7,True)]:
    her_znaet_chto(i[0],i[1],i[2],i[3])

pygame.display.update()

finished = False
while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()
