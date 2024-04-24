import math
import random

import pygame as pg


class Firework:
    def __init__(self, surface, pos, color, size, move, time, has_child=True):
        self.surface = surface
        self.pos = list(pos)
        self.color = list(color)
        self.size = size
        self.move = move

        self.time = time * 60
        self.count = 0

        self.explore = False
        self.has_child = has_child
        self.child = []

        self.destroy = False

    def update(self):
        if not self.explore:

            self.pos[0] += self.move[0]
            self.pos[1] += self.move[1]

            self.count += 1
            if self.count > self.time:
                self.explore = True

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
        for i in range(0, 360, 10):
            angle = random.randint(0, 360) / 180.0 * math.pi
            move_x = math.cos(angle) * self.move[0] - math.sin(angle) * self.move[1]
            move_y = math.sin(angle) * self.move[0] + math.cos(angle) * self.move[1]

            random_time = random.randint(8, 10)
            random_size = random.randint(2, 5)
            random_speed = random.random() * (2 - 1 + 1) + 1

            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)

            self.child.append(
                Firework(self.surface, self.pos, (r, g, b), self.size / random_size,
                         (move_x * random_speed, move_y * random_speed), self.time / 60 / random_time,
                         False))

    def draw(self):
        if not self.explore:
            pg.draw.circle(self.surface, self.color, self.pos, self.size)

        else:
            for x in self.child:
                x.draw()
