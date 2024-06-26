from stacked_sprite import *
from random import uniform
from entity import Entity

P = 'player'
K = 'kitty'
A, B, C, D, E = 'van', 'tank', 'blue_tree', 'car', 'grass'

MAP = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, C, C, 0, C, C, 0, 0, 0],
    [0, 0, C, 0, K, E, 0, 0, 0, 0, 0],
    [0, C, C, A, 0, 0, 0, B, C, 0, 0],
    [0, 0, 0, D, 0, P, 0, E, C, 0, 0],
    [0, 0, C, 0, E, 0, E, D, C, 0, 0],
    [0, 0, C, 0, 0, C, C, C, 0, 0, 0],
    [0, 0, 0, E, 0, C, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

MAP_SIZE = MAP_WIDTH, MAP_HEIGHT = vec2(len(MAP), len(MAP[0]))
MAP_CENTER = MAP_SIZE / 2


class Scene:
    def __init__(self, app):
        self.app = app
        self.load_scene()

    def load_scene(self):
        random_rot: () = lambda: uniform(0, 360)
        rand_pos: () = lambda pos: pos + vec2(uniform(-0.25, 0.25))

        for j, row in enumerate(MAP):
            for i, name in enumerate(row):
                pos = vec2(i, j) + vec2(0.5)
                if name == 'player':
                    self.app.player.offset = pos * TILE_SIZE
                elif name == 'kitty':
                    Entity(self.app, name, pos)
                elif name == 'blue_tree':
                    TransparentStackedSprite(self.app, name=name, pos=rand_pos(pos), rot=random_rot())
                elif name:
                    StackedSprite(self.app, name=name, pos=rand_pos(pos), rot=random_rot())

    def get_closest_object_to_player(self):
        closest = sorted(self.app.transparent_objects, key=lambda e: e.dist_to_player)
        closest[0].alpha_trigger = True
        closest[1].alpha_trigger = True

    def update(self):
        self.get_closest_object_to_player()
