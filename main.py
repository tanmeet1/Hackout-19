import kivy
from kivy.app import App

class IndexPage():

class Login():

class SignUp():


class HealthCare(App):
    def build(self):
        return IndexPage()

if __name__ == "__main__":
    HealthCare().run()