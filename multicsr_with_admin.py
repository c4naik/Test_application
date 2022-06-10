from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
import requests
help_str = '''
#:import Factory kivy.factory.Factory
ScreenManager:
    BaseScreen:
    BeginTestScreen:
    TestHistoryScreen:
    TestScreen:
    AdminMainScreen:
    WelcomeScreen:
    MainScreen:
    LoginScreen:
    OnlyLoginScreen:
    SignupScreen:
    

<BaseScreen>:
    name:'basescreen'
    MDLabel:
        halign :'center'
        text:'Welcome to Test'
        font_size : 36
        color : '0F0FCF'
        size_hint : (0.5,0.5)
        pos_hint : {'center_x':0.5, 'center_y':0.8}
    MDRaisedButton:
        text:'User'
        elevation:10
        pos_hint : {'center_x':0.5,'center_y':0.5}
        size_hint : (0.5,0.1)
        bold : True
        on_press: 
            root.manager.current = 'loginscreen'
            root.manager.transition.direction = 'left'
    MDRaisedButton:
        text:'Admin'
        elevation:10
        pos_hint : {'center_x':0.5,'center_y':0.3}
        size_hint : (0.5,0.1)
        bold : True
        on_press:
            root.manager.current = 'onlyloginscreen'
            root.manager.transition.direction = 'left'
            
<BeginTestScreen>:
    name: 'begintestscreen'
    MDLabel:
        text:'Quiz Name -'
        pos_hint : {'center_x':0.5,'center_y':0.9}
        size_hint: (0.5,0.1)
    MDLabel:
        text:'Max Marks -'
        pos_hint : {'center_x':0.5,'center_y':0.75}
        size_hint: (0.5,0.1)
    MDLabel:
        text:'Time Limit -'
        pos_hint : {'center_x':0.5,'center_y':0.6}
        size_hint: (0.5,0.1)
        
    MDRaisedButton:
        text:'START TEST'
        size_hint: (0.33,0.17)
        pos_hint: {'center_x':0.5,'center_y':0.2}
        #on_press:
        
    MDTextButton:
        text: 'Go Back'
        pos_hint: {'center_x':0.85,'center_y':0.2}
        on_press:
            root.manager.current = 'mainscreen'
            root.manager.transition.direction = 'right'
            
<TestHistoryScreen>:
    name :'testhistoryscreen' 
    MDTextButton:
        text: 'Go Back'
        pos_hint: {'center_x':0.85,'center_y':0.2}
        on_press:
            root.manager.current = 'mainscreen'
            root.manager.transition.direction = 'down'      
<TestScreen>:
    name: 'testscreen'
    MDLabel:
        text:'question'
        font_style:'H5'
        pos_hint: {'center_x':0.4,'center_y':0.7}
    MDTextButton:
        text: 'Test'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press:
            app.Opt()
    MDTextButton:
        text: 'Test'
        pos_hint: {'center_x':0.5,'center_y':0.7}
        on_press:
            app.Opt()
    MDTextButton:
        text: 'Test'
        pos_hint: {'center_x':0.5,'center_y':0.8}
        on_press:
            app.Opt()
    MDTextButton:
        text: 'Test'
        pos_hint: {'center_x':0.5,'center_y':0.9}
        on_press:
            app.Opt()
<MyPopup@Popup>
    auto_dismiss:False
    title:'Access Key is ZMP2345'
    size_hint:(0.6,0.2)
    pos_hint:{"x":0.2,"top":0.6}
    MDTextButton:
        text:"Close me"
        color:'white'
        on_release:root.dismiss()
        size_hint: (0.13,0.07)
        pos_hint: {'center_x':0.5,'center_y':0.2}

<AdminMainScreen>:
    name:'adminmainscreen'
    MDRaisedButton:
        text:'GenerateKey'
        size_hint: (0.13,0.07)
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_release: Factory.MyPopup().open()
    MDRaisedButton:
        text:'UploadQuiz'
        size_hint: (0.13,0.07)
        pos_hint: {'center_x':0.5,'center_y':0.4}
    MDTextButton:
        text: 'Go Back'
        pos_hint: {'center_x':0.85,'center_y':0.2}
        on_press:
            root.manager.current = 'onlyloginscreen'
            root.manager.transition.direction = 'right'      
<WelcomeScreen>:
    name:'welcomescreen'
    MDLabel:
        text:'Login'
        font_style:'H2'
        bold : True
        halign:'center'
        pos_hint: {'center_y':0.9}
    MDLabel:
        text:'&'
        font_style:'H2'
        halign:'center'
        pos_hint: {'center_y':0.7}
    MDLabel:
        text:'Signup'
        font_style:'H2'
        halign:'center'
        pos_hint: {'center_y':0.5}
    MDRaisedButton:
        text:'Login'
        pos_hint : {'center_x':0.4,'center_y':0.3}
        size_hint: (0.13,0.1)
        on_press: 
            root.manager.current = 'loginscreen'
            root.manager.transition.direction = 'left'
    MDRaisedButton:
        text:'Signup'
        pos_hint : {'center_x':0.6,'center_y':0.3}
        size_hint: (0.13,0.1)
        on_press:
            root.manager.current = 'signupscreen'
            root.manager.transition.direction = 'left'
        
<LoginScreen>:
    name:'loginscreen'
    MDLabel:
        text:'Login'
        font_style:'H2'
        halign:'center'
        pos_hint: {'center_y':0.9}
    MDTextField:
        
        id:login_email
        pos_hint: {'center_y':0.6,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Email'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"
    MDTextField:
        id:login_password
        pos_hint: {'center_y':0.4,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Password'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"
    MDRaisedButton:
        text:'Login'
        size_hint: (0.13,0.07)
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press:
            app.login()
            app.username_changer() 
            
        
    MDTextButton:
        text: 'Create an account'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press:
            root.manager.current = 'signupscreen'
            root.manager.transition.direction = 'up'
    MDTextButton:
        text: 'Go Back'
        pos_hint: {'center_x':0.85,'center_y':0.2}
        on_press:
            root.manager.current = 'basescreen'
            root.manager.transition.direction = 'right'
            
<OnlyLoginScreen>:
    name:'onlyloginscreen'
    MDLabel:
        text:'Login'
        font_style:'H2'
        halign:'center'
        pos_hint: {'center_y':0.9}
    MDTextField:
        
        id:login_email
        pos_hint: {'center_y':0.6,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Email'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"
    MDTextField:
        id:login_password
        pos_hint: {'center_y':0.4,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Password'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"
    MDRaisedButton:
        text:'Login'
        size_hint: (0.13,0.07)
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press:
            app.admin_login()
            app.username_changer() 
    MDTextButton:
        text: 'Go Back'
        pos_hint: {'center_x':0.85,'center_y':0.2}
        on_press:
            root.manager.current = 'basescreen'
            root.manager.transition.direction = 'right'
            
        

<SignupScreen>:
    name:'signupscreen'
    MDLabel:
        text:'Signup'
        font_style:'H2'
        halign:'center'
        pos_hint: {'center_y':0.9}
    MDTextField:
        id:signup_email
        pos_hint: {'center_y':0.6,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Email'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"
    MDTextField:
        id:signup_username
        pos_hint: {'center_y':0.75,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Username'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
    MDTextField:
        id:signup_password
        pos_hint: {'center_y':0.4,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Password'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"
    MDRaisedButton:
        text:'Signup'
        size_hint: (0.13,0.07)
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: app.signup()
    MDTextButton:
        text: 'Already have an account'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press:
            root.manager.current = 'loginscreen'
            root.manager.transition.direction = 'down'
  
    
    
<MainScreen>:
    name: 'mainscreen'
    MDLabel:
        id:username_info
        text:'Hello Main'
        font_style:'H4'
        pos_hint: {'center_x':0.54,'center_y':0.95}
        
    MDLabel:
        text:'Available Tests -'
        font_style:'H5'
        pos_hint: {'center_x':0.74,'center_y':0.8}
        
    MDRaisedButton:
        text:'Test1'
        size_hint: (0.4,0.07)
        pos_hint: {'center_x':0.5,'center_y':0.7}
        on_press:
            root.manager.current = 'begintestscreen'
            root.manager.transition.direction = 'left'
            # app.admin_login()
            # app.username_changer()  
            
    MDRaisedButton:
        text:'Test2'
        size_hint: (0.4,0.07)
        pos_hint: {'center_x':0.5,'center_y':0.6}
        # on_press:
        #     app.admin_login()
        #     app.username_changer() 
            
    MDRaisedButton:
        text:'Test3'
        size_hint: (0.4,0.07)
        pos_hint: {'center_x':0.5,'center_y':0.5}
        # on_press:
        #     app.admin_login()
        #     app.username_changer() 
            
    MDRaisedButton:
        text:'Test4'
        size_hint: (0.4,0.07)
        pos_hint: {'center_x':0.5,'center_y':0.4}
        # on_press:
        #     app.admin_login()
        #     app.username_changer() 
    
    MDRaisedButton:
        text:'Test5'
        size_hint: (0.4,0.07)
        pos_hint: {'center_x':0.5,'center_y':0.3}
        # on_press:
        #     app.admin_login()
        #     app.username_changer()    
        
    MDRaisedButton:
        text:'View Test History'
        size_hint: (0.5,0.1)
        pos_hint: {'center_x':0.5,'center_y':0.15}
        background_color: (1,0.2,0.1,1)
        on_press:
            root.manager.current = 'testhistoryscreen'
            root.manager.transition.direction = 'up'
        #     app.admin_login()
        #     app.username_changer() 
  




'''


