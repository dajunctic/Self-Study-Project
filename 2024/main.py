import random
import math
import pygame as pg

from firework import Firework

class App:
    def __init__(self):
        self.getTicksLastFrame = 0
        pg.init()
        pg.mixer.init()

        self.surf = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        pg.display.set_caption('2024')

        info = pg.display.Info()

        self.width = info.current_w
        self.height = info.current_h

        self.running = True
        self.clock = pg.time.Clock()

        self.fires = []
        self.time_per_fire = 0.5

        self.count = -1
        self.speed = 200

        self.move_x = 0
        self.move_y = -self.speed

        self.dt = 0
        self.prev = 0

        pg.mixer.music.load("aba.mp3")
        pg.mixer.music.play()

    def run(self):
        while self.running:
            for e in pg.event.get():
                if e.type == pg.QUIT or (e.type == pg.KEYDOWN and e.key == pg.K_q):
                    self.running = False

            self.update()
            self.draw()

            t = pg.time.get_ticks()
            self.dt = (t - self.getTicksLastFrame) / 1000.0
            self.getTicksLastFrame = pg.time.get_ticks()

            pg.display.flip()

    def update(self):
        self.count += self.dt

        if self.count > self.time_per_fire:
            self.count = 0

            x = random.randint(100, self.width - 100)
            y = self.height

            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)

            aa = -15 if x >= 640 else -5
            bb = 5 if x >= 640 else 15

            angle = random.randint(aa, bb) / 180 * math.pi

            move_x = math.cos(angle) * self.move_x - math.sin(angle) * self.move_y
            move_y = math.sin(angle) * self.move_x + math.cos(angle) * self.move_y

            rand_time = random.randint(2, 3)

            self.fires.append(Firework(self, (x, y),
                                       (r, g, b), 10, (move_x, move_y), rand_time))

            # self.sound.play()

        for x in self.fires:
            x.update()
            if x.destroy:
                del x

    def draw(self):
        self.surf.fill([0, 0, 0])

        for x in self.fires:
            x.draw()


if __name__ == '__main__':
    app = App()
    app.run()
