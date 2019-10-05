import kivy
import pandas as pd
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


class index_main(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        Box1=BoxLayout(orientation= 'vertical', spacing = 20)
        Box1.add_widget(Label(text="HealthCare"))
        carousel = Carousel(direction='right')

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
        print("Login Clicked")
        app.screenManager.current = "Login"

    def Signup_Callback(self, instance):
        print("Signup Clicked")
        app.screenManager.current = "SignUp"


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

        back = Button(text='Return to Main Menu')
        back.bind(on_press=self.retback)
        self.add_widget(back)
    
    def callback(self, instance):
        print('\n\nLogin as : '+ self.email.text +'\nPassword : '+ self.password.text)
        app.screenManager.current = "AfterLogin"

    def retback(self,instance):
        app.screenManager.current = "Index"

    

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

        self.signUp = Button(text="Sign Up")
        self.signUp.bind(on_press=self.signUpButton)
        self.add_widget(self.signUp)

        back = Button(text='Return to Main Menu')
        back.bind(on_press=self.retback)
        self.add_widget(back)

    def signUpButton(self,instance):
        email = self.email.text
        password = self.password.text

        print(f"Saving details in database\nEmail: {email}\nPassword: {password}")

    def retback(self,instance):
        app.screenManager.current = "Index"


class GetData(BoxLayout):

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.article_read = pd.read_csv("res/Singledata User Info.csv",names =['UID','Name','Time','Height','Weight','Allergy'])
        self.add_widget(Label(text="Patient Data"))
        self.orientation = 'vertical'
        # Grid1 = GridLayout(cols = 2)
        # Grid1.add_widget(Label(text = "Enter the Patient ID : "))
        # Grid1.uid = TextInput(multiline = False)
        # Grid1.add_widget(Grid1.pid)

        #self.add_widget(Grid1) 
        
        #self.submit = Button(text="Submit",on_press=self.submit_pid)
        #self.add_widget(self.submit)
        #self.add_widget(Label(text=str(article_read.UID[article_read.UID == self.__class__.pid])))
        # self.add_widget(Label(text=str(article_read[article_read.name[article_read.uid == self.__class__.pid]])))
        # self.add_widget(Label(text=str(article_read[article_read.time[article_read.uid == self.__class__.pid]])))
        # self.add_widget(Label(text=str(article_read[article_read.height[article_read.uid == self.__class__.pid]])))
        # self.add_widget(Label(text=str(article_read[article_read.weight[article_read.uid == self.__class__.pid]])))
        # self.add_widget(Label(text=str(article_read[article_read.allergy[article_read.uid == self.__class__.pid]])))

    # def submit_pid(self,instance):
    #     self.Grid1.pid = self.Grid1.uid.text
    def update_info(self,pid):
        print(self.article_read.head())
        self.add_widget(Label(text=str(self.article_read.UID[self.article_read.UID == pid])))
        self.add_widget(Label(text=str(self.article_read.Name[self.article_read.UID == pid])))
        self.add_widget(Label(text=str(self.article_read.Time[self.article_read.UID == pid])))
        self.add_widget(Label(text=str(self.article_read.Height[self.article_read.UID == pid])))
        self.add_widget(Label(text=str(self.article_read.Weight[self.article_read.UID == pid])))
        self.add_widget(Label(text=str(self.article_read.Allergy[self.article_read.UID == pid])))
        #print(self.__class__.pid)


class ScanUID(BoxLayout):
    
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.Grid1 = GridLayout(cols = 2)
        self.Grid1.add_widget(Label(text = "Enter the Patient ID : "))
        self.userID = TextInput(multiline = False)
        self.Grid1.add_widget(self.userID)

        self.add_widget(self.Grid1) 
        
        self.submit = Button(text="Submit",on_press=self.submit_pid)
        self.add_widget(self.submit)
    
    def submit_pid(self,instance):
        pid = self.userID.text
        print(pid)
        app.dataPage.update_info(pid)
        app.screenManager.current = "GetData"


class AfterLogin(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        view = Button(text="View Patient Data")
        view.bind(on_press=self.getuid)
        self.add_widget(view)

        add = Button(text="Add New Patient")
        view.bind(on_press=self.adduid)
        self.add_widget(add)

    def getuid(self,instance):
        app.screenManager.current = "GetUID"
    def adduid(self,instance):
        pass

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

        self.dataPage = GetData()
        dataScreen = Screen (name = "GetData")
        dataScreen.add_widget(self.dataPage)
        self.screenManager.add_widget(dataScreen)

        self.afterLoginPage = AfterLogin()
        afterLoginScreen  = Screen (name = "AfterLogin")
        afterLoginScreen.add_widget(self.afterLoginPage)
        self.screenManager.add_widget(afterLoginScreen)

        self.getUIDPage = ScanUID()
        getUIDScreen  = Screen (name = "GetUID")
        getUIDScreen.add_widget(self.getUIDPage)
        self.screenManager.add_widget(getUIDScreen)

        return self.screenManager


      
if __name__ == "__main__":
    app = HealthCare()
    app.run()