#from Galaxy import MainWidget
from kivy.uix.relativelayout import RelativeLayout

def keyboard_closed(self):
    self._keyboard.unbind(on_key_down=self._on_keyboard_down)
    self._keyboard.unbind(on_key_up=self._on_keyboard_up)
    self._keyboard = None

def on_keyboard_down(self, keyboard, keycode, text, modifiers):
    if keycode[1] == 'left':
        self.current_speed_x = self.SPEED_X
        self.press_left = True
    elif keycode[1] == 'right':
        self.current_speed_x = -self.SPEED_X
        self.press_right = True

    return True
    
def on_keyboard_up(self, keyboard, keycode):
    if keycode[1] == 'left':
        self.press_left = False
    elif keycode[1] == 'right':
        self.press_right = False
    
    if not self.press_left and not self.press_right:
        self.current_speed_x = 0
    return True

def on_touch_down(self, touch):
    if not self.state_game_over and self.state_game_has_started:
        if touch.x < self.width/2:
            self.current_speed_x = self.SPEED_X
            self.press_left = True
        else:
            self.current_speed_x = -self.SPEED_X
            self.press_right = True
    
    return super(RelativeLayout, self).on_touch_down(touch)

def on_touch_up(self, touch):
    if touch.x < self.width/2:
        self.press_left = False
    else:
        self.press_right = False
        
    if not self.press_left and not self.press_right:
        self.current_speed_x = 0
    