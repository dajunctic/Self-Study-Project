from kivy.core.text import LabelBase
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.image import AsyncImage
from kivy.loader import Loader
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.utils import rgba

Window.size = (400, 720)


class NavBar(FakeRectangularElevationBehavior, MDFloatLayout):
    pass


class LoaderImage(AsyncImage):
    Loader.loading_image = 'assets/loader.gif'


class WallpaperApp(MDApp):
    def build(self):
        return Builder.load_file('main.kv')

    def search(self, search_text):
        if search_text != "":
            self.root.ids.search_label.text = search_text
            self.root.ids.page_manager.current = 'search_results'

    def change_color(self, instance):
        if instance in self.root.ids.values():
            current_id = list(self.root.ids.keys())[list(self.root.ids.values()).index(instance)]
            for i in range(1, 4):
                if f"nav_icon{i}" == current_id:
                    self.root.ids[f"nav_icon{i}"].text_color = rgba(253, 175, 177, 255)
                else:
                    self.root.ids[f"nav_icon{i}"].text_color = rgba(222, 222, 222, 255)


if __name__ == '__main__':
    LabelBase.register(name="MPoppins", fn_regular="fonts/Poppins-Medium.ttf")
    LabelBase.register(name="BPoppins", fn_regular="fonts/Poppins-Bold.ttf")
    WallpaperApp().run()
