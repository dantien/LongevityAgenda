# main.py
import csv
import os

from toga import App as TogaApp

from longevityagenda.views.main_view import MainView
from longevityagenda.views.settings_view import SettingsView


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

        # Set up settings view
        self.settings_view = SettingsView()

    def startup(self):
        self.main_window = self.main_view.main_window
        self.main_window.app = self

        # Set up settings menu item
        settings_item = self.main_view.settings_item
        settings_item.on_select = self.show_settings

        self.main_window.show()

    def show_settings(self, widget):
        settings_window = self.settings_view.settings_window
        settings_window.show()


def main():
    return LongevityAgenda('Longevity Agenda', 'org.longevityagenda', startup=LongevityAgenda.startup)
