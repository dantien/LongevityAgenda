# dashboard.py
import toga
from toga.style.pack import COLUMN, ROW
from toga.style import Pack

class Dashboard:
    def __init__(self):
        self.box = toga.Box()

        # Create the heading label
        heading_label = toga.Label(
            'Dashboard',
            style=Pack(text_align=CENTER, font_weight=BOLD, font_size=24, padding_top=20)
        )

        # Create the social features box
        social_box = toga.Box(style=Pack(direction=COLUMN, padding=(20, 10)))
        social_label = toga.Label(
            'Social Feed',
            style=Pack(font_weight=BOLD, font_size=18)
        )
        social_list = toga.List()
        social_list.data = [
            'User 1 completed a 5k run',
            'User 2 reached their daily step goal',
            'User 3 lifted a personal best weight',
            'User 4 achieved their MAF training goal',
            'User 5 completed a yoga session'
        ]
        social_box.add(social_label)
        social_box.add(social_list)

        # Create the stats box
        stats_box = toga.Box(style=Pack(direction=COLUMN, padding=(20, 10)))
        stats_label = toga.Label(
            'Today\'s Stats',
            style=Pack(font_weight=BOLD, font_size=18)
        )
        stats_table = toga.Table(
            headings=['Metric', 'Value'],
            data=[
                ['Steps', '8,642'],
                ['Distance', '4.5 mi'],
                ['Calories Burned', '625'],
                ['Active Time', '1h 5m']
            ],
            style=Pack(flex=1, padding_top=10)
        )
        refresh_button = toga.Button(
            'Refresh',
            on_press=self.refresh_stats,
            style=Pack(padding=(0, 10))
        )
        connect_button = toga.Button(
            'Connect Bluetooth Device',
            on_press=self.connect_bluetooth_device
        )
        stats_box.add(stats_label)
        stats_box.add(stats_table)
        stats_box.add(refresh_button)
        stats_box.add(connect_button)

        # Add all boxes to main box
        self.box.add(heading_label)
        self.box.add(social_box)
        self.box.add(stats_box)

    def refresh_stats(self, widget):
        # Code to refresh the displayed stats
        pass

    def connect_bluetooth_device(self, widget):
        # Code to connect to a Bluetooth device that measures heart rate
        pass
