from enum import Enum

import pygame.time

from attribute import *


class Action(Enum):
    IDLE = 0
    JUMP = 1
    FALL = 2
    DEATH = 3
    RUN = 4
    TAKE_HIT = 5
    ATTACK_1 = 6
    ATTACK_2 = 7


class Fighter:
    def __init__(self, x, y, player, flip, data, sprite_sheet, animation_steps):
        self.size = data[0]
        self.image_scale = data[1]
        self.offset = data[2]

        self.actions = ['idle', 'jump', 'fall', 'death', 'run', 'take_hit', 'attack1', 'attack2']
        self.animation_list = self.load_images(sprite_sheet, animation_steps)
        self.animation_steps = animation_steps
        self.action = 0
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.image = self.animation_list[self.action][self.frame_index]

        # player is the value using the control correspond
        self.player = player
        self.rect = pygame.Rect((x, y, 120, 260))

        # flip False if fighter in right direct, True if in left direct
        self.flip = flip

        self.running = False
        self.jump = False

        self.speed_y = 0
        self.speed_x = .01
        self.gravity = .001

        self.dx = 0.0
        self.dy = 0.0

        self.attacking = False
        self.attacking_check = False
        self.attacking_base = 2.8  # Base attack in attack rectangle
        self.attacking_frame = data[3]
        self.attack_type = 0
        self.attacking_cooldown = 0

        self.hit = False
        self.health = 100
        self.alive = True

    def load_images(self, sprite_sheet, animation_steps):
        # extract image from sprite sheet
        animation_list = []

        for animation, act in zip(animation_steps, self.actions):
            temp_img_list = []
            for x in range(animation):
                temp_img = sprite_sheet[act].subsurface(x * self.size, 0, self.size, self.size)

                temp_scale_img = pygame.transform.scale(temp_img, (self.size * self.image_scale,
                                                                   self.size * self.image_scale))
                temp_img_list.append(temp_scale_img)

            animation_list.append(temp_img_list)

        return animation_list

    def move(self, target):
        self.dx = 0.0
        self.dy = 0.0

        self.running = False
        self.attack_type = 0

        # get keypresses
        self.control(target)

        # Apply gravity
        self.speed_y += self.gravity
        self.dy += self.speed_y

        # Ensure player stays on the screen
        if self.rect.left + self.dx * SCREEN_WIDTH < 0:
            self.dx = 0 - self.rect.left / SCREEN_WIDTH
        if self.rect.right + self.dx * SCREEN_WIDTH > SCREEN_WIDTH:
            self.dx = 1 - self.rect.right / SCREEN_WIDTH

        if self.rect.bottom + self.dy * SCREEN_HEIGHT > 0.9 * SCREEN_HEIGHT:
            self.speed_y = 0
            self.jump = False
            self.dy = 0.9 - self.rect.bottom / SCREEN_HEIGHT

        # Apply attack cooldown
        if self.attacking_cooldown > 0:
            self.attacking_cooldown -= 1

        # Update player position
        self.rect.x += self.dx * SCREEN_WIDTH
        self.rect.y += self.dy * SCREEN_HEIGHT

    def attack(self, target):
        if self.attacking_cooldown == 0:

            self.attacking = True
            self.attacking_check = True

    def attacking_result(self, target):
        attacking_rect = pygame.Rect(self.rect.centerx - self.attacking_base * self.rect.width * self.flip,
                                     self.rect.y, self.attacking_base * self.rect.width, self.rect.height)

        if attacking_rect.colliderect(target.rect):
            target.health -= 10
            target.hit = True

        # pygame.draw.rect(surface, (0, 255, 0), attacking_rect)

    def update(self, target):
        # check what action the player is performing
        if self.health <= 0:
            self.health = 0
            self.alive = False
            self.update_action(Action.DEATH.value)
        elif self.hit:
            self.update_action(Action.TAKE_HIT.value)
        elif self.attacking:
            if self.attack_type == 1:
                self.update_action(Action.ATTACK_1.value)
            else:
                self.update_action(Action.ATTACK_2.value)
        elif self.jump:
            self.update_action(Action.JUMP.value)
        elif self.running:
            self.update_action(Action.RUN.value)
        else:
            self.update_action(Action.IDLE.value)

        animation_cooldown = 75  # milli second

        self.image = self.animation_list[self.action][self.frame_index]

        # check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.frame_index += 1

            self.update_time = pygame.time.get_ticks()

            if self.attacking and self.frame_index == self.attacking_frame[self.attack_type - 1]:
                self.attacking_result(target)

            if self.frame_index >= self.animation_steps[self.action]:
                # if the player is dead and end the animation
                if not self.alive:
                    self.frame_index = self.animation_steps[self.action] - 1
                else:
                    self.frame_index = 0

                    # check if an attack was executed
                    if self.action in (Action.ATTACK_1.value, Action.ATTACK_2.value):
                        self.attacking = False
                        self.attacking_cooldown = 30

                    # check if damage was taken
                    if self.action == Action.TAKE_HIT.value:
                        self.hit = False
                        # if the player was in the middle of an attack, then the attack is stopped
                        self.attacking = False
                        self.attacking_check = False
                        self.attacking_cooldown = 30

    def update_action(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def draw(self):
        # pygame.draw.rect(surface, (255, 0, 0), self.rect)

        img = pygame.transform.flip(self.image, self.flip, False)
        surface.blit(img, (self.rect.x - (self.offset[0] * self.image_scale),
                           self.rect.y - (self.offset[1] * self.image_scale)))

    def control(self, target):
        key = pygame.key.get_pressed()
        if self.player == 1:

            # can only perform other actions if not currently attacking

            if not self.attacking and self.alive:
                # movement
                if key[pygame.K_a]:
                    self.dx = -self.speed_x
                    self.flip = True
                    self.running = True
                if key[pygame.K_d]:
                    self.dx = self.speed_x
                    self.flip = False
                    self.running = True

                # jump
                if key[pygame.K_w] and not self.jump:
                    self.speed_y = -0.032
                    self.jump = True

                # attack
                if key[pygame.K_r] or key[pygame.K_t]:

                    # determine which attack type was used
                    if key[pygame.K_r]:
                        self.attack_type = 1
                    if key[pygame.K_t]:
                        self.attack_type = 2

                    self.attack(target)

        if self.player == 2:

            # can only perform other actions if not currently attacking

            if not self.attacking and self.alive:
                # movement
                if key[pygame.K_LEFT]:
                    self.dx = -self.speed_x
                    self.flip = True
                    self.running = True
                if key[pygame.K_RIGHT]:
                    self.dx = self.speed_x
                    self.flip = False
                    self.running = True

                # jump
                if key[pygame.K_UP] and not self.jump:
                    self.speed_y = -0.032
                    self.jump = True

                # attack
                if key[pygame.K_PERIOD] or key[pygame.K_SLASH]:

                    # determine which attack type was used
                    if key[pygame.K_PERIOD]:
                        self.attack_type = 1
                    if key[pygame.K_SLASH]:
                        self.attack_type = 2
                    self.attack(target)
