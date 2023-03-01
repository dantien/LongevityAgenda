import toga
from toga.style.pack import *
from toga.style import Pack

class SettingsView(toga.Box):
    def __init__(self, heading='Settings', id=None, style=None):
        super().__init__(id=id, style=style)

        self.heading_label = toga.Label(
            heading,
            style=Pack(padding=(0, 5))
        )

        # Add heart rate monitor button
        self.heart_rate_monitor_button = toga.Button(
            'Heart Rate Monitor',
            on_press=self.heart_rate_monitor_handler,
            style=Pack(flex=1)
        )

        # Add all buttons to the box
        self.add(
            self.heading_label,
            self.heart_rate_monitor_button,
            style=Pack(direction=COLUMN)
        )

    def heart_rate_monitor_handler(self, widget):
        # Code to connect to Bluetooth heart rate monitor
        print('Connecting to Bluetooth heart rate monitor')
