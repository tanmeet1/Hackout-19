import kivy
kivy.require('1.10.0')
from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class index_main(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        Box1=BoxLayout(orientation= 'vertical', spacing = 20)
        Box1.add_widget(Label(text="HealthCare"))
        carousel = Carousel(direction='left')

        for i in range(1, 5):
            src = "res/%s.jpg" % str(i)
            image = AsyncImage(source=src, allow_stretch=True)
            carousel.add_widget(image)
        carousel.loop = True
        Clock.schedule_interval(carousel.load_next,2)
        Box1.add_widget(carousel)

        box2 = BoxLayout(spacing=20)
        Login =  Button(text='Login', on_press=self.Login_Callback)
        Signup =  Button(text='SignUp', on_press=self.Signup_Callback)
        box2.add_widget(Login)
        box2.add_widget(Signup)
        Box1.add_widget(box2)
        
        self.add_widget(Box1)
    
    def Login_Callback(self, instance):
        print("Login Complete")

    def Signup_Callback(self, instance):
        print("Signup Complete")


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
        return index_main()

      
if __name__ == "__main__":
    HealthCare().run()