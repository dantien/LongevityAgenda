# views/about_view.py
import toga
from toga.style.pack import COLUMN, Pack


class AboutView(toga.Box):
    def __init__(self):
        super().__init__(style=Pack(direction=COLUMN))

        self.heading = toga.Label(
            'About Longevity Agenda',
            style=Pack(padding=(0, 5))
        )

        self.description = toga.Label(
            'Longevity Agenda is a fitness and health tracking app designed to help you achieve your health goals. '
            'Use our app to track your progress, set challenges and goals, and connect with your friends and family to '
            'stay motivated on your fitness journey.',
            style=Pack(padding=(0, 5))
        )

        self.version = toga.Label(
            'Version 1.0.0',
            style=Pack(padding=(0, 5))
        )

        self.add(self.heading, self.description, self.version)
