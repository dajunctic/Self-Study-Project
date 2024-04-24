import math

import pygame as pg
from object_3d import *
from camera import *
from projection import *


class SoftwareRender:
    def __init__(self):
        pg.init()
        self.RESOLUTION = self.WIDTH, self.HEIGHT = 1280, 720
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2, self.HEIGHT // 2
        self.FPS = 60

        self.surface = pg.display.set_mode(self.RESOLUTION)
        self.clock = pg.time.Clock()

        self.object = None
        self.camera = None
        self.projection = None
        self.axes = None
        self.world_axes = None
        self.create_objects()

    def create_objects(self):
        self.camera = Camera(self, [2, 4, -20])
        self.projection = Projection(self)

        self.object = self.get_object_from_file("res/F1.obj")
        self.object.draw_vertexes = False
        # self.object.movement_flag = False

        self.world_axes = Axes(self)
        self.world_axes.translate([0.0001, 0.0001, 0.0001])
        self.world_axes.movement_flag = False
        self.world_axes.scale(6)

    def get_object_from_file(self, filename):
        vertexes, faces = [], []
        with open(filename) as f:
            for line in f:
                if line.startswith('v '):
                    vertexes.append([float(i) for i in line.split()[1:]] + [1])
                elif line.startswith('f'):
                    faces_ = line.split()[1:]
                    faces.append([int(face_.split('/')[0]) - 1 for face_ in faces_])

        return Object3D(self, vertexes, faces)

    def draw(self):
        self.surface.fill(pg.Color("darkslategray"))
        self.world_axes.draw()
        self.object.draw()

    def run(self):
        while True:
            self.draw()
            self.camera.control()

            [exit() for i in pg.event.get() if i.type == pg.QUIT]

            pg.display.set_caption(str(round(self.clock.get_fps(), 2)))
            pg.display.flip()
            self.clock.tick(self.FPS)


if __name__ == '__main__':
    app = SoftwareRender()
    app.run()
