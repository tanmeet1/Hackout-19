from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
def nav():
    Grid1 = GridLayout(cols = 5,size_hint=(1.,0.07))
        
    index_page = Button(text="Index Main",size_hint=(.5,.5),size=(10,10),on_press=ra)
    login_page = Button(text="Login",size_hint=(.5,.5),size=(10,10),on_press=rb)
    signup_page = Button(text="Sign Up",size_hint=(.5,.5),size=(10,10),on_press=rc)
    help_page = Button(text="Help",size_hint=(.5,.5),size=(10,10),on_press=rd)
    about_page = Button(text ="About",size_hint=(.5,.5),size=(10,10),on_press=re)

    Grid1.add_widget(index_page)
    Grid1.add_widget(login_page)
    Grid1.add_widget(signup_page)
    Grid1.add_widget(help_page)
    Grid1.add_widget(about_page)
    return Grid1

def rr(app,A,B,C,D,E):
    ra(app,A)
    rb(app,B)
    rc(app,C)
    rd(app,D)
    re(app,E)

def ra(app,A):
    app.screenManager.current = A

def rb(app,B):
    app.screenManager.current = B

def rc(app,C):
    app.screenManager.current = C

def rd(app,D):
    app.screenManager.current = D

def re(app,E):
    app.screenManager.current = E
