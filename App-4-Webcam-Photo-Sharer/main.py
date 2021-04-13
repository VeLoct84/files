from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder


Builder.load_file("frontend.kv")

class CameraScreen(Screen):
    def start():
        pass

    def stop():
        pass

    def capture():
        pass

class ImageScree(Screen):
    pass

class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


MainApp().run()
