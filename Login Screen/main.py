from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
Window.size = (400, 720)


class LoginApp(MDApp):
    def build(self):
        self.title = 'Login App'
        self.icon = 'assets/icon.png'
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'BlueGray'

        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file('main.kv'))
        screen_manager.add_widget(Builder.load_file('login.kv'))
        screen_manager.add_widget(Builder.load_file('signup.kv'))

        return screen_manager


if __name__ == "__main__":
    LoginApp().run()
