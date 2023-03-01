# main.py
import csv
import os

from toga import App as TogaApp
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

from longevityagenda.views.main_view import MainView

CHALLENGES_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'challenges.csv')

def load_challenges():
    challenges = []
    with open(CHALLENGES_FILE, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            challenges.append(row)
    return challenges

class LongevityAgenda(TogaApp):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Load challenges
        self.challenges = load_challenges()

        # Set up main window and view
        self.main_view = MainView()

    def startup(self):
        self.main_window = self.main_view.main_window
        self.main_window.app = self

        self.main_window.show()


def main():
    return LongevityAgenda('Longevity Agenda', 'org.longevityagenda', startup=LongevityAgenda.startup)
