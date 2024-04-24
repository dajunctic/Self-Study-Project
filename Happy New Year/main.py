import math
import random
import sys
from itertools import cycle

from firework import *


RES = (1280, 720)

BLINK_EVENT = pg.USEREVENT + 0

class App:
    def __init__(self):
        pg.init()
        self.surface = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        pg.display.set_caption("Happy New Year 2023")

        self.speed = 3

        self.count = -1
        self.time_per_fire = 0.3  # second
        self.time = self.time_per_fire * 60

        self.move_x = 0
        self.move_y = -self.speed

        self.fires = []

        screen_rect = self.surface.get_rect()
        self.font = pg.font.Font("debug.otf", 100)
        on_text_surface = self.font.render(
            'HAPPY NEW YEAR 2023', True, pg.Color('green3')
        )
        self.blink_rect = on_text_surface.get_rect()
        self.blink_rect.center = screen_rect.center
        off_text_surface = pg.Surface(self.blink_rect.size)
        off_text_surface.fill((0, 0, 0, 0))

        self.blink_surfaces = cycle([on_text_surface, off_text_surface])
        self.blink_surface = next(self.blink_surfaces)
        pg.time.set_timer(BLINK_EVENT, 1000)

    def update(self):
        self.count += 1
        if self.count % self.time == 0:
            x = random.randint(200, 1080)
            y = random.randint(730, 760)

            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)

            angle = random.randint(-15, 15) / 180 * math.pi
            move_x = math.cos(angle) * self.move_x - math.sin(angle) * self.move_y
            move_y = math.sin(angle) * self.move_x + math.cos(angle) * self.move_y

            rand_time = random.randint(1, 3)

            self.fires.append(Firework(self.surface, (x, y),
                                       (r, g, b), 10, (move_x, move_y), rand_time))

        for x in self.fires:
            x.update()
            if x.destroy:
                self.fires.remove(x)

    def draw(self):
        self.surface.fill([0, 0, 0])

        self.surface.blit(self.blink_surface, self.blink_rect)

        for x in self.fires:
            x.draw()

    def run(self):
        while True:

            self.update()
            self.draw()

            for e in pg.event.get():
                if e.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

                if e.type == BLINK_EVENT:
                    self.blink_surface = next(self.blink_surfaces)

            pg.display.update()
            self.clock.tick(60)


if __name__ == '__main__':
    app = App()
    app.run()
