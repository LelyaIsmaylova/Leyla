import pygame as pg
import numpy as np
from random import randint

SCREEN_SIZE = (800, 600)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

pg.init()
count = 0
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
WHITE = (255, 255, 255)

class Ball():
    def __init__(self, coord, vel, rad=10, color=None):
        if color == None:
            color = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.color = color
        self.coord = coord
        self.vel = vel
        self.rad = rad
        self.is_alive = True

    def draw(self, screen):
        pg.draw.circle(screen, self.color, self.coord, self.rad)

    def move(self, t_step=1., g=2.):
        self.vel[1] += int(g * t_step)
        for i in range(2):
            self.coord[i] += int(self.vel[i] * t_step)
        self.check_walls()
        if self.vel[0] ** 2 + self.vel[1] ** 2 < 2 ** 2 and self.coord[1] > SCREEN_SIZE[1] - 2 * self.rad:
            self.is_alive = False

    def check_walls(self):
        n = [[1, 0], [0, 1]]
        for i in range(2):
            if self.coord[i] < self.rad:
                self.coord[i] = self.rad
                self.flip_vel(n[i], 0.8, 0.9)
            elif self.coord[i] > SCREEN_SIZE[i] - self.rad:
                self.coord[i] = SCREEN_SIZE[i] - self.rad
                self.flip_vel(n[i], 0.8, 0.9)

    def flip_vel(self, axis, coef_perp=1., coef_par=1.):
        vel = np.array(self.vel)
        n = np.array(axis)
        n = n / np.linalg.norm(n)
        vel_perp = vel.dot(n) * n
        vel_par = vel - vel_perp
        ans = -vel_perp * coef_perp + vel_par * coef_par
        self.vel = ans.astype(np.int).tolist()


class Table():
    def __init__(self):
        self.x = randint(500, 780)
        self.y = randint(50, 750)
        self.r = randint(15, 50)
        self.vel = -5
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
        pg.draw.ellipse(screen, self.color, (self.x, self.y, self.r, self.r))

    def new_rect(self):
        global danger
        if not danger:
            pg.draw.ellipse(screen, BLACK, (self.x, self.y, self.r * 2, self.r))
            pg.draw.ellipse(screen, self.color, (self.x, self.y, self.r * 2, self.r))
        else:
            pg.draw.ellipse(screen, BLACK, (self.x, self.y, self.r * 2, self.r))
            self.x = randint(500, 770)
            self.y = randint(50, 750)
            self.r = randint(15, 50)
            self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
            pg.draw.ellipse(screen, self.color, (self.x, self.y, self.r * 2, self.r))
            danger = False

    def move(self, t_step=1., g=2.):
        self.x += int(self.vel * t_step)
        if self.x + self.r >= 800:
            self.vel = -self.vel
        if self.x - self.r <= 10:
            self.vel = -self.vel


