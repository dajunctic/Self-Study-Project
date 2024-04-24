import pygame.time

from fighter import Fighter
from attribute import *


def draw_health_bar(health, x, y):
    pygame.draw.rect(surface, (255, 255, 255), (x - 2, y - 2, SCREEN_WIDTH * .4 + 4, SCREEN_HEIGHT * .05 + 4))
    pygame.draw.rect(surface, (255, 0, 0), (x, y, SCREEN_WIDTH * .4, SCREEN_HEIGHT * .05))
    pygame.draw.rect(surface, (255, 255, 0), (x, y, SCREEN_WIDTH * .4 * health / 100, SCREEN_HEIGHT * .05))


def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    surface.blit(img, (x, y))


class Gameplay:
    bg = pygame.image.load('assets/image/arena.jpg')
    fighter_1 = None
    fighter_2 = None

    def __init__(self):
        self.init_fighter()

        # Gameplay Variable
        self.intro_count = 3
        self.last_count_update = pygame.time.get_ticks()

        self.count_font = pygame.font.Font('fonts/Turok.otf', 120)
        self.score_font = pygame.font.Font('fonts/Turok.otf', 30)
        self.victory_font = pygame.font.Font('fonts/Turok.otf', 150)
        self.victory_text = 'VICTORY'

        self.score = [0, 0]
        self.round_over = False
        self.ROUND_OVER_COOLDOWN = 5000
        self.round_over_time = pygame.time.get_ticks()

    def init_fighter(self):
        self.fighter_1 = Fighter(200, .9 * SCREEN_HEIGHT - 260, 1, False, HERO_KNIGHT_DATA, hero_knight_sheet,
                                 HERO_KNIGHT_ANIMATION_STEPS)
        self.fighter_2 = Fighter(940, .9 * SCREEN_HEIGHT - 260, 2, True, EVIL_WIZARD_2_DATA, evil_wizard_2_sheet,
                                 EVIL_WIZARD_2_ANIMATION_STEPS)

    def draw(self):
        scale_bg = pygame.transform.scale(self.bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
        surface.blit(scale_bg, (0, 0))

        draw_health_bar(self.fighter_1.health, SCREEN_WIDTH * .05, SCREEN_HEIGHT * .05)
        draw_health_bar(self.fighter_2.health, SCREEN_WIDTH * .55, SCREEN_HEIGHT * .05)

        # Update count_down
        if self.intro_count <= 0:
            self.fighter_1.move(self.fighter_2)
            self.fighter_2.move(self.fighter_1)
        else:
            # display counter time
            draw_text(str(self.intro_count), self.count_font, (255, 0, 0), SCREEN_WIDTH / 2 - 30, SCREEN_HEIGHT * .4)

            if pygame.time.get_ticks() - self.last_count_update >= 1000:
                self.intro_count -= 1
                self.last_count_update = pygame.time.get_ticks()

        self.fighter_1.update(self.fighter_2)
        self.fighter_2.update(self.fighter_1)

        self.fighter_1.draw()
        self.fighter_2.draw()

        # Check for player defeat
        if not self.round_over:
            if not self.fighter_1.alive:
                self.score[1] += 1
                self.round_over = True
                self.round_over_time = pygame.time.get_ticks()
            elif not self.fighter_2.alive:
                self.score[0] += 1
                self.round_over = True
                self.round_over_time = pygame.time.get_ticks()
        else:
            draw_text(self.victory_text, self.victory_font, (155, 0, 0), SCREEN_WIDTH / 2 - 300, SCREEN_HEIGHT * 0.4)

            if pygame.time.get_ticks() - self.round_over_time > self.ROUND_OVER_COOLDOWN:
                self.round_over = False
                self.intro_count = 3
                self.init_fighter()
                self.last_count_update = pygame.time.get_ticks()
