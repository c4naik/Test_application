import re
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
from datetime import datetime,timedelta
import time


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
    MainScreentwo
    MainScreen:
    LoginScreen:
    OnlyLoginScreen:
    CodeScreen:
    SignupScreen:
    

<BaseScreen>:
    name:'basescreen'
    Image:
        source:'logo.png'
        allow_stretch:True
        keep_ratio:True
        opacity:0.2
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
            text: str(app.show_q1().iloc[0]) + ". " + str(app.show_q1().iloc[1])
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
                print(app.count)
                
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

               
       
        AnchorLayout:
            anchor_y:'bottom'
            BoxLayout:
                MDLabel:
                    text:'End Time -'+str(app.get_start_time())
               
                MDLabel:
                    text:'Current Time-'+str(app.current_time())
 
                Button:
                    on_release:app.root.current = 'q2'
                    background_normal:'nextbtn.png'
                    background_down:'nextbtn.png'

<Q2>:
    name:'q2'
    
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: str(app.show_q2().iloc[0]) + ". " + str(app.show_q2().iloc[1])
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
                print(app.count)
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
                MDLabel:
                    text:'End Time -'+str(app.get_start_time())
             
                MDLabel:
                    text:'Current Time-'+str(app.current_time())
                    
                Button:
                    on_release:app.root.current = 'q3'
                    background_normal:'nextbtn.png'
                    background_down:'nextbtn.png'

<Q3>:
    name:'q3'
    
    BoxLayout:
        orientation: 'vertical'

        Label:
            text: str(app.show_q3().iloc[0]) + ". " + str(app.show_q3().iloc[1])
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
                print(app.count)
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
                MDLabel:
                    text:'End Time -'+str(app.get_start_time())

                MDLabel:
                    text:'Current Time-'+str(app.current_time())
  


                Button:
                    background_normal:'submitbtn.jpg'
                    background_down:'submitbtn.jpg'
                    on_release:
                        app.add_score(str(app.score()))
                        app.root.current = 'final'
                        
                        

<FinalPage>:
    name:'final'
    
    MDLabel:
        text: "Score : " + str(app.showscore())
        pos_hint : {'center_x':0.5,'center_y':0.7}
        size_hint: (0.5,0.2)
        
    MDTextButton:
        text: 'RETURN'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        size_hint:(0.5,0.2)
        on_press:
            root.manager.current = 'mainscreentwo'
            root.manager.transition.direction = 'right'
        
 
<TestMainScreen>:
    name: 'testmainscreen'
    MDLabel:
        text:
 
            
<BeginTestScreen>:
    name: 'begintestscreen'
    Image:
        source:'bg3.jpg'
        allow_stretch:True
        keep_ratio:True
        opacity:0.2
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
    Image:
        source:'bg4.jpg'
        allow_stretch:True
        keep_ratio:True
        opacity:0.2
    MDTextButton:
        text: "Your Test 1 Score :     " + str(app.showscore())    
        pos_hint : {'center_x':0.5,'center_y':0.5}
        size_hint: (0.5,0.2)
        
    MDTextButton:
        text: 'Go Back'
        pos_hint: {'center_x':0.85,'center_y':0.2}
        on_press:
            root.manager.current = 'mainscreentwo'
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
    auto_dismiss:True
    title:'Access Key'
    size_hint:(0.6,0.2)
    pos_hint:{"x":0.2,"top":0.6}
    MDLabel:
        text:'COEP#123'
        font_style:'H3'
        color:(1,1,1)
        pos_hint: {'center_x':0.4,'center_y':0.7}
<MyPopup_1@Popup>
    auto_dismiss:True
    title:'Test Submission Status '
    size_hint:(0.6,0.2)
    pos_hint:{"x":0.2,"top":0.6}
    MDLabel:
        text:'Link Submitted Successfully'
        font_style:'H4'
        color:(1,1,1)
        pos_hint: {'center_x':0.4,'center_y':0.7}
        
