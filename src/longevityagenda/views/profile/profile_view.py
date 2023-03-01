# views/profile_view.py

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class ProfileView(toga.Box):
    def __init__(self, heading='Profile', id=None, style=None):
        super().__init__(id=id, style=style)

        self.heading_label = toga.Label(
            heading,
            style=Pack(padding=(0, 5))
        )

        # Add widgets to capture user information
        self.first_name_input = toga.TextInput(placeholder='First Name', style=Pack(flex=1))
        self.last_name_input = toga.TextInput(placeholder='Last Name', style=Pack(flex=1))
        self.email_input = toga.TextInput(placeholder='Email Address', style=Pack(flex=1))
        self.phone_input = toga.TextInput(placeholder='Phone Number', style=Pack(flex=1))
        self.address_input = toga.TextInput(placeholder='Address', style=Pack(flex=1))

        # Add a save button to save user profile
        self.save_button = toga.Button(
            'Save Profile',
            on_press=self.save_profile_handler,
            style=Pack(flex=1)
        )

        # Add all widgets to the box
        self.add(
            self.heading_label,
            self.first_name_input,
            self.last_name_input,
            self.email_input,
            self.phone_input,
            self.address_input,
            self.save_button,
            style=Pack(direction=COLUMN)
        )

    def save_profile_handler(self, widget):
        # Handle save profile button press
        first_name = self.first_name_input.value
        last_name = self.last_name_input.value
        email = self.email_input.value
        phone = self.phone_input.value
        address = self.address_input.value

        # Code to save user profile information to database or file
        print('User profile saved successfully')