class BaseScreen(Screen):
    pass
class BeginTestScreen(Screen):
    pass
class TestHistoryScreen(Screen):
    pass
class TestScreen(Screen):
    pass
class AdminMainScreen(Screen):
    pass
class WelcomeScreen(Screen):
    pass
class MainScreen(Screen):
    pass
class LoginScreen(Screen):
    pass
class OnlyLoginScreen(Screen):
    pass
class SignupScreen(Screen):
    pass
class MDLabel():
    pass
class MDRaisedButton():
    pass
class MDTextButton():
    pass
class MDTextField():
    pass

sm = ScreenManager()
sm.add_widget(BaseScreen(name = 'basescreen'))
sm.add_widget(TestScreen(name = 'testscreen'))
sm.add_widget(TestHistoryScreen(name = 'testhistoryscreen'))
sm.add_widget(BeginTestScreen(name = 'begintestscreen'))
sm.add_widget(AdminMainScreen(name='adminmainscreen'))
sm.add_widget(WelcomeScreen(name = 'welcomescreen'))
sm.add_widget(MainScreen(name = 'mainscreen'))
sm.add_widget(LoginScreen(name = 'loginscreen'))
sm.add_widget(OnlyLoginScreen(name='onlyloginscreen'))
sm.add_widget(SignupScreen(name = 'signupscreen'))


