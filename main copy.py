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
from kivy.factory import Factory

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
    ProfileScreen:
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
        id:emailid
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
        on_release: root.forgotpassword(emailid.text)
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

<ProfileScreen>:
    name: "profile"
    MDBoxLayout:
        # md_bg_color: app.theme_cls.primary_color
        orientation:'vertical'

        MDToolbar:
            
            title: "Profile"
            left_action_items: [["arrow-left", lambda x:app.change_screen("home")]] 
            # left_action_items: [["arrow-left", lambda x: x]]
            # on_action_button:  root.manager.current = "home"
            elevation: 5
        MDFloatLayout:
            MDFloatLayout:
                size_hint_x:1
                size_hint_y:.3
                pos_hint:{"centre_x":.5,"center_y":.85}
                canvas:
                    Color:
                        rgb:(1,1,1,1)
                    Rectangle:
                        size:self.size
                        pos:self.pos
                        source:"SPRK.png"
            MDIconButton:
                icon:"pic1.png"
                user_font_size: "128sp"
                radius: [0, 25, 25, 25]
                pos_hint:{"center_x":.5,"center_y":.7}
            MDList:
                TwoLineAvatarIconListItem:
                    id:user_name
                    text: "User Name"
                    secondary_text: "Harsh"
                    IconLeftWidget:
                        icon: "account"
                    
                TwoLineAvatarIconListItem:
                    id:email
                    text: "Email"
                    secondary_text: "harshrai.09@rediffmail.com"
                    IconLeftWidget:
                        icon: "email"
                
                TwoLineAvatarIconListItem:
                    id:date_of_birth
                    text: "Date of Birth"
                    secondary_text: "23-10-2003"
                    IconLeftWidget:
                        icon: "calendar-month"
                    
<HomeScreen>:
    name: "home"
    NavigationLayout:
        ScreenManager:
            Screen:
                MDBoxLayout:
                    # md_bg_color: app.theme_cls.primary_color
                    orientation:'vertical'
                    canvas.before:
                        Rectangle:
                            pos: self.pos
                            size: self.size
                            source: 'SPRK.png'
                    MDToolbar:
                      
                        title: "Ave"
                        left_action_items: [ ['menu', lambda x: nav_drawer.set_state()]] 
                        elevation: 5
                    MDBoxLayout:
                        # md_bg_color: app.theme_cls.primary_color
                        orientation:'vertical'

                        MDBoxLayout:
                            id: root_chatroom
                            # md_bg_color: app.theme_cls.primary_color
                            orientation:'vertical'


                            ScrollView:
                                id: scrollarea
                                MDList:
                                    spacing: "10dp"
                                    padding: "10dp"
                                    id: container



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

                                MDIconButton:
                                    icon:"send"
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    md_bg_color: app.theme_cls.primary_color
                                    on_release: root.Input(msg_textbox.text)
        MDNavigationDrawer:
            id: nav_drawer
            ContentNavigationDrawer:
                orientation: 'vertical'
                padding: "8dp"
                spacing: "8dp"
                Image:
                    id: avatar
                    size_hint: (1,1)
                    source: "pic1.png"
                ScrollView:
                    DrawerList:
                        id: md_list          
                        MDList:
                            OneLineIconListItem:
                                text: "Profile"    
                                on_release: 
                                    root.manager.transition = NoTransition()
                                    root.manager.current = 'profile'                        
                                IconLeftWidget:
                                    icon: "face-profile"

                         
                            OneLineIconListItem:
                                text: "Logout"
                                on_release: 
                                    root.manager.transition = NoTransition()
                                    root.manager.current = 'login'
                                IconLeftWidget:
                                    icon: "logout"

<SendCard@MDCard>:
    id: stubborn_layout
    size_hint_y: None
    height: label.height # Bind to Label height to update according to font size, for example
    md_bg_color: app.theme_cls.primary_color
    radius: [25, 0, 25, 25]
    MDLabel:
    	id: label # Add id for referencing in stubborn_layout
    	size_hint_y: None
    	size: self.texture_size
    	padding_x: 20
    	padding_y: 20
        markup: True
        halign: "right"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        font_style: "H6"

<RecieveCard@MDCard>:
    id: stubborn_layout
    size_hint_y: None
    height: label.height # Bind to Label height to update according to font size, for example
    radius: [0, 25, 25, 25]
    MDLabel:
    	id: label # Add id for referencing in stubborn_layout
    	size_hint_y: None
    	size: self.texture_size
    	padding_x: 20
    	padding_y: 20
        font_style: "H6"        
        
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
    def forgotpassword(self,emailid):
        auth.send_password_reset_email(emailid)

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
            self.dialog = MDDialog(title='Exist',text="Email Already Exists Try Logging In", size_hint=(0.8, 1),buttons=[MDFlatButton(text='OK', on_release=self.switch_screen)])
            self.dialog.open()     
        

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def switch_screen(self,obj):
        self.close_dialog("")
        self.parent.current = 'login'

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

class ProfileScreen(Screen):
    pass

class HomeScreen(Screen):
    def Input(self,Data):  
        print(Data)      
        send_inst = Factory.SendCard()
        send_inst.ids.label.text=Data
        self.ids.container.add_widget(send_inst)
        print(send_inst.height)
        if Data.isnumeric():
            print("true")
            output=produce_answer(Data)
            print(output)
        else:
            output=process(Data)
            print(output)
            print("false")

        recieve_inst = Factory.RecieveCard()
        recieve_inst.width=self.ids.msg_textbox.size[0]
        recieve_inst.ids.label.text=output
        
        self.ids.container.add_widget(recieve_inst)
        self.ids.scrollarea.scroll_to(recieve_inst)
        self.ids.msg_textbox.text=""
# Create the screen manager
screen_manager = ScreenManager()
screen_manager.add_widget(LoginScreen(name='login'))
screen_manager.add_widget(ForgotScreen(name='forgot'))
screen_manager.add_widget(SignupScreen(name='signup'))
screen_manager.add_widget(ProfileScreen(name='profile'))
screen_manager.add_widget(HomeScreen(name='home'))
screen=""
class DemoApp(MDApp):

    class ContentNavigationDrawer(BoxLayout):
        pass

    class DrawerList(ThemableBehavior, MDList):
        pass
    def change_screen(self, screen1):
        # the same as in .kv: app.root.current = screen
        screen.current = screen1
    def build(self):
        global screen
        screen = Builder.load_string(screen_helper)
        screen.current = "profile"
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