import sys,os
import kivy

kivy.require('1.0.7')

from kivy.app import App 
from kivy.core.window import Window 
from kivy.core.window import Window
from kivy.uix.label import Label 
from kivy.uix.widget import Widget 
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.dropdown import DropDown
from kivy.properties import ObjectProperty
############################################################
sys.path.append("../")
from Handlers.LoginHandler import LoginHandler 
from Handlers.ResponseHandler import ResponseHandler
from Handlers.CourseHandler import CourseHandler



class CourseDropDown(DropDown):
    pass

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

        # Widgets for folder path input 
        self.dnd_label = Label(
            text = "Drag and drop your directory of choice ",
            pos = (0,0),
            font_size = 20
            )
        self.file_path = ""
        self.dropdown = DropDown()
        self.main_btn = Button(text="Courses found",
            size_hint=(.88,.06),
            pos_hint={'x':.05, 'y':.88},
            background_color =( 1.0, 140.0, 0.0, 1.0),
            font_size = 16)

    def addToDropdown(self, course_btn):
        self.dropdown.add_widget(course_btn)

    # To Select the Module 
    # btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))

    def show_dropdown(self):
        self.main_btn.bind(on_release= self.dropdown.open)
        self.dropdown.bind(on_select=lambda instance, x: setattr(self.main_btn, 'text', x))
        self.add_widget(self.main_btn)
        # self.dropdown.open(self.main_btn)

    def notify(self, text):
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
    
    def setFilePath(self, filepath):
        self.file_path = filepath
        self.remove_widget(self.dnd_label)

    def remove_login_widgets(self):
            self.remove_widget(self.username_input)    
            self.remove_widget(self.password_input)
            self.remove_widget(self.username_label)
            self.remove_widget(self.password_label)
            self.remove_widget(self.login_button)

    def add_path_widgets(self):
        self.add_widget(self.dnd_label)

    def getLoginData(self, obj):
        # User didnt enter a username
        if not self.username_input.text:
            self.notify("No username entered!")
        # user entered username but no password
        elif not self.password_input.text:
            self.notify("No Password entered!")
        # user entered username and password
        else:
            self.notify("Logging in to your account")
            loginHandler = LoginHandler(self.username_input.text, self.password_input.text, self)
            
            response, session = loginHandler.login()
            
            # sucessfull login 
            if not response is None and not session is None:
                
                self.remove_login_widgets()
                
                responseHandler = ResponseHandler(response, session, self)
                courses = responseHandler.getCourses()
                self.notify(f"{len(courses)} courses were found")


                courseHandler = CourseHandler(session, self, courses)
                courseHandler.handle()


class MoodleApp(App):
    
    def __init__(self, **kwargs):
        
        super(MoodleApp, self).__init__(**kwargs)
        
        # save Login screen for updating the screen after login
        self.LoginScreen = LoginScreen()
        
        Window.bind(on_dropfile = self.on_file_drop)
    
    def build(self):
        self.title = "MoodleBot v.01"
        return self.LoginScreen

    def on_file_drop(self, window, file_path):
        
        # save the file path
        self.LoginScreen.setFilePath(file_path)

        # notify that file path has been dropped
        self.LoginScreen.notify("Dropped filepath.")
        # handle the filePath
        