class LoginApp(MDApp):
    def build(self):
        self.strng = Builder.load_string(help_str)
        self.url  = "https://loginset-testapp-default-rtdb.asia-southeast1.firebasedatabase.app/.json"
        return self.strng

    def signup(self):
        signupEmail = self.strng.get_screen('signupscreen').ids.signup_email.text
        signupPassword = self.strng.get_screen('signupscreen').ids.signup_password.text
        signupUsername = self.strng.get_screen('signupscreen').ids.signup_username.text
        if signupEmail.split() == [] or signupPassword.split() == [] or signupUsername.split() == []:
            cancel_btn_username_dialogue = MDFlatButton(text = 'Retry',on_release = self.close_username_dialog)
            self.dialog = MDDialog(title = 'Invalid Input',text = 'Please Enter a valid Input',size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
        if len(signupUsername.split())>1:
            cancel_btn_username_dialogue = MDFlatButton(text = 'Retry',on_release = self.close_username_dialog)
            self.dialog = MDDialog(title = 'Invalid Username',text = 'Please enter username without space',size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
        else:
            print(signupEmail,signupPassword)
            signup_info = str({f'\"{signupEmail}\":{{"Password":\"{signupPassword}\","Username":\"{signupUsername}\"}}'})
            signup_info = signup_info.replace(".","-")
            signup_info = signup_info.replace("\'","")
            to_database = json.loads(signup_info)
            print((to_database))
            requests.patch(url = self.url,json = to_database)
            self.strng.get_screen('loginscreen').manager.current = 'loginscreen'
    auth = 'OovbOiKqlkIaA0Nu0rIjhlJIxQVEyPGlgLJAV7kG'
    
    def admin_login(self):
        loginEmail = self.strng.get_screen('onlyloginscreen').ids.login_email.text
        loginPassword = self.strng.get_screen('onlyloginscreen').ids.login_password.text
        self.login_check = False
        # supported_loginEmail = loginEmail.replace('.','-')
        # supported_loginPassword = loginPassword.replace('.','-')
        # request  = requests.get(self.url+'?auth='+self.auth)
        # data = request.json()
        # emails= set()
        # for key,value in data.items():
        #     emails.add(key)
        if loginEmail =='admin1@gmail.com' and loginPassword == 'admin1':
            #self.username = data[supported_loginEmail]['Username']
            self.username = 'admin'
            self.login_check=True
            self.strng.get_screen('adminmainscreen').manager.current = 'adminmainscreen'
        else:
            print("user no longer exists")

    def login(self):
        loginEmail = self.strng.get_screen('loginscreen').ids.login_email.text
        loginPassword = self.strng.get_screen('loginscreen').ids.login_password.text

        self.login_check = False
        supported_loginEmail = loginEmail.replace('.','-')
        supported_loginPassword = loginPassword.replace('.','-')
        request  = requests.get(self.url+'?auth='+self.auth)
        data = request.json()
        emails= set()
        for key,value in data.items():
            emails.add(key)
        if supported_loginEmail in emails and supported_loginPassword == data[supported_loginEmail]['Password']:
            self.username = data[supported_loginEmail]['Username']
            self.login_check=True
            self.strng.get_screen('mainscreen').manager.current = 'mainscreen'
        else:
            print("user no longer exists")
    def close_username_dialog(self,obj):
        self.dialog.dismiss()
        
    def Opt(self):
        self.strng.get_screen('testscreen')
        
    def username_changer(self):
        if self.login_check:
            self.strng.get_screen('mainscreen').ids.username_info.text = f"welcome {self.username}"


LoginApp().run()