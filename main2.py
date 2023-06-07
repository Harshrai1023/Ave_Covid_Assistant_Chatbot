# remove both line when build App
#keyboard input
from kivy.core.window import Window
Window.keyboard_anim_args = {'d': 0, 't': 'in_out_expo'}
Window.softinput_mode = "below_target"

from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, TransitionBase, FadeTransition, NoTransition
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
from kivymd.uix.label import MDLabel, MDIcon
from Card import MDCard
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.uix.dialog import MDDialog

from kivy.clock import  Clock
import pyrebase

from nltk import word_tokenize #to tokenize sentences
from nltk.corpus import stopwords #importing stopwords
from nltk.stem import WordNetLemmatizer #importing lemmatizer, alternately import any stemmer of your choice

# from android.permissions import request_permissions, Permission
# request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
from Ave_new import *


lemmatizer=WordNetLemmatizer() #creating lemmatizer object
question_list=["None","what are the symptoms of corona","what are the symptoms of corona"]
question_file=open(r'question.txt', 'r+')


#Configure and Connext to Firebase

firebaseConfig = {'apiKey': "AIzaSyBEgAe2oW3o32ETdVrpY8EybpCbUkfZaC0",
                  'authDomain': "avee-f69d2.firebaseapp.com",
                  'databaseURL': "https://avee-f69d2.firebaseio.com",
                  'projectId': "avee-f69d2",
                  'storageBucket': "avee-f69d2.appspot.com",
                  'messagingSenderId': "77370570586",
                  'appId': "1:77370570586:web:78482e5f25df9ebe03e563",}

firebase=pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()
db=firebase.database()

