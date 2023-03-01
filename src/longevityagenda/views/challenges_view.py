import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

class ChallengesView(toga.Box):
    def __init__(self, challenges, heading='Challenges', id=None, style=None):
        super().__init__(id=id, style=style)
        self.challenges = challenges

        self.heading_label = toga.Label(
            heading,
            style=Pack(padding=(0, 5))
        )

        self.challenge_buttons = [
            toga.Button(
                challenge['title'],
                on_press=self.challenge_handler(challenge),
                style=Pack(flex=1)
            ) for challenge in self.challenges
        ]

        self.box = toga.Box(
            children=self.challenge_buttons,
            style=Pack(direction=COLUMN)
        )

        self.add(
            self.heading_label,
            self.box,
            style=Pack(direction=COLUMN)
        )

    def challenge_handler(self, challenge):
        def handler(widget):
            # Handle challenge button press for the given challenge
            print(f"{challenge['title']} challenge button pressed")
        return handler
