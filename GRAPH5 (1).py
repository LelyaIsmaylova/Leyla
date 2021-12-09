import pygame
from pygame.draw import circle

clock = pygame.time.Clock()
pygame.init()

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D

screen = pygame.display.set_mode((1500, 750))

cbs = (60,30)
cbc = (1400,5)
clear_button = pygame.Surface(cbs, pygame.SRCALPHA)
clear_font = pygame.font.Font(None, 30).render('Clear', True, BLACK)
clear_button.blit(clear_font, (5,5))

nbs = (60,30)
nbc = (70,5)
node_button = pygame.Surface(nbs, pygame.SRCALPHA)
font_node = pygame.font.Font(None, 30).render("Node", True, BLACK)
node_button.blit(font_node, (5,5))

ebs = (60,30)
ebc = (140,5)
edge_button = pygame.Surface(ebs, pygame.SRCALPHA)
font_edge = pygame.font.Font(None, 30).render("Edge", True, BLACK)
edge_button.blit(font_edge, (5,5))

bbs = (60,30)
bbc = (5,5)
back_button = pygame.Surface(bbs, pygame.SRCALPHA)
font_back = pygame.font.Font(None, 30).render("Back", True, BLACK)
back_button.blit(font_back,(5,5))

agbs = (120,30)
agbc = (300,5)
add_graph_button = pygame.Surface(agbs, pygame.SRCALPHA)
font_add_graph = pygame.font.Font(None, 30).render("Add Graph", True, BLACK)
add_graph_button.blit(font_add_graph, (5,5))

numbers = []

for i in range(1,21):
    surface = pygame.Surface((40, 40), pygame.SRCALPHA)
    number = pygame.font.Font(None, 30).render(str(i), True, BLACK)
    surface.blit(number, (0,0))
    numbers.append(surface)


def press_button(x1, x2, y1, y2, pos):
    return (pos[0] > x1) and (pos[0] < x2) and (pos[1] > y1) and (pos[1] < y2)

def press_node(pos):
    for node in nodes:
        if (pos[0]-node[0])**2+(pos[1]-node[1])**2 <= 256:
            return node
    return -1


def show_buttons():
    if mode == 'start':
        screen.blit(clear_button, cbc)
        screen.blit(node_button, nbc)
        screen.blit(edge_button, ebc)
    else:
        screen.blit(back_button, bbc)

def show_graph():
    for edge in edges:
        pygame.draw.line(screen, BLACK, edge[0], edge[1], 1)

    for i in range(len(nodes)):
        circle(screen, GREEN, nodes[i], 16)
        circle(screen, BLACK, nodes[i], 16, 1)
        screen.blit(numbers[i], (nodes[i][0]-6,nodes[i][1]-8))


nodes = []
edges = []
point1 = -1
point2 = -1
mode = 'start'
finished = False

while not finished:
    screen.fill(WHITE)

    show_buttons()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if mode == 'start':
                if press_button(nbc[0], nbc[0]+nbs[0], nbc[1], nbc[1]+nbs[1], pos):
                    mode = 'add node'
                elif press_button(ebc[0], ebc[0]+ebs[0], ebc[1], ebc[1]+ebs[1], pos):
                    mode = 'add edge 1'
                elif press_button(cbc[0], cbc[0]+cbs[0], cbc[1], cbc[1]+cbs[1], pos):
                    nodes.clear()
                    edges.clear()
            elif mode == 'add node':
                if (pos[0] > 50) and (pos[0] < 1450) and (pos[1] < 700) and (pos[1] > 50):
                    nodes.append((pos[0], pos[1]))
                if press_button(bbc[0], bbc[0]+bbs[0], bbc[1], bbc[1]+bbs[1], pos):
                    mode = 'start'
            elif mode == 'add edge 1':
                point1 = press_node(pos)
                if point1 != -1:
                    mode = 'add edge 2'
                if press_button(bbc[0], bbc[0]+bbs[0], bbc[1], bbc[1]+bbs[1], pos):
                    mode = 'start'
            elif mode == 'add edge 2':
                point2 = press_node(pos)
                if point2 != -1 and point2 != point1:
                    edges.append((point1, point2))
                    mode = 'add edge 1'
                    point1 = -1
                    point2 = -1
                if press_button(bbc[0], bbc[0]+bbs[0], bbc[1], bbc[1]+bbs[1], pos):
                    mode = 'start'

    show_graph()

    pygame.display.update()
    clock.tick(60)

pygame.quit()