screen_helper = """
#Put in screen_helper for transiton including hash
#: import NoTransition kivy.uix.screenmanager.NoTransition
#: import SlideTransition kivy.uix.screenmanager.SlideTransition
#: import CardTransition kivy.uix.screenmanager.CardTransition
#: import SwapTransition kivy.uix.screenmanager.SwapTransition
#: import FadeTransition kivy.uix.screenmanager.FadeTransition
#: import WipeTransition kivy.uix.screenmanager.WipeTransition
#: import FallOutTransition kivy.uix.screenmanager.FallOutTransition
#: import RiseInTransition kivy.uix.screenmanager.RiseInTransition
ScreenManager:
    LoginScreen:
    ForgotScreen:
    SignupScreen:
    VerificationScreen:
    HomeScreen:
    
<LoginScreen>:
    name: 'login'
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'back.png'
    MDLabel:
        text: f"[color=#FFFFFF][b]Log in[/b][/color]"
        markup: True
        halign: "center"
        pos_hint: {"center_y":.67}
        font_style: "H6"
        
    MDTextField:
        id: Input_user_email
        text: "harshrai.09@rediffmail.com"
        hint_text: "Username or Email"
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        size_hint: .75,0.085
        color_mode: 'custom'
        current_hint_text_color: 1,1,1,1
        line_color_normal: 1,1,1,1
        icon_right: "shield-account"
        icon_right_color: 1,1,1,1
        # mode: "rectangle"
    
    MDTextField:
        id: Input_password
        text: "123456"
        hint_text: "Password"
        pos_hint: {"center_x":0.5, "center_y":0.52}
        size_hint: .75,0.085
        password: True
        current_hint_text_color: 1,1,1,1
        line_color_normal: 1,1,1,1
        icon_right: "eye"
        icon_right_color: 1,1,1,1
        # mode: "rectangle"
    
    MDRaisedButton:
        text: "Login"
        pos_hint: {"center_x": 0.5, "center_y":0.43}
        size_hint: .7,0.05
        on_release: root.Login() 
            
    MDTextButton:
        text: f"[b]Forgot Password?[/b]"
        markup: True
        pos_hint: {"center_x":0.5, "center_y":0.36}
        on_release: 
            root.manager.transition = WipeTransition(duration=1.2)
            root.manager.current = 'forgot'
    MDTextButton:
        text: f"[color=#FFFFFF][b]Don't have an account?[/color] Sign up[/b]"
        markup: True
        pos_hint: {"center_x":0.5, "center_y":0.3}
        on_release:
            root.manager.transition = WipeTransition(duration=1.2)
            root.manager.current = 'signup'
            
    
<ForgotScreen>:
    name: "forgot"
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'back.png'
    
    MDLabel:
        text: f"[color=#FFFFFF][b]Forgot Password[/b][/color]"
        markup: True
        halign: "center"
        pos_hint: {"center_y":.67}
        font_style: "H6"
        
    MDTextField:
        hint_text: "Username or Email"
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        size_hint: .75,0.08
        color_mode: 'custom'
        current_hint_text_color: 1,1,1,1
        line_color_normal: 1,1,1,1
        icon_right: "shield-account"
        icon_right_color: 1,1,1,1
        # mode: "rectangle"
    MDRaisedButton:
        text: "Forgot Password"
        pos_hint: {"center_x": 0.5, "center_y":0.5}
        size_hint: .7,0.05
        on_release: root.manager.current = "verification"
    MDTextButton:
        text: f"[color=#FFFFFF]Don't have an account?[/color] Sign up"
        markup: True
        pos_hint: {"center_x":0.5, "center_y":0.4}
        on_release: root.manager.current = 'signup'
    
    MDTextButton:
        text: f"[b][color=#FFFFFF]Back To[/color] Login[/b]"
        markup: True
        pos_hint: {"center_x":0.5, "center_y":0.33}
        on_release: root.manager.current = 'login'
      
<SignupScreen>:
    name: "signup"
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'back.png'
    
    MDLabel:
        text: f"[color=#FFFFFF][b]Sign Up[/b][/color]"
        markup: True
        halign: "center"
        pos_hint: {"center_y":.67}
        font_style: "H6"
        
    MDTextField:
        id: Email
        hint_text: "Email"
        pos_hint: {"center_x": 0.5, "center_y": 0.60}
        size_hint: .75,0.08
        color_mode: 'custom'
        current_hint_text_color: 1,1,1,1
        line_color_normal: 1,1,1,1
        icon_right: "email"
        icon_right_color: 1,1,1,1
        # mode: "rectangle"
    
    MDTextField:
        id: Username
        hint_text: "Username"
        pos_hint: {"center_x":0.5, "center_y":0.52}
        size_hint: .75,0.08
        color_mode: 'custom'
        current_hint_text_color: 1,1,1,1
        line_color_normal: 1,1,1,1
        icon_right: "account"
        icon_right_color: 1,1,1,1
        # mode: "rectangle"
    
    MDTextField:
        id: Password
        hint_text: "Password"
        pos_hint: {"center_x":0.5, "center_y":0.44}
        size_hint: .75,0.08
        color_mode: 'custom'
        current_hint_text_color: 1,1,1,1
        line_color_normal: 1,1,1,1
        password: True
        icon_right: "eye"
        icon_right_color: 1,1,1,1
        # mode: "rectangle"
    
    MDTextField:
        id: DateField
        hint_text: "Date of Birth"
        pos_hint: {"center_x":0.5, "center_y":0.36}
        size_hint: .75,0.08
        color_mode: 'custom'
        current_hint_text_color: 1,1,1,1
        line_color_normal: 1,1,1,1
        
        # mode: "rectangle"
    MDIconButton:
        icon: "calendar-month"
        pos_hint: {"center_x":0.825, "center_y":0.375}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        on_release: root.ShowDatepicker()
    MDRaisedButton:
        text: "Sign up"
        pos_hint: {"center_x": 0.5, "center_y":0.28}
        size_hint: .7,0.05
        on_release: root.SignUp() 
    
    MDTextButton:
        text: f"[color=#FFFFFF]Have an account?[/color] Log in"
        markup: True
        pos_hint: {"center_x":0.5, "center_y":0.22}
        on_release: root.manager.current = "login"
<VerificationScreen>:
    name: "verification"
    MDLabel:
        text: "Ave"
        halign: "center"
        pos_hint: {"center_y": .8}
        font_style: "H3"
    
    MDLabel:
        text: "Account verification"
        halign: "center"
        pos_hint: {"center_y":.73}
        font_style: "Subtitle2"
    
    MDLabel:
        text: "We've sent a verification code to your email."
        halign: "center"
        pos_hint: {"center_y":.67}
        font_style: "Body2"
        
    MDTextField:
        hint_text: "Enter your verification Code"
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        size_hint: .75,0.08
        max_text_length: 6
        # mode: "rectangle"
    MDRaisedButton:
        text: "Submit"
        pos_hint: {"center_x": 0.5, "center_y":0.52}
        size_hint: .7,0.05
    
    MDTextButton:
        text: "Resend code"
        pos_hint: {"center_x": 0.5, "center_y":0.45}
        on_release: root.manager.current = "verification"
    MDLabel:
        text: "Never share your verification code to anyone."
        halign: "center"
        pos_hint: {"center_y":.4}
        font_style: "Caption"

<HomeScreen>:
    name: "home"
    MDBoxLayout:
        # md_bg_color: app.theme_cls.primary_color
        orientation:'vertical'

        MDToolbar:
            id:profile_bar
            title: "Ave"
            left_action_items: [ ["arrow-left", lambda x:app.screen_manager.change_screen("home")]] 
            elevation: 5
        MDBoxLayout:
            # md_bg_color: app.theme_cls.primary_color
            orientation:'vertical'
            
            MDBoxLayout:
                id: root_chatroom
                # md_bg_color: app.theme_cls.primary_color
                orientation:'vertical'
                
            
                ScrollView:
                    id: msg_scroll_view
                    MDList:
                        spacing: "10dp"
                        padding: "10dp"
                        id:all_msgs
                        
                MDCard:
                    id:send_card
                    size_hint: None,None
                    size: root_chatroom.size[0], msg_textbox.size[1]
                    pos_hint: {"center_x": .5, "center_y": .5}
                    spacing: dp(2)
                    padding: dp(5)

                    ScrollView:        
                        MDTextField:
                            id:msg_textbox
                            multiline: True
                            on_text: root.chat_textbox()
                        
                        
                    MDIconButton:
                        icon:"send"
                        on_release: root.send_msg(msg_textbox.text)
"""


