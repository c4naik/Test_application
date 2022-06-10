from re import A
from kivy.lang import Builder
from kivymd.app import MDApp,App
from kivy.animation import Animation
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from kivy.config import Config
from kivy.clock import Clock
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import Label
import requests
from kivy.factory import Factory


help_str = '''
#:import Factory kivy.factory.Factory
ScreenManager:
    BaseScreen:
    Q1:
    Q2:
    Q3:
    FinalPage:
    TestMainScreen:
    BeginTestScreen:
    TestHistoryScreen:
    TestScreen:
    AdminMainScreen:
    WelcomeScreen:
    MainScreen:
    LoginScreen:
    OnlyLoginScreen:
    CodeScreen:
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
            
<Q1>:
    name:'q1'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: str( app.ini()) + str(app.show_q1().iloc[0]) + ". " + str(app.show_q1().iloc[1])
            text_size: self.width, None
            size_hint: 1, None
            height: self.texture_size[1]
            font_size:self.width/15
            color: 0,0,0
            canvas.before:
                Rectangle:
                    pos: self.pos
                    size: self.size
           
        Button:
            text: 'a. '+ str(app.show_q1().iloc[2])
            text_size: self.width, None
            font_size:self.width/15
            color: (1,1,0)
            on_release:
                
                app.count += 1
        Button:
            text: 'b. '+ str(app.show_q1().iloc[3])
            text_size: self.width, None
            font_size:self.width/15
            color: (1,1,0)
            on_release:
              
        Button:
            text: 'c. '+str(app.show_q1().iloc[4])
            text_size: self.width, None
            font_size:self.width/15
            color: (1,1,0)
            on_release:
           
        Button:
            text: 'd. '+ str(app.show_q1().iloc[5])
            text_size: self.width, None
            font_size:self.width/15
            color: (1,1,0)
            on_release:
               
        MDFloatingActionButton:
            icon: 'arrow-right-bold'
            #arrow-right-bold-circle": "\uF056"
            pos_hint: {'center_x': .5, 'center_y': .15}
            elevation_normal: 8
            md_bg_color: utils.get_color_from_hex("#0E2433")
            text_color: utils.get_color_from_hex("#FFFFFF")
            on_press:
                root.manager.current = "q2"

<Q2>:
    name:'q2'
    
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: str(app.ini())+ str(app.show_q2().iloc[0]) + ". " + str(app.show_q2().iloc[1])
            text_size: self.width, None
            size_hint: 1, None
            height: self.texture_size[1]
            font_size:self.width/15
            color: 0,0,0
            canvas.before:
                Rectangle:
                    pos: self.pos
                    size: self.size
         
        Button:
            text: 'a. '+ str(app.show_q2().iloc[2])
            text_size: self.width, None
            font_size:self.width/15
            color: (1,1,0)
            on_release:
                app.count+=1
        Button:
            text: 'b. '+ str(app.show_q2().iloc[3])
            text_size: self.width, None
            font_size:self.width/15
            color: (1,1,0)
            on_release:
                
        Button:
            text: 'c. '+str(app.show_q2().iloc[4])
            text_size: self.width, None
            font_size:self.width/15
            color: (1,1,0)
            on_release:
               
        Button:
            text: 'd. '+ str(app.show_q2().iloc[5])
            text_size: self.width, None
            font_size:self.width/15
            color: (1,1,0)
            on_release:
               

       
        AnchorLayout:
            anchor_y:'bottom'
            BoxLayout:
                Button:
                    on_release:app.root.current = 'q1'
                    background_normal:'backbtn.png'
                    background_down:'backbtn.png'
                Button:
                    on_release:app.root.current = 'q3'
                    background_normal:'nextbtn.png'
                    background_down:'nextbtn.png'

<Q3>:
    name:'q3'
    
    BoxLayout:
        orientation: 'vertical'

        Label:
            text: str(app.ini())+str(app.show_q3().iloc[0]) + ". " + str(app.show_q3().iloc[1])
            text_size: self.width, None
            size_hint: 1, None
            height: self.texture_size[1]
            font_size:self.width/15
            color: 0,0,0
            canvas.before:
                Rectangle:
                    pos: self.pos
                    size: self.size
         
        Button:
            text: 'a. '+ str(app.show_q3().iloc[2])
            text_size: self.width, None
            font_size:self.width/15
            color: (1,1,0)
            on_release:
                app.count += 1
        Button:
            text: 'b. '+ str(app.show_q3().iloc[3])
            text_size: self.width, None
            font_size:self.width/15
            color: (1,1,0)
            on_release:
               
        Button:
            text: 'c. '+str(app.show_q3().iloc[4])
            text_size: self.width, None
            font_size:self.width/15
            color: (1,1,0)
            on_release:
                
        Button:
            text: 'd. '+ str(app.show_q3().iloc[5])
            text_size: self.width, None
            font_size:self.width/15
            color: (1,1,0)
            on_release:
               

        AnchorLayout:
            anchor_y:'bottom'
            BoxLayout:
                Button:
                    on_release:app.root.current = 'q2'
                    background_normal:'backbtn.png'
                    background_down:'backbtn.png'
                Button:
                    on_release:app.root.current = 'final'
                    app.add_score(app.score())
                    background_normal:'nextbtn.png'
                    background_down:'nextbtn.png'

<FinalPage>:
    name:'final'
    
    MDLabel:
        text: "Score : " + str(app.score())
        pos_hint : {'center_x':0.5,'center_y':0.7}
        size_hint: (0.5,0.2)
        
    MDTextButton:
        text: 'RETURN'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        size_hint:(0.5,0.2)
        on_press:
            root.manager.current = 'mainscreen'
            root.manager.transition.direction = 'right'
        
 
<TestMainScreen>:
    name: 'testmainscreen'
    MDLabel:
        text:
 
            
<BeginTestScreen>:
    name: 'begintestscreen'

    MDLabel:
        text: "Name - " + app.shx()
        pos_hint : {'center_x':0.5,'center_y':0.9}
        size_hint: (0.5,0.1)
    MDLabel:
        
        text:'Max Marks - '+ str( app.shx1())
        pos_hint : {'center_x':0.5,'center_y':0.75}
        size_hint: (0.5,0.1)
    MDLabel:
        text:'Time Limit - '+ str(app.shx2())
        pos_hint : {'center_x':0.5,'center_y':0.6}
        size_hint: (0.5,0.1)
        
    MDRaisedButton:
        text:'START TEST'
        size_hint: (0.33,0.17)
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press:
            root.manager.current = 'codescreen'
            root.manager.transition.direction='left'
        
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
    title:'Access Key is COEP#123 '
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
            
<CodeScreen>:
    name:'codescreen'
    MDLabel:
        text:'Enter Key'
        font_style:'H2'
        halign:'center'
        pos_hint: {'center_y':0.9}
    MDTextField:
        
        id:login_email
        pos_hint: {'center_y':0.6,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Access Code'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"
  
    MDRaisedButton:
        text:'Login'
        size_hint: (0.13,0.07)
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press:
            app.acs_code()
            
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
        on_press:
            #app.show_marks()
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
        

  




'''


