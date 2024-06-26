from settings import *


class Cache:
    def __init__(self):
        self.stacked_sprite_cache = {}
        self.entity_sprite_cache = {}
        self.viewing_angle = 360 // NUM_ANGLES
        self.outline_thickness = 5
        self.get_stacked_sprite_cache()
        self.get_entity_sprite_cache()

    def get_entity_sprite_cache(self):
        for sprite_name in ENTITY_SPRITE_ATTRS:
            self.entity_sprite_cache[sprite_name] = {
                'images': None,
            }
            attrs = ENTITY_SPRITE_ATTRS[sprite_name]
            images = self.get_layer_array(attrs)
            self.entity_sprite_cache[sprite_name]['images'] = images

    def get_stacked_sprite_cache(self):
        for obj_name in STACKED_SPRITE_ATTRS:
            self.stacked_sprite_cache[obj_name] = {
                'rotated_sprites': {},
            }
            attrs = STACKED_SPRITE_ATTRS[obj_name]
            layer_array = self.get_layer_array(attrs)
            self.run_prerender(obj_name, layer_array, attrs)

    def run_prerender(self, obj_name, layer_array, attrs):
        outline = attrs.get('outline', True)
        for angle in range(NUM_ANGLES):
            surf = pg.Surface(layer_array[0].get_size())
            surf = pg.transform.rotate(surf, angle * self.viewing_angle)
            sprite_surf = pg.Surface([surf.get_width(), surf.get_height()
                                      + attrs['num_layers'] * attrs['scale']])
            sprite_surf.fill('khaki')
            sprite_surf.set_colorkey('khaki')

            for ind, layer in enumerate(layer_array):
                layer = pg.transform.rotate(layer, angle * self.viewing_angle)
                sprite_surf.blit(layer, (0, ind * attrs['scale']))

            # outline
            if outline:
                outline_coors = pg.mask.from_surface(sprite_surf).outline()
                pg.draw.polygon(sprite_surf, 'black', outline_coors, self.outline_thickness)

            image = pg.transform.flip(sprite_surf, True, True)
            self.stacked_sprite_cache[obj_name]['rotated_sprites'][angle] = image

    def get_layer_array(self, attrs):
        # load sprite sheet
        sprite_sheet = pg.image.load(attrs['path']).convert_alpha()

        # scaling
        sprite_sheet = pg.transform.scale(sprite_sheet, vec2(sprite_sheet.get_size()) * attrs['scale'])
        sheet_width = sprite_sheet.get_width()
        sheet_height = sprite_sheet.get_height()
        sprite_height = sheet_height // attrs['num_layers']

        # new height to prevent error
        sheet_height = sprite_height * attrs['num_layers']

        # get sprites
        layer_array = []
        for y in range(0, sheet_height, sprite_height):
            sprite = sprite_sheet.subsurface((0, y, sheet_width, sprite_height))
            layer_array.append(sprite)

        return layer_array[::-1]
