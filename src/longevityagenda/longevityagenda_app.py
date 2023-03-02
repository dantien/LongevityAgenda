import toga
from toga.style.pack import COLUMN, Pack
from views.profile_view import ProfileView

class MyWindow(toga.Window):
    def __init__(self, title):
        super().__init__(title=title)

        # Create a box to contain the profile view
        self.profile_box = toga.Box()

        # Create an instance of the profile view and add it to the box
        self.profile_view = ProfileView()
        self.profile_box.add(self.profile_view)

        # Add the box to the main window
        self.content = self.profile_box


class SettingsView(toga.Box):
    def __init__(self, id=None, style=None):
        super().__init__(id=id, style=style)

        self.heading_label = toga.Label(
            'Settings',
            style=Pack(padding=(0, 5))
        )

        self.profile_view = ProfileView()

        self.add(
            self.heading_label,
            self.profile_view,
            style=Pack(direction=COLUMN)
        )


class LongevityAgenda(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

        settings_view = SettingsView()

        main_box.add(settings_view)

        self.main_window = toga.MainWindow(title=self.name, size=(640, 480))
        self.main_window.content = main_box
        self.main_window.show()

