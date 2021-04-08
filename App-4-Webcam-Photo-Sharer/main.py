from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

import requests
import wikipedia

Builder.load_file("frontend.kv")

class FirstScreen(Screen):
    def get_link(self):
        # get user query 
        query = self.manager.current_screen.ids.user_query.text
        # get search from wikipedia and url for image 
        page = wikipedia.page(query)
        image_link = page.images[0]
        return image_link

    def get_summary(self):
        query = self.manager.current_screen.ids.user_query.text
        # get search from wikipedia and url for image 
        page = wikipedia.page(query)
        summary = page.summary
        return summary

    def download_image(self):
        # download the images 
        req = requests.get(self.get_link())
        image_path = "files/download.jpg"
        # write bytes format 
        with open(image_path, "wb") as file:
            file.write(req.content)
        return image_path

    def set_images(self):
        # set the image to the Image widget
        self.manager.current_screen.ids.img123.source = self.download_image()

    def info(self):
        self.ids.summary.text = self.get_summary()

class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


MainApp().run()
