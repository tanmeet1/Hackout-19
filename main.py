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
import datetime
import csv

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
            data.loc[UserID_Data]["Name"] = UserName_Data
            data.loc[UserID_Data]["Time"] = time_data
            data.loc[UserID_Data]["Height"] = Height_data
            data.loc[UserID_Data]["Weight"] = Weight_data
            data.loc[UserID_Data]["Allergy"] = Allergy_data
            #data.drop([0],axis=0)
            print(data)
            #data.to_csv('out.csv',index=True)
        else:
            with open('res/Singledata User Info.csv','a') as fd:
                    writer = csv.writer(fd)
                    writer.writerow(fields)


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

class Update_info(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        self.add_widget(Label(text="Patient Data"))
        self.orientation = 'vertical'
        # Grid1 = GridLayout(cols = 2)
        # Grid1.add_widget(Label(text = "Enter the Patient ID : "))
        # Grid1.uid = TextInput(multiline = False)
        # Grid1.add_widget(Grid1.pid)

        #self.add_widget(Grid1) 
        
    def update_info(self,pid):
        self.article_read = pd.read_csv("res/Singledata User Info.csv",names =['UID','Name','Time','Height','Weight','Allergy'])
        self.add_widget(Label(text=str(self.article_read.UID[self.article_read.UID == pid])))
        self.add_widget(Label(text=str(self.article_read.Name[self.article_read.UID == pid])))
        self.add_widget(Label(text=str(self.article_read.Time[self.article_read.UID == pid])))
        self.add_widget(Label(text=str(self.article_read.Height[self.article_read.UID == pid])))
        self.add_widget(Label(text=str(self.article_read.Weight[self.article_read.UID == pid])))
        self.add_widget(Label(text=str(self.article_read.Allergy[self.article_read.UID == pid])))
        #print(self.__class__.pid)


        
class ScanUID(BoxLayout):
    
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

        add = Button(text="Add New Patient")
        add.bind(on_press=self.adduid)
        self.add_widget(add)

    def getuid(self,instance):
        app.screenManager.current = "GetUID"
    def adduid(self,instance):
        app.screenManager.current = "UpdateInfo"
        Box1.add_widget(grid)
        self.add_widget(Box1)
    
    
    def Submit_Callback(self, instance):
        print("Submit Clicked")
        UserID_Data = str(self.userID.text)
        UserName_Data = str(self.userName.text)
        Height_data = str(self.hight.text)
        Weight_data = str(self.weight.text)
        Allergy_data = str(self.allergy.text)
        time_data = str(datetime.datetime.now())
        fields=[UserID_Data,UserName_Data,time_data,Height_data,Weight_data,Allergy_data]
        # with open('.csv', 'a') as csvFile:
        #     writer = csv.writer(csvFile)
        #     writer.writerow(fields)
        # csvFile.close()
        app.screenManager.current = "UpdateInfo"

    def Back_Callback(self, instance):
        print("Back Clicked")
        app.screenManager.current = "DataScreen"



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

        self.UpdateInfo = Update_info()
        UpdateInfoScreen = Screen(name="UpdateInfo")
        UpdateInfoScreen.add_widget(self.UpdateInfo)
        self.screenManager.add_widget(UpdateInfoScreen)

        self.UpdateInfo = Update_info()
        UpdateInfoScreen = Screen(name="UpdateInfo")
        UpdateInfoScreen.add_widget(self.UpdateInfo)
        self.screenManager.add_widget(UpdateInfoScreen)

        return self.screenManager



if __name__ == "__main__":
    app = HealthCare()
    app.run()
