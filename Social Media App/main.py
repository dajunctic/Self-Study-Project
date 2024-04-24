from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager

Window.size = (400, 720)


class ProfileCard(MDFloatLayout, FakeRectangularElevationBehavior):
    pass


class SearchBar(MDFloatLayout, FakeRectangularElevationBehavior):
    pass


class ProfileButton(Image, Button):
    pass


class SocialMediaApp(MDApp):
    def build(self):
        self.title = "Social Media"

        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file('conversation.kv'))
        screen_manager.add_widget(Builder.load_file('homepage.kv'))
        screen_manager.add_widget(Builder.load_file('profile.kv'))

        return screen_manager


if __name__ == '__main__':
    SocialMediaApp().run()

