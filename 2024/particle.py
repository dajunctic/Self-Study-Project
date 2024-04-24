import random

import pygame


class Particle:
    SIZE_DEC = 0.1
    GRAVITY = 1

    def __init__(self, app, x, y, vx, vy, size, color):
        self.app = app
        self.surface = app.surf

        self.x = x
        self.y = y

        self.vx = vx
        self.vy = vy

        self.alive = True
        self.size = size

        self.color = color

    def update(self):
        self.x += self.vx * self.app.dt
        self.y += self.vy * self.app.dt

        self.vy += self.GRAVITY

        self.size -= self.SIZE_DEC
        if self.size <= 0:
            self.size = 0
            self.alive = False

    def draw(self):
        pygame.draw.circle(self.surface, self.color, (self.x, self.y), self.size)


class ParticleEffect:
    def __init__(self, app, x, y, color):
        self.app = app
        self.surface = app.surf
        self.x = x
        self.y = y

        self.particles = []
        # self.frames = 0

        self.color = color

    def update(self):
        self.make_particle()

        self.particles = [x for x in self.particles if x.alive]
        for x in self.particles:
            x.update()

    def draw(self):
        for x in self.particles:
            x.draw()

    def make_particle(self):
        vx = random.randint(-5, 5) / 10
        vy = 4

        size = random.randint(4, 8)

        self.particles.append(Particle(self.app, self.x, self.y, vx, vy, size, self.color))

    def set_pos(self, x, y):
        self.x = x
        self.y = y
