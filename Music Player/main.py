import kivy.properties
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.core.text import LabelBase
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.animation import Animation
from kivy.core.audio import SoundLoader, Sound
from kivy.uix.floatlayout import FloatLayout
import kivy.properties
import pygame
from mutagen.mp3 import MP3

Window.size = (390, 700)


class MusicPlayer(MDApp):
    def build(self):
        self.title = 'Dazu Music'
        self.icon = 'assets/icon.png'
        return Builder.load_file('main.kv')


class SongCover(BoxLayout):
    angle = NumericProperty()
    anim = Animation(angle=-360, d=4, t='linear')
    anim += Animation(angle=0, d=0, t='linear')
    anim.repeat = True

    song = None
    song_file = 'A Man Without Love - Engelbert Humperdin.mp3'
    name = StringProperty()
    artist = StringProperty()
    length = StringProperty()
    current_length = StringProperty()

    music_start = False

    progress = ObjectProperty()
    play_button = ObjectProperty()

    start_time = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # self.song = SoundLoader.load('A Man Without Love - Engelbert Humperdin.mp3')
        self.get_info()

        kivy.properties.Clock.schedule_interval(self.update, 1.0/10)
        # kivy.properties.Clock.schedule_interval(self.count, 0.2)

    def get_info(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.song_file)
        self.anim.start(self)
        self.song = MP3(self.song_file)

        file_name = str(list(self.song_file.split('-'))[0])
        artist_name = str(list(self.song_file.split('-'))[-1])

        self.name = str(list(file_name.split('\\'))[-1])
        self.artist = str(list(artist_name.split('.'))[0])

        mlength = format(int(self.song.info.length)//60, '02d')
        slength = format(int(self.song.info.length) % 60, '02d')
        self.length = str(f'{mlength}:{slength}')

    def play(self, widget):
        if widget.icon == 'play-outline':
            widget.icon = 'pause'

            if not self.music_start:
                self.music_start = True
                # self.start_time = 0

            pygame.mixer.music.play(0, self.start_time)
        else:
            widget.icon = 'play-outline'
            pygame.mixer.music.pause()

    def replay(self):
        self.progress.value = pygame.mixer.music.get_pos() / 1000
        pygame.mixer.music.stop()
        pygame.mixer.music.play()

        self.progress.value = 0
        self.start_time = 0
        self.music_start = True
        self.play_button.icon = 'pause'

    def update(self, dt):
        if self.music_start:
            self.progress.max = int(self.song.info.length)

            current_length = self.start_time + pygame.mixer.music.get_pos() / 1000
            if abs(self.progress.value - current_length) > 1:
                self.start_time = self.progress.value
                pygame.mixer.music.stop()
                pygame.mixer.music.play(0, self.progress.value)
            else:
                self.progress.value = current_length

            if not pygame.mixer.music.get_busy():
                self.music_start = False
                self.play_button.icon = 'play-outline'
        else:
            self.start_time = self.progress.value

        mclength = format(int(self.start_time + pygame.mixer.music.get_pos() / 1000) // 60, '02d')
        sclength = format(int(self.start_time + pygame.mixer.music.get_pos() / 1000) % 60, '02d')
        self.current_length = str(f'{mclength}:{sclength}')


if __name__ == '__main__':
    LabelBase.register('BPoppins', fn_regular='fonts/Poppins-Bold.ttf')
    LabelBase.register('MPoppins', fn_regular='fonts/Poppins-Medium.ttf')
    MusicPlayer().run()
