from gameplay import Gameplay
from enum import Enum


class Scene(Enum):
    MENU = 0,
    GAMEPLAY = 1


class Manager:
    game = Gameplay()

    def __init__(self):
        self.scene = Scene.GAMEPLAY

    def show(self, surface):
        self.game.show(surface)
