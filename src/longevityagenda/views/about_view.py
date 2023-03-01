import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

class AboutView(toga.Box):
    def __init__(self, heading='About', id=None, style=None):
        super().__init__(id=id, style=style)

        self.heading_label = toga.Label(
            heading,
            style=Pack(padding=(0, 5))
        )

        # Add the app description
        app_description = toga.Label(
            'This app is designed to help users improve their longevity through fitness, health, and social engagement.',
            style=Pack(padding=(0, 10))
        )

        # Add the developer information
        developer_info = toga.Label(
            'Developed by John Doe',
            style=Pack(padding=(0, 10))
        )

        # Add all labels to the box
        self.add(
            self.heading_label,
            app_description,
            developer_info,
            style=Pack(direction=COLUMN)
        )