class Gun():
    def __init__(self, coord=[30, SCREEN_SIZE[1] // 2],
                 min_pow=10, max_pow=55):
        self.coord = coord
        self.angle = 0
        self.min_pow = min_pow
        self.max_pow = max_pow
        self.power = min_pow
        self.active = False

    def draw(self, screen):
        '''рисует пушку и танк'''
        end_pos = [self.coord[0] + np.sqrt(self.power) * np.cos(self.angle),
                   self.coord[1] + np.sqrt(self.power) * np.sin(self.angle)]
        pg.draw.line(screen, RED, self.coord, end_pos, 5)
        pg.draw.rect(screen, GREEN, (self.coord[0] - 10, self.coord[1] - 5, 10, 10))
        pg.draw.rect(screen, GREEN, (self.coord[0] - 15, self.coord[1] + 5, 20, 10))

    def strike(self):
        vel = [int(self.power * np.cos(self.angle)), int(self.power * np.sin(self.angle))]
        self.active = False
        self.power = self.min_pow
        return Ball(list(self.coord), vel)

    def move(self):
        if self.active and self.power < self.max_pow:
            self.power += 5

    def set_angle(self, mouse_pos):
        self.angle = np.arctan2(mouse_pos[1] - self.coord[1],
                                mouse_pos[0] - self.coord[0])


class Enemy():
    pass
    '''пушки-враги'''

    def __init__(self, coord=[785, 0, 785, 595]):
        self.gun = Gun()
        self.angle = [0, 0]
        self.coord = coord
        self.vel = [0, 0]
        self.bomcor = [785, 0, 785, 595]

    def draw(self):
        end_pos = [[self.coord[0] - 40 * np.cos(self.angle[0]),
                    self.coord[1] - 40 * np.sin(self.angle[0])],
                   [self.coord[2] - 40 * np.cos(self.angle[1]),
                    self.coord[3] - 40 * np.sin(self.angle[1])]]
        pg.draw.line(screen, MAGENTA, [self.coord[0], self.coord[1]], end_pos[0], 10)
        pg.draw.rect(screen, GREEN, (self.coord[0] - 10, self.coord[1] - 5, 30, 30))
        pg.draw.line(screen, YELLOW, [self.coord[2], self.coord[3]], end_pos[1], 10)
        pg.draw.rect(screen, BLUE, (770, 570, 30, 30))

    def set_angle(self):
        for i in range(2):
            self.angle[i] = np.arctan2(-self.gun.coord[1] + self.coord[1 + i * 2],
                                       -self.gun.coord[0] + self.coord[0 + i * 2])

    def boom(self, t_step=1.):
        self.vel = [-10 * np.cos(self.angle[0]), -10 * np.sin(self.angle[0])]
        for i in range(2):
            self.bomcor[i] += int(self.vel[i] * t_step)
            self.bomcor[2] += int(self.vel[i] * t_step)

    def bomb(self):
        self.bomcor = [785, 0, 785, 595]
        pg.draw.circle(screen, WHITE, (self.bomcor[0], self.bomcor[1]), 10)
        pg.draw.circle(screen, WHITE, (self.bomcor[2], self.bomcor[3]), 10)


class Target():
    def __init__(self):
        self.x = randint(300, 500)
        self.y = randint(0, 400)
        self.r = randint(15, 50)
        self.vel = 1
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
        pg.draw.circle(screen, self.color, (self.x, self.y), self.r)

    def new_target(self):
        global strike
        if not strike:
            pg.draw.circle(screen, BLACK, (self.x, self.y), self.r)
            pg.draw.circle(screen, self.color, (self.x, self.y), self.r)
        else:
            pg.draw.circle(screen, BLACK, (self.x, self.y), self.r)
            self.x = randint(300, 500)
            self.y = randint(0, 400)
            self.r = randint(15, 50)
            self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
            pg.draw.circle(screen, self.color, (self.x, self.y), self.r)
            strike = False

    def move(self, t_step=1., g=2.):
        global strike
        if strike:
            self.vel = randint(1, 5)
        self.y += int(self.vel * t_step)
        self.check_walls()

    def check_walls(self):
        if self.y < self.r:
            self.vel = -self.vel
        elif self.y > SCREEN_SIZE[1] - self.r:
            self.y = SCREEN_SIZE[1] - self.r
            self.vel = -self.vel


class Manager():
    def __init__(self):
        self.gun = Gun()
        self.table = Table()
        self.balls = []
        self.target = Target()
        self.enemy = Enemy()

    def process(self, events, screen):
        global count
        global strike
        global danger
        done = self.handle_events(events)
        self.move()
        self.draw(screen)
        self.check_alive()
        for ball in self.balls:
            if ((self.target.x - ball.coord[0]) ** 2 + (self.target.y - ball.coord[1]) ** 2) <= (
                    (self.target.r + ball.rad) ** 2):
                count += 1
                strike = True
                self.target.new_target()
            elif ((self.table.x - ball.coord[0]) ** 2 + (self.table.y - ball.coord[1]) ** 2) <= (
                    (self.table.r + ball.rad) ** 2):
                count += 3
                danger = True
                self.table.new_rect()
        if ((self.target.x - self.gun.coord[0]) ** 2 + (self.target.y - self.gun.coord[1]) ** 2) <= (
                (self.target.r + 20) ** 2):
            count = 5
            strike = True
            self.target.new_target()
        elif ((self.table.x - self.gun.coord[0]) ** 2 + (self.table.y - self.gun.coord[1]) ** 2) <= (
                (self.table.r + 20) ** 2):
            count -= 15
            danger = True
            self.table.new_rect()
        return done

    def draw(self, screen):
        screen.fill(BLACK)
        for ball in self.balls:
            ball.draw(screen)
        self.gun.draw(screen)
        self.target.new_target()
        self.enemy.draw()
        self.table.new_rect()
        self.enemy.bomb()

    def move(self):
        for ball in self.balls:
            ball.move()
        self.gun.move()
        self.target.move()
        self.table.move()
        self.enemy.boom()

    def check_alive(self):
        dead_balls = []
        for i, ball in enumerate(self.balls):
            if not ball.is_alive:
                dead_balls.append(i)

        for i in reversed(dead_balls):
            self.balls.pop(i)
        balls = len(self.balls)

    def handle_events(self, events):
        global count
        global strike
        global balls
        global evnum
        done = False
        for event in events:
            if event.type == pg.QUIT or balls >= 100:
                done = True
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.gun.coord[1] -= 10
                elif event.key == pg.K_DOWN:
                    self.gun.coord[1] += 10
                elif event.key == pg.K_RIGHT:
                    self.gun.coord[0] += 10
                elif event.key == pg.K_LEFT:
                    self.gun.coord[0] -= 10
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.gun.active = True
            elif event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    self.balls.append(self.gun.strike())
                    balls += 1
        if pg.mouse.get_focused():
            mouse_pos = pg.mouse.get_pos()
            self.gun.set_angle(mouse_pos)
        return done


screen = pg.display.set_mode(SCREEN_SIZE)
pg.display.set_caption("The gun")
clock = pg.time.Clock()

strike = True
balls = 0
evnum = 0
danger = True
mgr = Manager()
done = False

while not done:
    clock.tick(20)

    done = mgr.process(pg.event.get(), screen)

    pg.display.flip()
pg.quit()
print("Вы получаете " + str(count) + " очков за " + str(balls) + " выстрелов")