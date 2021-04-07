from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

Builder.load_file("frontend.kv")

class FirstScreen(Screen):
    def find_images(self):
       self.manager.current_screen.ids.img123.source = "files/island.jpg" 


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


MainApp().run()
