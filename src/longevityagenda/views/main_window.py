# views/main_window.py
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from .profile_view import ProfileView

class MainWindow(toga.MainWindow):
    def __init__(self, title):
        super().__init__(title=title)

        # Create the profile view box
        profile_view = ProfileView(heading='My Profile')

        # Create a label to display a welcome message
        welcome_label = toga.Label(
            'Welcome to Longevity Agenda!',
            style=Pack(font_size=24, padding=(10, 20))
        )

        # Add the profile view and welcome label to the main box
        self.main_box.add(
            profile_view,
            welcome_label,
            style=Pack(direction=COLUMN)
        )

