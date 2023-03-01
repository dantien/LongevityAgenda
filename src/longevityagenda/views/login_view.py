import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

class LoginView(toga.Box):
    def __init__(self, heading='Login', id=None, style=None):
        super().__init__(id=id, style=style)

        # Add a heading label
        self.heading_label = toga.Label(
            heading,
            style=Pack(padding=(0, 5), font_size=24)
        )

        # Add the email input field
        self.email_input = toga.TextInput(
            placeholder='Email',
            style=Pack(flex=1, padding=(0, 5))
        )

        # Add the password input field
        self.password_input = toga.PasswordInput(
            placeholder='Password',
            style=Pack(flex=1, padding=(0, 5))
        )

        # Add the login button
        self.login_button = toga.Button(
            'Login',
            on_press=self.login_handler,
            style=Pack(flex=1, padding=(0, 5))
        )

        # Add the forgot password link
        self.forgot_password_link = toga.Link(
            'Forgot password?',
            url='https://example.com/forgot_password',
            style=Pack(padding=(0, 5))
        )

        # Add all widgets to the box
        self.add(
            self.heading_label,
            self.email_input,
            self.password_input,
            self.login_button,
            self.forgot_password_link,
            style=Pack(direction=COLUMN)
        )

    def login_handler(self, widget):
        # Handle login button press
        email = self.email_input.value
        password = self.password_input.value
        print(f'Login clicked. Email: {email}, Password: {password}')
