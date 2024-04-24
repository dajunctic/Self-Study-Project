from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import ObjectProperty

class MenuWidget(RelativeLayout):
    def on_touch_down(self, touch):
        if self.opacity == 0:
            return False
        return super().on_touch_down(touch)
    

class HighScore(RelativeLayout):
    high_score_display = None
    high_score = []
    
    # box_score = ObjectProperty()
    box_score = BoxLayout()
    
    def __init__(self, **kw):
        super().__init__(**kw)
        self.opacity = 0
        # pass
        self.init()
        
        self.box_score.orientation = 'vertical'
        self.box_score.size_hint = (1, .4)
        self.box_score.pos_hint = {'center_y': .5}
        for i in range(5):
            l = Label(text=str(self.high_score[i]), font_name='fonts/Eurostile.ttf', font_size=35)
            self.box_score.add_widget(l)
            
        self.add_widget(self.box_score)
            
    def init(self):
            
        with open("sources/high_score.txt") as f:
            self.high_score = f.read().splitlines()

        for i in range(len(self.high_score)):
            self.high_score[i] = int(self.high_score[i])
    
    
    def update(self, value):
        
        self.high_score.append(value)
        self.high_score.sort(reverse=True)

        self.box_score.clear_widgets()
        for i in range(5):
            l = Label(text=str(self.high_score[i]), font_name='fonts/Eurostile.ttf', font_size=35)
            self.box_score.add_widget(l)

        with open('sources/high_score.txt', 'w') as f:
            f.write('')
        with open('sources/high_score.txt', 'a') as f:
            for i in range(5):
                f.write(str(self.high_score[i]) + '\n')
        
        #print(self.high_score_text)

    def reset(self):
        with open('sources/high_score.txt', 'w') as f:
            f.write('')
        with open('sources/high_score.txt', 'a') as f:
            for i in range(5):
                f.write('0\n')
        
        self.init()
        self.box_score.clear_widgets()
        for i in range(5):
            l = Label(text=str(self.high_score[i]), font_name='fonts/Eurostile.ttf', font_size=35)
            self.box_score.add_widget(l)
        
        
    def on_touch_down(self, touch):
        if self.opacity == 0:
            return False
        return super().on_touch_down(touch)