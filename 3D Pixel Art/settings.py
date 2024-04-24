import pygame as pg

vec2 = pg.math.Vector2

RES = WIDTH, HEIGHT = vec2(1280, 720)
CENTER = H_WIDTH, H_HEIGHT = RES // 2
TILE_SIZE = 200

PLAYER_SPEED = 0.5
PLAYER_ROTATE_SPEED = 0.0015

BG_COLOR = 'olivedrab'

NUM_ANGLES = 90  # multiple of 360 -> 24, 30, 36, 40, 45, 60, 72, 90, 120, 180

ENTITY_SPRITE_ATTRS = {
    'player': {
        'path': 'assets/entity/player/player.png',
        'num_layers': 7,
        'scale': 0.18,
        'y_offset': 0,
    },
    'kitty': {
        'path': 'assets/entity/cats/kitty.png',
        'num_layers': 8,
        'scale': 0.5,
        'y_offset': -20,
    }

}

STACKED_SPRITE_ATTRS = {
    'van': {
        'path': 'assets/stacked_sprites/van.png',
        'num_layers': 20,
        'scale': 4,
        'y_offset': -25,
    },
    'tank': {
        'path': 'assets/stacked_sprites/tank.png',
        'num_layers': 17,
        'scale': 6,
        'y_offset': -30,
    },
    'car': {
        'path': 'assets/stacked_sprites/car.png',
        'num_layers': 9,
        'scale': 8,
        'y_offset': -10,
    },
    'blue_tree': {
        'path': 'assets/stacked_sprites/blue_tree.png',
        'num_layers': 43,
        'scale': 5,
        'y_offset': -80,
    },
    'grass': {
        'path': 'assets/stacked_sprites/grass.png',
        'num_layers': 11,
        'scale': 4,
        'y_offset': -40,
        'outline': False,
    }
}
