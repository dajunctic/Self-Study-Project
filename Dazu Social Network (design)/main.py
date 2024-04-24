from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.button import Button
from kivy.uix.image import Image

Window.size = (400, 720)


class ProfileCard(MDFloatLayout, FakeRectangularElevationBehavior):
    pass


class SearchBar(MDFloatLayout, FakeRectangularElevationBehavior):
    pass


class ProfileButton(Image, Button):
    pass


class DazuApp(MDApp):
    def build(self):
        self.title = 'Dazu'
        self.icon = 'assets/icon.png'
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'BlueGray'

        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file('main.kv'))
        screen_manager.add_widget(Builder.load_file('login.kv'))
        screen_manager.add_widget(Builder.load_file('signup.kv'))
        screen_manager.add_widget(Builder.load_file('homepage.kv'))
        screen_manager.add_widget(Builder.load_file('profile.kv'))
        screen_manager.add_widget(Builder.load_file('conversation.kv'))

        return screen_manager


if __name__ == "__main__":
    DazuApp().run()
