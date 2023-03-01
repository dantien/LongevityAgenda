import toga
from toga.style.pack import COLUMN, ROW
from toga.style import Pack

class Dashboard:
    def __init__(self):
        self.box = toga.Box()

        label = toga.Label(
            'Dashboard',
            style=Pack(text_align=CENTER, font_weight=BOLD, font_size=24)
        )

        # Create the social features box
        social_box = toga.Box(style=Pack(direction=ROW, padding=10))
        feed_list = toga.List()
        feed_list.add('User 1 completed a 5k run')
        feed_list.add('User 2 reached their daily step goal')
        feed_list.add('User 3 lifted a personal best weight')
        feed_list.add('User 4 achieved their MAF training goal')
        feed_list.add('User 5 completed a yoga session')
        social_box.add(feed_list)
        social_box.style.update(
            background_color=secondary_color,
            padding_top=10,
            padding_bottom=10,
            padding_left=20,
            padding_right=20
        )

        # Create the stats box
        stats_box = toga.Box(style=Pack(direction=COLUMN, padding=10))
        stats_label = toga.Label(
            'Today\'s Stats',
            style=Pack(font_size=18)
        )
        stats_box.add(stats_label)

        # Add all boxes to main box
        self.box.add(label)
        self.box.add(social_box)
        self.box.add(stats_box)

    def refresh_stats(self, widget):
        # Code to refresh the displayed stats
        pass

    def connect_bluetooth_device(self, widget):
        # Code to connect to a Bluetooth device that measures heart rate
        pass
