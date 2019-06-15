import sys,os
import kivy

kivy.require('1.0.7')

from kivy.app import App 
from kivy.uix.label import Label 
from kivy.core.window import Window 
from kivy.uix.widget import Widget 
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from  kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

############################################################
sys.path.append("../")
from Handlers.LoginHandler import LoginHandler 

class LoginScreen(FloatLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
       	
        self.info_label = Label(text= "Login to Moodle ",
            # pos_hint={'x':-.47, 'y':-.47},
            
            pos = (0,-250),
            font_size = 12,
            color = (6.0, 1790.0, 0.0,1.0))
        
        self.add_widget(self.info_label)
        
        self.username_input, self.password_input = self.addTextInput()
       	self.username_label , self.password_label = self.addLabels()
        self.login_button = self.addButtons()

    def updateInfoLabel(self, text):
        self.info_label.text = text

    def addTextInput(self):

       	username_input = TextInput(
        	size_hint =  (.2, None),
        	height = 30,
        	multiline =False,
        	pos_hint={'x':.4, 'y':.7}
        	)

       	password_input = TextInput(
        	size_hint =  (.2, None),
        	height = 30,
        	multiline =False,
        	pos_hint={'x':.4, 'y':.6},
            password = True
        	)

        # add text field for username 
        self.add_widget(username_input)
        # add text field for password
        self.add_widget(password_input)
        return username_input, password_input
    
    def addLabels(self):
        # label the test field
        username_label  = Label(text= "Username : ",pos_hint={'x':-.17, 'y':.22})
        password_label  = Label(text= "Password : ",pos_hint={'x':-.17, 'y':.12})
        self.add_widget(username_label);self.add_widget(password_label)
        return username_label, password_label

    def addButtons(self):

        login_button = Button(text="login",
            size_hint=(.15,.09),
            pos_hint={'x':.65, 'y':.63},
            background_color =( 1.0, 140.0, 0.0, 1.0),
            font_size = 20)
        
        login_button.bind(on_press = self.getLoginData)
        self.add_widget(login_button)
        return login_button

    def remove_login_widget(self):
        self.remove_widget(self.username_input)    
        self.remove_widget(self.password_input)
        self.remove_widget(self.username_label)
        self.remove_widget(self.password_label)
        self.remove_widget(self.login_button)

    def getLoginData(self, obj):
        # User didnt enter a username
        if not self.username_input.text:
            self.updateInfoLabel("No username entered!")
        # user entered username but no password
        elif not self.password_input.text:
            self.updateInfoLabel("No Password entered!")
        # user entered username and password
        else:
            self.updateInfoLabel("Logging in to your account")
            loginHandler = LoginHandler(self.username_input.text, self.password_input.text)
            
            response, session = loginHandler.login(self)
            # sucessfull login 
            if not response is None and not session is None:
                self.remove_login_widget()
                
class MoodleApp(App):
    
    def __init__(self, **kwargs):
        super(MoodleApp, self).__init__(**kwargs)
        # save Login screen for updating the screen after login
        self.LoginScreen = LoginScreen()

    def build(self):
        self.title = "MoodleBot v.01"
        return self.LoginScreen

    