class LoginScreen(Screen):
    def Login(self):
        email = self.ids.Input_user_email.text 
        password = self.ids.Input_password.text
        if email == "" and password == "":
                self.dialog = MDDialog(title='Username and Password',text="Please enter a Username and Password to Login", size_hint=(0.8, 1),buttons=[MDFlatButton(text='OK', on_release=self.close_dialog)])
                self.dialog.open()
        elif email == "":
                self.dialog = MDDialog(title='Username',text="Please enter a Username to Login", size_hint=(0.8, 1),buttons=[MDFlatButton(text='OK', on_release=self.close_dialog)])
                self.dialog.open()
        elif password == "":
                self.dialog = MDDialog(title='Password',text="Please enter a Password to Login", size_hint=(0.8, 1),buttons=[MDFlatButton(text='OK', on_release=self.close_dialog)])
                self.dialog.open()
        else:
            print("sent")         
            Clock.schedule_once(lambda dt:self.login_try(), 0.5)
            
            
    def login_try(self):
        print("reached")
        email = self.ids.Input_user_email.text 
        password = self.ids.Input_password.text
        try:
            login = auth.sign_in_with_email_and_password(email, password)
            print("Successfully logged in!")
            # print(auth.get_account_info(login['idToken']))
            verified = auth.get_account_info(login['idToken'])['users'][0]['emailVerified']
            # auth.send_email_verification(login['idToken'])
            print(verified)    
            if verified == True:
                self.parent.transition = NoTransition()
                self.parent.current = 'home'
            else:#Not Verified
                self.dialog = MDDialog(title='Please Verify',text="Please Verify Your Account to Login", size_hint=(0.8, 1),buttons=[MDFlatButton(text='OK', on_release=self.close_dialog)])
                self.dialog.open()            
        except:
            self.dialog = MDDialog(title='Sign Up',text="The Username And Password Combination Does Not Exist Try Singing Up Or Check Your Network Connection", size_hint=(0.8, 1),buttons=[MDFlatButton(text='OK', on_release=self.close_dialog)])
            self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()      
    pass

class ForgotScreen(Screen):
    pass

class SignupScreen(Screen):
    def SignUp(self):
        email = self.ids.Email.text
        username = self.ids.Username.text
        password = self.ids.Password.text
        dateField = self.ids.DateField.text
        if email == "" or username == "" or password == "" or dateField == "" :
            self.dialog = MDDialog(title='Details Not Filled',text="Please Enter The Details to Sign Up", size_hint=(0.8, 1),buttons=[MDFlatButton(text='OK', on_release=self.close_dialog)])
            self.dialog.open()
        else:
            print("sent")         
            Clock.schedule_once(lambda dt:self.SignUp_try(), 0.5)

    def SignUp_try(self):
        print("Sign up...")
        email = self.ids.Email.text
        username = self.ids.Username.text
        password = self.ids.Password.text
        dateField = self.ids.DateField.text
        try:
            user = auth.create_user_with_email_and_password(email, password)
            auth.send_email_verification(user['idToken'])
            self.dialog = MDDialog(title='Verify',text="A Verification Mail has been sent to your mail Please Verify to Login", size_hint=(0.8, 1),buttons=[MDFlatButton(text='OK', on_release=self.close_dialog)])
            self.dialog.open()
        except: 
            print("Email already exists")       
        

    def close_dialog(self, obj):
        self.dialog.dismiss()
        

    def ShowDatepicker(self):
        from kivymd.uix.picker import MDDatePicker
        picker = MDDatePicker(callback=self.got_date)
        picker.open()

    def got_date(self,the_date):
        print(the_date)
        print(the_date.year)
        print(the_date.month)
        print(the_date.day)
        print("date")
        self.ids.DateField.text=str(the_date)
        
    pass

