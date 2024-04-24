import math
import random

import pygame as pg

from particle import ParticleEffect


class Firework:
    def __init__(self, app, pos, color, size, move, time, has_child=True):
        self.app = app
        self.surface = app.surf
        self.pos = list(pos)
        self.color = list(color)
        self.size = size
        self.move = move

        self.time = time
        self.count = 0

        self.explode = False
        self.has_child = has_child
        self.child = []

        self.destroy = False

        self.gravity = 1

        self.particle = ParticleEffect(self.app, pos[0], pos[1], self.color)

    def update(self):
        if not self.explode:

            self.pos[0] += self.move[0] * self.app.dt
            self.pos[1] += self.move[1] * self.app.dt

            if not self.has_child:
                self.move = (self.move[0], self.move[1] + self.gravity)

            self.particle.update()
            self.particle.set_pos(self.pos[0], self.pos[1])

            self.count += self.app.dt
            if self.count > self.time:
                self.explode = True

                if self.has_child:
                    self.make_child()
                else:
                    self.destroy = True
        else:
            for x in self.child:
                x.update()

            self.child = [x for x in self.child if not x.destroy]

            if len(self.child) == 0:
                self.destroy = True

    def make_child(self):
        for i in range(0, 720, 1):
            angle = random.randint(0, 360) / 180.0 * math.pi
            move_x = math.cos(angle) * self.move[0] - math.sin(angle) * self.move[1]
            move_y = math.sin(angle) * self.move[0] + math.cos(angle) * self.move[1]

            random_time = random.randint(3, 7)
            random_size = random.randint(2, 4)
            random_speed = random.random() * (2 - 1 + 1) + 1

            self.child.append(
                Firework(self.app, self.pos, self.color, self.size / random_size,
                         (move_x * random_speed, move_y * random_speed), self.time / random_time,
                         False))

        for i in range(0, 50, 1):
            angle = random.randint(0, 360) / 180.0 * math.pi
            move_x = math.cos(angle) * self.move[0] - math.sin(angle) * self.move[1]
            move_y = math.sin(angle) * self.move[0] + math.cos(angle) * self.move[1]

            random_time = random.randint(2, 5)
            random_size = random.randint(2, 4)
            random_speed = random.random() * (1 - 0 + 1)

            self.child.append(
                Firework(self.app, self.pos, self.color, self.size / random_size,
                         (move_x * random_speed, move_y * random_speed), self.time / random_time,
                         False))

    def draw(self):
        if not self.explode:

            if self.has_child:
                self.particle.draw()
            else:
                pg.draw.circle(self.surface, self.color, self.pos, self.size)

        else:
            for x in self.child:
                x.draw()
