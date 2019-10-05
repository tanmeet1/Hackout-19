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
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import csv


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
        Login =  Button(text='Login', on_press=self.Login_Callback, background_color=(1,0,0,1))
        Signup =  Button(text='SignUp', on_press=self.Signup_Callback,background_color=(1,0,0,1))
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


class Update_info(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
    
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
        #self.article_read = pd.read_csv("res/Singledata User Info.csv",names=["UID","Name","Time","Height","Weight","Allergy"])
        self.add_widget(Label(text="Patient Data"))
        self.orientation = 'vertical'

        
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

        back = Button(text='Back')
        back.bind(on_press=self.retback)
        self.add_widget(back)

    def retback(self,instance):
        app.screenManager.current = "AfterLogin"

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
        self.orientation = 'vertical'
        view = Button(text="View Patient Data")
        view.bind(on_press=self.getuid)
        self.add_widget(view)

        add = Button(text="Add New Patient")
        add.bind(on_press=self.adduid)
        self.add_widget(add)

        visual = Button(text="Visualize Patient Data")
        visual.bind(on_press=self.showVisual)
        self.add_widget(visual)

    def getuid(self,instance):
        app.screenManager.current = "GetUID"
    def adduid(self,instance):
        app.screenManager.current = "UpdateInfo"
    def showVisual(self,instance):
        app.screenManager.current = "VisualMenu"


class VisualMenu(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        self.userID = TextInput(text="Add UserID here",multiline=False)
        self.add_widget(self.userID)

        self.steps = Button(text="Steps")
        self.steps.bind(on_press=self.showSteps)
        self.add_widget(self.steps)

        self.sleep = Button(text="Sleep")
        self.sleep.bind(on_press=self.showSleep)
        self.add_widget(self.sleep)

        self.heartRate = Button(text="Heart Rate")
        self.heartRate.bind(on_press=self.showHeartRate)
        self.add_widget(self.heartRate)

        self.pp = Button(text="Past Prescriptions")
        self.pp.bind(on_press=self.showPP)
        self.add_widget(self.pp)


    def showSteps(self,instance):
        userID = self.userID.text
        app.stepsVisualPage.setUID(userID)
        app.screenManager.current = "StepsVisual"

    def showSleep(self,instance):
        userID = self.userID.text
        app.sleepVisualPage.setUID(userID)
        app.screenManager.current = "SleepVisual"

    def showHeartRate(self,instance):
        userID = self.userID.text
        app.heartRateVisualPage.setUID(userID)
        app.screenManager.current = "HeartRateVisual"

    def showPP(self,instance):
        userID = self.userID.text
        app.PPVisualPage.setUID(userID)
        app.screenManager.current = "PPVisual"


class StepsVisual(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(Label(text="Steps Data",size_hint=(0.25,0.25),pos_hint={'top ':1,'center_x':0.5}))

    def setUID(self,UID):
        data = pd.read_csv('res/Multidata User Info1.csv')
        
        step_data = data[data.UID==int(UID)]
        #print(sleep_data)

        x_axis = step_data.TimeStamp
        y_axis = step_data.Steps

        #print(x_axis)
        #print(y_axis)

        #plt.figure(sigsize=(10,10))
        ax = sns.lineplot(x_axis,y_axis)
        #ax.set_xticklables(rotation=90)
        plt.xticks(rotation=90)
        ax.get_figure().savefig("res/step_data.png")
        
        self.image = AsyncImage(source="res/step_data.png", allow_stretch=True)
        self.add_widget(self.image)
        
        self.back_button = Button(text="Back",on_press=self.Back_callBack,size_hint=(0.25,0.25),pos_hint={'top ':1,'center_x':0.5})
        self.add_widget(self.back_button)

    def Back_callBack(self,instance):
        self.remove_widget(self.image)
        self.remove_widget(self.back_button)
        app.screenManager.current = "VisualMenu"

    
class SleepVisual(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(Label(text="Sleep Data",size_hint=(0.25,0.25),pos_hint={'top ':1,'center_x':0.5}))

    def setUID(self,UID):
        data = pd.read_csv('res/Multidata User Info1.csv')
        
        sleep_data = data[data.UID==int(UID)]

        x_axis = sleep_data.TimeStamp
        y_axis = sleep_data.Sleep

        ax = sns.lineplot(x_axis,y_axis)
        plt.xticks(rotation=90)
        ax.get_figure().savefig("res/sleep_data.png")
        
        self.image = AsyncImage(source="res/sleep_data.png", allow_stretch=True)
        self.add_widget(self.image)
        
        self.back_button = Button(text="Back",on_press=self.Back_callBack,size_hint=(0.25,0.25),pos_hint={'top ':1,'center_x':0.5})
        self.add_widget(self.back_button)

    def Back_callBack(self,instance):
        self.remove_widget(self.image)
        self.remove_widget(self.back_button)
        app.screenManager.current = "VisualMenu"


class HeartRateVisual(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(Label(text="HeartRate Data",size_hint=(0.25,0.25),pos_hint={'top ':1,'center_x':0.5}))

    def setUID(self,UID):
        data = pd.read_csv('res/Multidata User Info1.csv')
        
        heartRate_data = data[data.UID==int(UID)]

        x_axis = heartRate_data.TimeStamp
        y_axis = heartRate_data.HR

        ax = sns.lineplot(x_axis,y_axis)
        plt.xticks(rotation=90)
        ax.get_figure().savefig("res/heartRate_data.png")
        
        self.image = AsyncImage(source="res/heartRate_data.png", allow_stretch=True)
        self.add_widget(self.image)
        
        self.back_button = Button(text="Back",on_press=self.Back_callBack,size_hint=(0.25,0.25),pos_hint={'top ':1,'center_x':0.5})
        self.add_widget(self.back_button)

    def Back_callBack(self,instance):
        self.remove_widget(self.image)
        self.remove_widget(self.back_button)
        app.screenManager.current = "VisualMenu"


class PPVisual(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(Label(text="Past Prescription Data",size_hint=(0.25,0.25),pos_hint={'top ':1,'center_x':0.5}))

    def setUID(self,UID):
        data = pd.read_csv('res/Multidata User Info1.csv')
        
        # sleep_data = data[data.UID==int(UID)]

        # x_axis = sleep_data.TimeStamp
        # y_axis = sleep_data.Sleep

        # ax = sns.lineplot(x_axis,y_axis)
        # plt.xticks(rotation=90)
        # ax.get_figure().savefig("res/pp_data.png")
        
        # self.image = AsyncImage(source="res/pp_data.png", allow_stretch=True)
        # self.add_widget(self.image)
        
        self.back_button = Button(text="Back",on_press=self.Back_callBack,size_hint=(0.25,0.25),pos_hint={'top ':1,'center_x':0.5})
        self.add_widget(self.back_button)

    def Back_callBack(self,instance):
        self.remove_widget(self.image)
        self.remove_widget(self.back_button)
        app.screenManager.current = "VisualMenu"


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

        self.VisualMenuPage = VisualMenu()
        VisualMenuScreen = Screen(name="VisualMenu")
        VisualMenuScreen.add_widget(self.VisualMenuPage)
        self.screenManager.add_widget(VisualMenuScreen)

        self.stepsVisualPage = StepsVisual()
        stepScreen = Screen(name="StepsVisual")
        stepScreen.add_widget(self.stepsVisualPage)
        self.screenManager.add_widget(stepScreen)

        self.sleepVisualPage = SleepVisual()
        sleepScreen = Screen(name="SleepVisual")
        sleepScreen.add_widget(self.sleepVisualPage)
        self.screenManager.add_widget(sleepScreen)

        self.heartRateVisualPage = HeartRateVisual()
        heartRateScreen = Screen(name="HeartRateVisual")
        heartRateScreen.add_widget(self.heartRateVisualPage)
        self.screenManager.add_widget(heartRateScreen)

        self.ppVisualPage = PPVisual()
        ppScreen = Screen(name="PPVisual")
        ppScreen.add_widget(self.ppVisualPage)
        self.screenManager.add_widget(ppScreen)


        return self.screenManager


      
if __name__ == "__main__":
    app = HealthCare()
    app.run()