<AdminMainScreen>:
    name:'adminmainscreen'
    Image:
        source:'bg5.jpg'
        allow_stretch:True
        keep_ratio:True
        opacity:0.2
    MDTextField:
        id:signup_email
        pos_hint: {'center_y':0.6,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Enter Test Link'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        required: True
        mode: "rectangle"
    MDRaisedButton:
        text:'Submit Link'
        size_hint: (0.13,0.07)
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_press:app.admin_main()
        on_release: Factory.MyPopup_1().open()
    MDRaisedButton:
        text:'GenerateKey'
        size_hint: (0.13,0.07)
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_release: Factory.MyPopup().open()
    # MDRaisedButton:
    #     text:'UploadQuiz'
    #     size_hint: (0.13,0.07)
    #     pos_hint: {'center_x':0.5,'center_y':0.4}
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
    Image:
        source:'bg2.jpg'
        allow_stretch:True
        keep_ratio:True
        opacity:0.2
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
    Image:
        source:'bg4.jpg'
        allow_stretch:True
        keep_ratio:True
        opacity:0.2
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
    Image:
        source:'bg3.jpg'
        allow_stretch:True
        keep_ratio:True
        opacity:0.2
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
        text:'Proceed'
        size_hint: (0.13,0.07)
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press:
            app.writetime()
            app.acs_code()
            
    MDTextButton:
        text: 'Go Back'
        pos_hint: {'center_x':0.85,'center_y':0.2}
        on_press:
            root.manager.current = 'basescreen'
            root.manager.transition.direction = 'right'
       

<SignupScreen>:
    name:'signupscreen'
    Image:
        source:'bg4.jpg'
        allow_stretch:True
        keep_ratio:True
        opacity:0.2
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
            
<MainScreentwo>:
    name: 'mainscreentwo'
    Image:
        source:'bg1.jpg'
        allow_stretch:True
        keep_ratio:True
        opacity:0.2
    MDLabel:
        text:'Welcome'
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
    
  
    
    
<MainScreen>:
    name: 'mainscreen'
    Image:
        source:'bg1.jpg'
        allow_stretch:True
        keep_ratio:True
        opacity:0.4
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
class MainScreentwo(Screen):
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




        
sm = ScreenManager()
sm.add_widget(BaseScreen(name = 'basescreen'))
sm.add_widget(TestMainScreen(name = 'testmainscreen'))
sm.add_widget(TestScreen(name = 'testscreen'))
sm.add_widget(TestHistoryScreen(name = 'testhistoryscreen'))
sm.add_widget(BeginTestScreen(name = 'begintestscreen'))
sm.add_widget(AdminMainScreen(name='adminmainscreen'))
sm.add_widget(WelcomeScreen(name = 'welcomescreen'))
sm.add_widget(MainScreentwo(name='mainscreentwo'))
sm.add_widget(MainScreen(name = 'mainscreen'))
sm.add_widget(LoginScreen(name = 'loginscreen'))
sm.add_widget(OnlyLoginScreen(name='onlyloginscreen'))
sm.add_widget(CodeScreen(name = 'codescreen'))
sm.add_widget(SignupScreen(name = 'signupscreen'))


# file1 =  open('MyFile.txt', 'w')
# file1.write(start_time())
class QuizApp(MDApp):
    count = 0
    def chktime(self,currenttime,endtime):
        if endtime < currenttime :
            self.strng.get_screen('final').manager.current = 'final'
            
        
    def writetime(self):
        file1 =  open('MyFile.txt', 'w')
        file1.write(self.start_time() )
        
    def start_time(self):
        ini = datetime.now()+ timedelta(minutes=30)
        strt_time = ini.strftime("%H:%M:%S") 
        return strt_time
    
    def build(self):
        
        
        self.strng = Builder.load_string(help_str)
        
        self.url2 = "https://testrecord-ba907-default-rtdb.asia-southeast1.firebasedatabase.app/.json"
        
        self.url  = "https://loginset-testapp-default-rtdb.asia-southeast1.firebasedatabase.app/.json"
     
        return self.strng

    
    auth = 'OovbOiKqlkIaA0Nu0rIjhlJIxQVEyPGlgLJAV7kG'
    auth2 = 'MmkkVvk0BFO1HMkdpagvcNr181mlWRP8mcr0hFVF'
    
    
    def admin_login(self):
        loginEmail = self.strng.get_screen('onlyloginscreen').ids.login_email.text
        loginPassword = self.strng.get_screen('onlyloginscreen').ids.login_password.text
        self.login_check = False

        if loginEmail =='admin1@gmail.com' and loginPassword == 'admin1':
            self.username = 'admin'
            self.login_check=True
            self.strng.get_screen('adminmainscreen').manager.current = 'adminmainscreen'
        else:
            print("user no longer exists")
    def admin_main(self):
        Link=self.strng.get_screen('adminmainscreen').ids.signup_email.text
        file = open("TestLink.txt","w")
        file.write(Link)
    def get_link(self):
        file = open("TestLink.txt","r")
        data=file.read()
        print(data)
        return data
    def solve(self,s):
        pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
        if re.match(pat,s):
            return True
        return False
    def signup(self):
        signupEmail = self.strng.get_screen('signupscreen').ids.signup_email.text
        signupPassword = self.strng.get_screen('signupscreen').ids.signup_password.text
        signupUsername = self.strng.get_screen('signupscreen').ids.signup_username.text
        if self.solve(signupEmail) and (signupEmail.split() == [] or signupPassword.split() == [] or signupUsername.split() == []):
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
            
    def add_score(self,score): 
        score_info = str({f'\"{self.username}\":{{"score":\"{score}\"}}'})
        score_info = score_info.replace(".","-")
        score_info = score_info.replace("\'","")
        to_database = json.loads(score_info)
        print((to_database))
        requests.patch(url = self.url2,json = to_database)
        
           
    def acs_code(self):
        access = self.strng.get_screen('codescreen').ids.login_email.text
        
        if access =='COEP#123':
            
            self.strng.get_screen('q1').manager.current = 'q1'
            
    def showscore(self):
        request  = requests.get("https://testrecord-ba907-default-rtdb.asia-southeast1.firebasedatabase.app/.json"+'?auth='+'MmkkVvk0BFO1HMkdpagvcNr181mlWRP8mcr0hFVF')
        data = request.json()
        self.scr = data['x1']['score']
        print(self.scr)
        return self.scr        
            
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
            self.strng.get_screen('mainscreen').ids.username_info.text = f"Welcome {self.username}"
            
      
          
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
    
            
    
    def score(self):
        m = (self.count)*5
        return m 
        
    
    def timer(self):
        clock = Clock()
        clock.start()
        return clock
    
    def get_start_time(self):
        file = open("MyFile.txt","r")
        data=file.read()
        print(data)
        return data
    
    def current_time(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        return current_time
    
    def time_diff(self,start):
        t=self.current_time()
        if(t==start):
            return 1
        else:
            return 0

QuizApp().run()