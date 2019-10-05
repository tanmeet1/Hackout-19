import kivy
import pandas as pd
import navbar
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
import datetime
import csv


class index_main(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        Grid1 = GridLayout(cols = 5,size_hint=(1.,0.07))
        
        index_page = Button(text="Index Main",size_hint=(.5,.5),size=(10,10))
        login_page = Button(text="Login",size_hint=(.5,.5),size=(10,10))
        signup_page = Button(text="Sign Up",size_hint=(.5,.5),size=(10,10))
        help_page = Button(text="Help",size_hint=(.5,.5),size=(10,10))
        about_page = Button(text ="About",size_hint=(.5,.5),size=(10,10))

        Grid1.add_widget(index_page)
        Grid1.add_widget(login_page)
        Grid1.add_widget(signup_page)
        Grid1.add_widget(help_page)
        Grid1.add_widget(about_page)
        Box1=BoxLayout(orientation= 'vertical', spacing = 20)
        Box1.add_widget(Label(text="HealthCare (For Doctors)",font_size='30sp'))
        carousel = Carousel(direction='right')

        for i in range(1, 5):
            src = "res/%s.jpg" % str(i)
            image = AsyncImage(source=src, allow_stretch=True)
            carousel.add_widget(image)
        carousel.loop = True
        Clock.schedule_interval(carousel.load_next,2)
        Box1.add_widget(carousel)

        Grid2 = GridLayout(cols = 2,size_hint=(1.0,0.3),pos_hint={'center x' : 0.7},pos=(10,10))
        Login = Button(text='Login', on_press=self.Login_Callback)
        Signup = Button(text='SignUp', on_press=self.Signup_Callback)
        Grid2.add_widget(Login)
        Grid2.add_widget(Signup)
        Box1.add_widget(Grid2)
        self.add_widget(Grid1)
        self.add_widget(Box1)

    def Login_Callback(self, instance):
        print("Login Clicked")
        app.screenManager.current = "Login"

    def Signup_Callback(self, instance):
        print("Signup Clicked")
        app.screenManager.current = "SignUp"


class Update_info(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.orientation='vertical'
        Gridr = navbar.nav()
        self.add_widget(Gridr)  
        Box1=BoxLayout(orientation= 'vertical', spacing = 20)
        Box1.add_widget(Label(text="Update Info"))
        grid = GridLayout(cols = 2)

        grid.add_widget(Label(text="User ID :",color=(1,0,0,1)))
        self.userID = TextInput(multiline=False)
        grid.add_widget(self.userID)
        grid.add_widget(Label(text="User Name :",color=(1,0,0,1)))
        self.userName = TextInput(multiline=False)
        grid.add_widget(self.userName)
        grid.add_widget(Label(text="Height :",color=(1,0,0,1)))
        self.hight = TextInput(multiline=False)
        grid.add_widget(self.hight)
        grid.add_widget(Label(text="Weight :",color=(1,0,0,1)))
        self.weight = TextInput(multiline=False)
        grid.add_widget(self.weight)
        grid.add_widget(Label(text="Allergy :",color=(1,0,0,1)))
        self.allergy = TextInput(multiline=False)
        grid.add_widget(self.allergy)
        
        self.Submit =  Button(text='Submit', on_press=self.Submit_Callback,color=(0,1,0,1))
        Back =  Button(text='Back', on_press=self.Back_Callback,color=(0,1,0,1))
        grid.add_widget(self.Submit)
        grid.add_widget(Back)

        Box1.add_widget(grid)
        self.add_widget(Box1)
    
    def Submit_Callback(self, instance):
        print("Submit Clicked")
        UserID_Data = int(self.userID.text)
        UserName_Data = str(self.userName.text)
        Height_data = str(self.hight.text)
        Weight_data = str(self.weight.text)
        Allergy_data = str(self.allergy.text)
        time_data = str(datetime.datetime.now())
        fields=[UserID_Data,UserName_Data,time_data,Height_data,Weight_data,Allergy_data]

        data = pd.read_csv("res/Singledata User Info.csv")
        
        #print(data.index)
        #print(data["UID"])
        data.set_index("UID",inplace=True)
        if UserID_Data in data.index:
            data.loc[UserID_Data]['Name'] = UserName_Data
            data.loc[UserID_Data]["Time"] = time_data
            data.loc[UserID_Data]["Height"] = Height_data
            data.loc[UserID_Data]["Weight"] = Weight_data
            data.loc[UserID_Data]["Allergy"] = Allergy_data
            data.to_csv("res/Singledata User Info.csv",index=True)
        else:
            with open("res/Singledata User Info.csv",'a') as dataN:
                writer = csv.writer(dataN)
                writer.writerow(fields)
            dataN.close()

        app.screenManager.current = "AfterLogin"

    def Back_Callback(self, instance):
        print("Back Clicked")
        app.screenManager.current = "AfterLogin"


class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.spacing = 150
        self.orientation='vertical'
        self.box1 = BoxLayout(spacing = 30, pos_hint={'top ':1}, size_hint=(1,0.15),padding=[0,20,0,0])
        self.box1.add_widget(Label(text='Email id: '))
        self.email = TextInput(multiline=False)
        self.box1.add_widget(self.email)

        self.box2 = BoxLayout(spacing = 30, pos_hint={'center_y':1}, size_hint=(1,0.15),padding=[0,0,0,20])

        self.box2.add_widget(Label(text='Password: '))
        self.password = TextInput(password=True, multiline=False)
        self.box2.add_widget(self.password)

        self.box3 = BoxLayout(spacing = 30, pos_hint={'center_x':0.5,'center_y':1.25}, size_hint=(1.0,0.20),padding=[0,0,0,80])

        self.login = Button(text='Login')
        self.login.bind(on_press=self.callback)
        self.box3.add_widget(self.login)

        back = Button(text='Return to Main Menu')
        back.bind(on_press=self.retback)
        self.box3.add_widget(back)

        self.add_widget(self.box1)
        self.add_widget(self.box2)
        self.add_widget(self.box3)
    
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
        #self.article_read = pd.read_csv("res/Singledata User Info.csv",names=["UID","Name","Time","Height","Weight","Allergy"])
        self.orientation='vertical'
        Gridr=navbar.nav()
        #navbar.rr(app,"Index","Login","SignUp")
        self.add_widget(Gridr)
        self.add_widget(Label(text="Patient Data"))
        self.orientation = 'vertical'
        # Grid1 = GridLayout(cols = 2)
        # Grid1.add_widget(Label(text = "Enter the Patient ID : "))
        # Grid1.uid = TextInput(multiline = False)
        # Grid1.add_widget(Grid1.pid)

        #self.add_widget(Grid1) 
        
    def update_info(self,pid):
        #print(self.article_read.UID)
        #print(self.article_read.UID == int(pid))
        self.article_read = pd.read_csv("res/Singledata User Info.csv")
        comp = self.article_read.UID == int(pid)
        self.add_widget(Label(text="UID: "+ str(self.article_read.UID[comp].values)))
        self.add_widget(Label(text="Name: "+str(self.article_read.Name[comp].values)))
        self.add_widget(Label(text="Time: "+str(self.article_read.TimeStamp[comp].values)))
        self.add_widget(Label(text="Height: "+str(self.article_read.Height[comp].values)))
        self.add_widget(Label(text="Weight: "+str(self.article_read.Weight[comp].values)))
        self.add_widget(Label(text="Allergy: "+str(self.article_read.Allergy[comp].values)))
        #print(self.__class__.pid)


class ScanUID(BoxLayout):
    
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        Gridr = navbar.nav()
        self.Grid1 = GridLayout(cols = 2)
        self.add_widget(Gridr)
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
        self.orientation='vertical'
        self.spacing = 320
        Gridr = navbar.nav()
        self.add_widget(Gridr)

        Gridmain = GridLayout(cols = 2,size_hint=(1.0,0.03),pos_hint={'bottom x' : 1},pos=(10,10),spacing = 30)
        
        view = Button(text="View Patient Data",on_press=self.getuid)
        add = Button(text="Add New Patient",on_press=self.adduid)
        
        Gridmain.add_widget(view)
        Gridmain.add_widget(add)
        
        self.add_widget(Gridmain)

    def getuid(self,instance):
        app.screenManager.current = "GetUID"
    def adduid(self,instance):
        app.screenManager.current = "UpdateInfo"


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

        self.UpdateInfo = Update_info()
        UpdateInfoScreen = Screen(name="UpdateInfo")
        UpdateInfoScreen.add_widget(self.UpdateInfo)
        self.screenManager.add_widget(UpdateInfoScreen)

        return self.screenManager


      
if __name__ == "__main__":
    app = HealthCare()
    app.run()