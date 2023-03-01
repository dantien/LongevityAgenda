import toga
from toga.style import Pack
from toga.style.pack import *

class SignupView(toga.Box):
    def __init__(self, heading='Sign Up', id=None, style=None):
        super().__init__(id=id, style=style)

        self.heading_label = toga.Label(
            heading,
            style=Pack(padding=(0, 5))
        )

        self.username_input = toga.TextInput(placeholder='Username')
        self.email_input = toga.TextInput(placeholder='Email')
        self.password_input = toga.PasswordInput(placeholder='Password')

        self.signup_button = toga.Button(
            'Sign Up',
            on_press=self.signup_handler,
            style=Pack(flex=1)
        )

        self.add(
            self.heading_label,
            self.username_input,
            self.email_input,
            self.password_input,
            self.signup_button,
            style=Pack(direction=COLUMN, padding=10, spacing=5)
        )

    def signup_handler(self, widget):
        username = self.username_input.value
        email = self.email_input.value
        password = self.password_input.value

        # TODO: implement signup functionality
        print(f'Signing up user {username} with email {email} and password {password}')
