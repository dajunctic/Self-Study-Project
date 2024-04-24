import sys
from cache import Cache
from settings import *
from player import Player
from scene import Scene


class App:
    def __init__(self):
        self.surface = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.time = 0
        self.delta_time = 0.01
        self.anim_trigger = False
        self.anim_event = pg.USEREVENT + 0

        pg.time.set_timer(self.anim_event, 100)
        # group
        self.main_group = pg.sprite.LayeredUpdates()
        self.transparent_objects = []
        # game object
        self.cache = Cache()
        self.player = Player(self)
        # scene
        self.scene = Scene(self)

    def update(self):
        self.scene.update()
        self.main_group.update()
        pg.display.set_caption(f'{self.clock.get_fps(): .2f}')
        self.delta_time = self.clock.tick()

    def draw(self):
        self.surface.fill(BG_COLOR)
        self.main_group.draw(surface=self.surface)
        pg.display.flip()

    def check_event(self):
        self.anim_trigger = False
        for e in pg.event.get():
            if e.type == pg.QUIT or e.type == pg.K_ESCAPE:
                pg.quit()
                sys.exit()
            elif e.type == self.anim_event:
                self.anim_trigger = True

    def get_time(self):
        self.time = pg.time.get_ticks() * 0.001

    def run(self):
        while True:
            self.check_event()
            self.get_time()
            self.update()
            self.draw()


if __name__ == '__main__':
    app = App()
    app.run()
