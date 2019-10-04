import kivy
from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen


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



class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='Email id: '))
        self.email = TextInput(multiline=False)
        self.add_widget(self.email)

        self.add_widget(Label(text='Password: '))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)

        login = Button(text='Login')
        login.bind(on_press=self.callback)
        self.add_widget(login)
    
    def callback(self, instance):
        print('\n\nLogin as : '+ self.email.text +'\nPassword : '+ self.password.text)
    

class SignUp(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        
        self.add_widget(Label(text="Email Id:"))
        self.email = TextInput(multiline=False)
        self.add_widget(self.email)

        self.add_widget(Label(text="Password:"))
        self.password = TextInput(password=True,multiline=False)
        self.add_widget(self.password)

        self.add_widget(Label())

        self.signUp = Button(text="Sign Up")
        self.signUp.bind(on_press=self.signUpButton)
        self.add_widget(self.signUp)

    def signUpButton(self,instance):
        email = self.email.text
        password = self.password.text

        print(f"Saving details in database\nEmail: {email}\nPassword: {password}")

        
class HealthCare(App):
    def build(self):
        self.screenManager = ScreenManager()

        self.indexPage = index_main()
        indexScreen = Screen(name="Index")
        indexScreen.add_widget(self.indexPage)
        self.screenManager.add_widget(indexScreen)

        self.loginPage = LoginScreen()
        loginScreen = Screen(name="Login")
        loginScreen.add_widget(self.loginPage)
        self.screenManager.add_widget(loginScreen)

        self.signUpPage = SignUp()
        signUpScreen = Screen(name="SignUp")
        signUpScreen.add_widget(self.signUpPage)
        self.screenManager.add_widget(signUpScreen)

        return self.screenManager


      
if __name__ == "__main__":
    HealthCare().run()