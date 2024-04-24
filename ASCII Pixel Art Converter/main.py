import pygame as pg
import cv2


class ArtConverter:
    def __init__(self, path="img/car.jpg", font_size=12):
        pg.init()

        self.path = path
        self.cv2_image = None
        self.image = self.get_image()
        self.RESOLUTION = self.WIDTH, self.HEIGHT = self.image.shape[0], self.image.shape[1]
        self.surface = pg.display.set_mode(self.RESOLUTION)
        self.clock = pg.time.Clock()

        self.ASCII_CHARS = '.",:;!~+-xmo*#W&8@'
        self.ASCII_COEFF = 255 // (len(self.ASCII_CHARS) - 1)

        self.font = pg.font.SysFont('Courier', font_size, bold=True)
        self.CHAR_STEP = int(font_size * 0.6)
        self.RENDERED_ASCII_CHARS = [self.font.render(char, False, 'white') for char in self.ASCII_CHARS]

    def get_image(self):
        self.cv2_image = cv2.imread(self.path)
        transposed_image = cv2.transpose(self.cv2_image)
        gray_image = cv2.cvtColor(transposed_image, cv2.COLOR_BGR2GRAY)
        return gray_image

    def draw_cv2_image(self):
        resized_cv2_image = cv2.resize(self.cv2_image, (320, 180), interpolation=cv2.INTER_AREA)
        cv2.imshow('img', resized_cv2_image)

    def draw_converted_image(self):
        char_indices = self.image // self.ASCII_COEFF

        for x in range(0, self.WIDTH, self.CHAR_STEP):
            for y in range(0, self.HEIGHT, self.CHAR_STEP):
                char_index = char_indices[x, y]
                if char_index:
                    self.surface.blit(self.RENDERED_ASCII_CHARS[char_index], (x, y))

    def draw(self):
        self.surface.fill('black')
        self.draw_converted_image()
        self.draw_cv2_image()

    def save_image(self):
        pygame_image = pg.surfarray.array3d(self.surface)
        cv2_img = cv2.transpose(pygame_image)
        cv2.imwrite('converted_image.jpg', cv2_img)
        print("New image saved!")

    def run(self):
        while True:
            self.draw()

            for i in pg.event.get():
                if i.type == pg.QUIT:
                    exit()

                elif i.type == pg.KEYDOWN:
                    if i.key == pg.K_s:
                        self.save_image()

            pg.display.set_caption(str(round(self.clock.get_fps(), 2)))
            pg.display.flip()
            self.clock.tick()


if __name__ == '__main__':
    app = ArtConverter()
    app.run()