class VerificationScreen(Screen):
    pass

class HomeScreen(Screen):

    def chat_textbox(self):
        """
            MDCard size change when MSGbox use multilines.
            MDCard y axis size incress when MSGbox y axis size incress
        """
        fixed_Y_size = self.ids.root_chatroom.size[1]/3
        msg_textbox=self.ids.msg_textbox.size
        
        if msg_textbox[1] <= fixed_Y_size:
            
            self.ids.send_card.size[1]=msg_textbox[1]
            print(msg_textbox)
        else:
            self.ids.send_card.size[1]=fixed_Y_size
    
    def send_msg(self,msg_data):
        """
            When send button use to send msg this function call
            and clear MSGbox 
        """
        
        text_msg = MDLabel(text=msg_data,halign="left",)
        # text_msg.text_size=(None,None)
        # print(text_msg.texture.size)
        # text_msg.texture_update()
        # print(text_msg.text_size,text_msg.texture.size)        
        sizeX = self.ids.msg_textbox.size[0]    
        a=str(text_msg.text)
        print(len(a.split("\n")))
        sizeY = self.ids.msg_textbox.size[1]+40
        # ->> sizeY is equal to msg_textbox sizeY because text_msg sizeY not work 
        # that's why i use msg_textbox is called 'Jugaad'
        print(sizeY)
        print(text_msg.size)
        msg_card= MDCard(
            orientation= "vertical",
            size_hint=[None,None],
            size=[sizeX,sizeY],
            spacing=8,
            padding=20,
            elevation=9,
            ripple_behavior= True,
            radius= [25,25,25,0 ],
            pos_hint= {"center_x": .5, "center_y": .5}

        )
        msg_card.add_widget(text_msg)
        self.ids.all_msgs.add_widget(msg_card)
        print(msg_data)
        
        

        self.ids.msg_scroll_view.scroll_to(msg_card)
        self.ids.msg_textbox.text=""

# Create the screen manager
screen_manager = ScreenManager()
screen_manager.add_widget(LoginScreen(name='login'))
screen_manager.add_widget(ForgotScreen(name='forgot'))
screen_manager.add_widget(SignupScreen(name='signup'))
screen_manager.add_widget(VerificationScreen(name='verification'))
screen_manager.add_widget(HomeScreen(name='home'))

class DemoApp(MDApp):

    class ContentNavigationDrawer(BoxLayout):
        pass

    class DrawerList(ThemableBehavior, MDList):
        pass
    
    def build(self):
        screen = Builder.load_string(screen_helper)
        screen.current = "home"
        #print(self.theme_cls.primary_palette) color of palette
        if question_file.readlines() == []:
            try:    
                question_list=db.child("Database").child("Questions").get().val()
                self.clean_list(question_list)
                print("empty")
            except:
                pass #No internet box to be shown
        else:
            print("not empty")
            pass
        return screen
    
    def clean_list(self,question_list):    
        def process(enter): 
            global lemmatizer, question_file
            raw_words=word_tokenize(enter) #cleaning of sentence begins here
            words=[]
            for word in raw_words:
                words.append(word.lower())
                words_no_punc=[]
            for word in words:
                if word.isalpha():
                    words_no_punc.append(word)
            clean_words=[]
            stopword=stopwords.words("english")
            for word in words_no_punc:
                if word not in stopword:
                    clean_words.append(word) #cleaning of sentence concludes
            final_list=[] 
            for word in clean_words: #storing only the stem words rather than the actual words
                final_list.append(lemmatizer.lemmatize(word, pos="n"))
            question_file.write(" ".join(final_list))
            question_file.write("\n")
            #question_file.write("\n")
        length=len(question_list) 
        for i in range(1,length):
            process(question_list[i])   
        #f.close()
        question_file.close()


DemoApp().run()