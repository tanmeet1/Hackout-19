import kivy
kivy.require('1.10.0')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
#Builder.load_file('index_carousel.kv')

class index_main():
    def __init__(self,**kwargs):
        #super().__init__(**kwargs)
        self.carousel=Carousel()
        self.Box1=BoxLayout(orientation= 'vertical', spacing = 20)
        self.Box1.add_widget(Label(text="HealthCare"))
        self.carousel.direction = "right"
        for i in range(1, 5):
            src = "res/%s.jpg" % str(i)
            image = AsyncImage(source=src, allow_stretch=True)
            self.carousel.add_widget(image)
        self.carousel.loop = True
        Clock.schedule_interval(self.carousel.load_next,2)
        self.Box1.add_widget(self.carousel)


#class Login():

#class SignUp():


class HealthCare(App):
    def build(self):
        return index_main()

if __name__ == "__main__":
    HealthCare().run()