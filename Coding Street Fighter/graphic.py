import pygame


def draw_rect_alpha(surface, color, rect):
    shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
    surface.blit(shape_surf, rect)


def draw_image(screen, image, x=0, y=0):
    screen.blit(image, (x, y))


class Image:
    def __init__(self, path):
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.path = path
        self.image = self.load()

    def load(self):
        return pygame.image.load(self.path)

    def set_rect(self, rect):
        self.rect = rect

    def scale(self, size_x, size_y):
        self.image = pygame.transform.scale(self.image, (size_x, size_y))

    def show(self, screen):
        draw_image(screen, self.image, self.rect.x, self.rect.y)


# Text #
DefaultFont = "Data/font/NikkyouSans-mLKax.ttf";
DefaultSize = 32;
DefaultColor = (255, 255, 255);


class Text:
    font = DefaultFont
    size = DefaultSize
    color = DefaultColor
    rect = pygame.Rect(0, 0, 0, 0)

    def set_size(self, size):
        self.size = size;

    def set_rect(self, obj):
        self.rect.x = obj.x
        self.rect.y = obj.y
        self.rect.w = obj.w
        self.rect.h = obj.h

    def set_font(self, font):
        self.font = font

    def set_color(self, color):
        self.color = color

    def show(self, screen, text):
        large_text = pygame.font.Font(self.font, self.size)

        text_surface = large_text.render(text, True, self.color)
        text_rect = text_surface.get_rect()

        text_rect.center = (self.rect.x + self.rect.w / 2, self.rect.y + self.rect.h / 2)
        screen.blit(text_surface, text_rect)


class Animation(pygame.sprite.Sprite):
    def __init__(self, x, y, path, frame):
        super().__init__()
        self.sprite_count = frame
        self.current_sprite = 0

        self.sprites = []
        self.load_sprites(path)
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]

    def load_sprites(self, path):
        path = "Data/img/" + path
        for i in range(self.sprite_count):
            te = str(i + 1)
            for i in range(3 - len(te)):
                te = '0' + te
            self.sprites.append(pygame.image.load(path + te + ".png"))

    def update(self, speed):
        self.current_sprite += speed
        self.current_sprite %= self.sprite_count

        self.image = self.sprites[int(self.current_sprite)]
