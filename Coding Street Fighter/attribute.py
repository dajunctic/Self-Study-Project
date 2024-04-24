import pygame

pygame.init()
TITLE = 'Coding Street Fighter'

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

FPS = 60

surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(TITLE)

HERO_KNIGHT_ANIMATION_STEPS = [11, 3, 3, 11, 8, 4, 7, 7]
HERO_KNIGHT_SIZE = 180
HERO_KNIGHT_SCALE = 4
HERO_KNIGHT_OFFSET = [75, 50]
HERO_KNIGHT_ATTACK_FRAME = [4, 4]
HERO_KNIGHT_DATA = [HERO_KNIGHT_SIZE, HERO_KNIGHT_SCALE, HERO_KNIGHT_OFFSET, HERO_KNIGHT_ATTACK_FRAME]


hero_knight_sheet = {
    'idle': pygame.image.load('assets/image/Hero Knight/Sprites/Idle.png').convert_alpha(),
    'jump': pygame.image.load('assets/image/Hero Knight/Sprites/Jump.png').convert_alpha(),
    'fall': pygame.image.load('assets/image/Hero Knight/Sprites/Fall.png').convert_alpha(),
    'death': pygame.image.load('assets/image/Hero Knight/Sprites/Death.png').convert_alpha(),
    'run': pygame.image.load('assets/image/Hero Knight/Sprites/Run.png').convert_alpha(),
    'take_hit': pygame.image.load('assets/image/Hero Knight/Sprites/Take Hit.png').convert_alpha(),
    'attack1': pygame.image.load('assets/image/Hero Knight/Sprites/Attack1.png').convert_alpha(),
    'attack2': pygame.image.load('assets/image/Hero Knight/Sprites/Attack2.png').convert_alpha()
}

EVIL_WIZARD_2_ANIMATION_STEPS = [8, 2, 2, 7, 8, 3, 8, 8]
EVIL_WIZARD_2_SIZE = 250
EVIL_WIZARD_2_SCALE = 3.4
EVIL_WIZARD_2_OFFSET = [104, 91]
EVIL_WIZARD_2_ATTACK_FRAME = [4, 4]
EVIL_WIZARD_2_DATA = [EVIL_WIZARD_2_SIZE, EVIL_WIZARD_2_SCALE, EVIL_WIZARD_2_OFFSET, EVIL_WIZARD_2_ATTACK_FRAME]

evil_wizard_2_sheet = {
    'idle': pygame.image.load('assets/image/EVil Wizard 2/Sprites/Idle.png').convert_alpha(),
    'jump': pygame.image.load('assets/image/EVil Wizard 2/Sprites/Jump.png').convert_alpha(),
    'fall': pygame.image.load('assets/image/EVil Wizard 2/Sprites/Fall.png').convert_alpha(),
    'death': pygame.image.load('assets/image/EVil Wizard 2/Sprites/Death.png').convert_alpha(),
    'run': pygame.image.load('assets/image/EVil Wizard 2/Sprites/Run.png').convert_alpha(),
    'take_hit': pygame.image.load('assets/image/EVil Wizard 2/Sprites/Take Hit.png').convert_alpha(),
    'attack1': pygame.image.load('assets/image/EVil Wizard 2/Sprites/Attack1.png').convert_alpha(),
    'attack2': pygame.image.load('assets/image/EVil Wizard 2/Sprites/Attack2.png').convert_alpha()
}