class BaseScreen(Screen):
    pass
class TestMainScreen(Screen):
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
class CodeScreen(Screen):
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



class HomePage(Screen):
    pass
    
class Q1(Screen):
    pass

class Q2(Screen):
    pass

class Q3(Screen):
    pass

class FinalPage(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass


class IncrediblyCrudeClock(MDLabel):
    a = NumericProperty(5)  # seconds

    def start(self):
        Animation.cancel_all(self)  # stop any current animations
        self.anim = Animation(a=0, duration=self.a)
        def finish_callback(animation, incr_crude_clock):
            incr_crude_clock.text = "FINISHED"
        self.anim.bind(on_complete=finish_callback)
        self.anim.start(self)

    def on_a(self, instance, value):
        self.text = str(round(value, 1))


class Clock(MDLabel):
     
    # Set the numeric property
    # i.e set the counter number you can change it accordingly
    a = NumericProperty(100)  # seconds
 
    # To start countdown
    def start(self):
        Animation.cancel_all(self)  # stop any current animations
        self.anim = Animation(a = 0, duration = self.a)
 
        # TO finish count down
        def finish_callback(animation, clock):
            clock.text = "FINISHED"
 
        self.anim.bind(on_complete = finish_callback)
        self.anim.start(self)
 
    # If u remove this there will be nothing on screen
    def on_a(self, instance, value):
        self.text = str(round(value, 1))
        
        
sm = ScreenManager()
sm.add_widget(BaseScreen(name = 'basescreen'))
sm.add_widget(TestMainScreen(name = 'testmainscreen'))
sm.add_widget(TestScreen(name = 'testscreen'))
sm.add_widget(TestHistoryScreen(name = 'testhistoryscreen'))
sm.add_widget(BeginTestScreen(name = 'begintestscreen'))
sm.add_widget(AdminMainScreen(name='adminmainscreen'))
sm.add_widget(WelcomeScreen(name = 'welcomescreen'))
sm.add_widget(MainScreen(name = 'mainscreen'))
sm.add_widget(LoginScreen(name = 'loginscreen'))
sm.add_widget(OnlyLoginScreen(name='onlyloginscreen'))
sm.add_widget(CodeScreen(name = 'codescreen'))
sm.add_widget(SignupScreen(name = 'signupscreen'))


class LoginApp(MDApp):
    count = 0
    def build(self):
        
        
        self.strng = Builder.load_string(help_str)
        
        self.url2 = "https://testrecord-ba907-default-rtdb.asia-southeast1.firebasedatabase.app/.json"
        
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
    auth2 = 'MmkkVvk0BFO1HMkdpagvcNr181mlWRP8mcr0hFVF'
    
    
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
    def add_score(self,score):  
        signup_info = str({f'\"{self.username}\":{{"Email":\"{self.mail}\","Test1_Score:\"{score}\"}}'})
        signup_info = signup_info.replace(".","-")
        signup_info = signup_info.replace("\'","")
        to_database = json.loads(signup_info)
        print((to_database))
        requests.patch(url = self.url,json = to_database)
        self.strng.get_screen('loginscreen').manager.current = 'loginscreen' 
        
           
    def acs_code(self):
        access = self.strng.get_screen('codescreen').ids.login_email.text
        
        # supported_loginEmail = loginEmail.replace('.','-')
        # supported_loginPassword = loginPassword.replace('.','-')
        # request  = requests.get(self.url+'?auth='+self.auth)
        # data = request.json()
        # emails= set()
        # for key,value in data.items():
        #     emails.add(key)
        if access =='COEP#123':
            #self.username = data[supported_loginEmail]['Username']
            
            self.strng.get_screen('q1').manager.current = 'q1'
            
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
            self.mail = data[supported_loginEmail]
            self.login_check=True
            self.strng.get_screen('mainscreen').manager.current = 'mainscreen'
        else:
            print("user no longer exists")
    def close_username_dialog(self,obj):
        self.dialog.dismiss()
        
    def Opt(self):
        self.strng.get_screen('testscreen')
        
    def show_marks(self):
        request  = requests.get(self.url2 +'?auth='+self.auth2)
        data = request.json()
        return data['Test1']['max_marks']
        
    def username_changer(self):
        if self.login_check:
            self.strng.get_screen('mainscreen').ids.username_info.text = f"welcome {self.username}"
            
      
          
    def show_q1(self):
        import pandas as pd
        url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTMrSUVtqQIZtz8iS_MmfhXdZ1q0Ra9b1yHarEoIiPsqzJrlfVpqhlHb9QQOeyQUqZY_qsZrZLj7R-9/pub?output=csv'
        df = pd.read_csv(url)
        return df.iloc[0]
    
    def show_q2(self):
        import pandas as pd
        url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTMrSUVtqQIZtz8iS_MmfhXdZ1q0Ra9b1yHarEoIiPsqzJrlfVpqhlHb9QQOeyQUqZY_qsZrZLj7R-9/pub?output=csv'
        df = pd.read_csv(url)
        return df.iloc[1]
    
    def show_q3(self):
        import pandas as pd
        url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTMrSUVtqQIZtz8iS_MmfhXdZ1q0Ra9b1yHarEoIiPsqzJrlfVpqhlHb9QQOeyQUqZY_qsZrZLj7R-9/pub?output=csv'
        df = pd.read_csv(url)
        return df.iloc[2]

    def shx(self):
        import pandas as pd
        url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTEg-QpgOrRDsAzQApQNwTpy-Ljv2548rppPAIZ4GYClnzE-fkI4zLpoq6efTuxIunuBfDNC7Ez1tSx/pub?output=csv'
        df = pd.read_csv(url)
        return df.iat[0,0]
    
    def shx1(self):
        import pandas as pd
        url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTEg-QpgOrRDsAzQApQNwTpy-Ljv2548rppPAIZ4GYClnzE-fkI4zLpoq6efTuxIunuBfDNC7Ez1tSx/pub?output=csv'
        df = pd.read_csv(url)
        return df.iat[0,1]
    
    def shx2(self):
        import pandas as pd
        url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTEg-QpgOrRDsAzQApQNwTpy-Ljv2548rppPAIZ4GYClnzE-fkI4zLpoq6efTuxIunuBfDNC7Ez1tSx/pub?output=csv'
        df = pd.read_csv(url)
        return df.iat[0,2]
    
    def inc(self):
        #if (self.a ==1):
            self.count += 1
            
    def ini(self):
        self.a = 1
        
    def counter_ini(self):
        self.count = 0
        self.a = 1
    
    def score(self):
        m = (self.count)*2
        return m 
    
    def timer(self):
        clock = Clock()
        clock.start()
        return clock

    count = 2
LoginApp().run()