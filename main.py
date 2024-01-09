
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, SlideTransition

from dashboard import DashScreen

from login import LoginScreen
from homepage import MainScreen
from signup import SignupScreen
class MyApp(MDApp):
    def build(self):



        sm = ScreenManager(transition=SlideTransition())
        main_screen = MainScreen(name='MainScreen')
        login_screen = LoginScreen(name='LoginScreen')
        signup_screen = SignupScreen(name='SignupScreen')
        sm.add_widget(main_screen)
        sm.add_widget(login_screen)
        sm.add_widget(signup_screen)
        sm.add_widget(DashScreen(name='dashboard'))


        # Set the initial screen to the login screen
        sm.current = 'MainScreen'

        # Set the screen manager for the login screen
        main_screen.app = self

        return sm





if __name__ == '__main__':
    MyApp().run()
