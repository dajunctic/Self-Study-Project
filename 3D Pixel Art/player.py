from settings import *
import math
from entity import BaseEntity


class Player(BaseEntity):
    def __init__(self, app, name='player'):
        super().__init__(app, name)

        self.group.change_layer(self, CENTER.y)

        self.rect = self.image.get_rect(center=CENTER)

        self.offset = vec2(0)
        self.inc = vec2(0)
        self.angle = 0
        self.diag_move_corr = 1 / math.sqrt(2)

    def control(self):
        self.inc = vec2(0)
        speed = PLAYER_SPEED * self.app.delta_time
        rotate_speed = PLAYER_ROTATE_SPEED * self.app.delta_time

        key_state = pg.key.get_pressed()

        if key_state[pg.K_LEFT]:
            self.angle += rotate_speed
        if key_state[pg.K_RIGHT]:
            self.angle += -rotate_speed

        if key_state[pg.K_w]:
            self.inc += vec2(0, -speed).rotate_rad(-self.angle)
        if key_state[pg.K_s]:
            self.inc += vec2(0, +speed).rotate_rad(-self.angle)
        if key_state[pg.K_a]:
            self.inc += vec2(-speed, 0).rotate_rad(-self.angle)
        if key_state[pg.K_d]:
            self.inc += vec2(+speed, 0).rotate_rad(-self.angle)

        if self.inc:
            self.inc *= self.diag_move_corr

    def update(self):
        super().update()
        self.control()
        self.move()

    def move(self):
        self.offset += self.inc
